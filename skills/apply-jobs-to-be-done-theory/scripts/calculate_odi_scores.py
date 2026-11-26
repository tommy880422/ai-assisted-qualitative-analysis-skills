#!/usr/bin/env python3
"""Calculate transparent ODI-style opportunity scores from a CSV file.

Required columns: outcome, importance, satisfaction.
Inputs must already be transformed to the declared scale (0-10 by default).
Formula: importance + max(importance - satisfaction, 0).
"""

from __future__ import annotations

import argparse
import csv
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


REQUIRED = ("outcome", "importance", "satisfaction")


def decimal_arg(value: str) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"not a number: {value}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate ODI-style opportunity scores from 0-scale_max inputs."
    )
    parser.add_argument("input", type=Path, help="Input CSV")
    parser.add_argument("--output", type=Path, help="Output CSV; stdout if omitted")
    parser.add_argument("--scale-max", type=decimal_arg, default=Decimal("10"))
    parser.add_argument(
        "--threshold",
        type=decimal_arg,
        default=Decimal("10"),
        help=(
            "Heuristic underserved threshold; default 10, which is calibrated for "
            "0-10 inputs. Restate it whenever --scale-max is not 10."
        ),
    )
    parser.add_argument(
        "--table-stake-cutoff",
        type=decimal_arg,
        default=Decimal("8"),
        help=(
            "Flag outcomes with both importance and satisfaction at/above this value. "
            "Default 8 is an operationalization of Ulwick's 'very important and very "
            "satisfied', not a value stated in the source. Declare it in the write-up."
        ),
    )
    parser.add_argument(
        "--overserved-margin",
        type=decimal_arg,
        default=Decimal("0"),
        help=(
            "Flag overserved when satisfaction exceeds importance by more than this "
            "margin. Default 0 reproduces Ulwick's opportunity landscape, in which the "
            "overserved region is simply satisfaction > importance."
        ),
    )
    parser.add_argument("--digits", type=int, default=2, help="Decimal places in output")
    return parser.parse_args()


def check_scale_coherence(
    scale_max: Decimal, threshold: Decimal, cutoff: Decimal, margin: Decimal
) -> list[str]:
    """Reject parameter sets that would silently produce empty classifications.

    The opportunity score ranges 0 to 2*scale_max, so a threshold above that can never
    be met, and a table-stakes cutoff above scale_max can never be met. Both failures
    are silent: every row is simply labelled "no". Ulwick's threshold of 10 is
    calibrated for 0-10 inputs and must not be applied to raw 1-5 ratings.
    """
    problems: list[str] = []
    max_opportunity = scale_max * 2
    if threshold > max_opportunity:
        problems.append(
            f"--threshold {threshold} exceeds the maximum possible opportunity score "
            f"{max_opportunity} for --scale-max {scale_max}; no outcome could ever be "
            f"flagged underserved. Transform the ratings to 0-{scale_max} first, or set "
            f"a threshold justified for this scale."
        )
    if cutoff > scale_max:
        problems.append(
            f"--table-stake-cutoff {cutoff} exceeds --scale-max {scale_max}; no outcome "
            f"could ever be flagged as table stakes."
        )
    if margin < 0:
        problems.append("--overserved-margin must not be negative")
    if margin >= scale_max:
        problems.append(
            f"--overserved-margin {margin} is not smaller than --scale-max {scale_max}; "
            f"no outcome could ever be flagged overserved."
        )
    return problems


def parse_score(raw: str, field: str, row_number: int, scale_max: Decimal) -> Decimal:
    try:
        value = Decimal(raw.strip())
    except (InvalidOperation, AttributeError) as exc:
        raise ValueError(f"row {row_number}: {field} is not numeric: {raw!r}") from exc
    if value < 0 or value > scale_max:
        raise ValueError(
            f"row {row_number}: {field}={value} is outside 0-{scale_max}"
        )
    return value


def format_decimal(value: Decimal, digits: int) -> str:
    quantum = Decimal(1).scaleb(-digits)
    return str(value.quantize(quantum, rounding=ROUND_HALF_UP))


def main() -> int:
    args = parse_args()
    if args.scale_max <= 0:
        print("error: --scale-max must be positive", file=sys.stderr)
        return 2
    if args.digits < 0 or args.digits > 10:
        print("error: --digits must be between 0 and 10", file=sys.stderr)
        return 2

    problems = check_scale_coherence(
        args.scale_max, args.threshold, args.table_stake_cutoff, args.overserved_margin
    )
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 2

    # Ulwick's threshold sits at 1.0 * scale_max (10 on a 0-10 scale). A threshold far
    # above that is reachable only at extreme rating combinations, so it is almost
    # certainly a scale that was never transformed.
    if args.threshold > args.scale_max * Decimal("1.5"):
        print(
            f"warning: --threshold {args.threshold} is high relative to --scale-max "
            f"{args.scale_max}. Ulwick's heuristic of 10 assumes 0-10 inputs "
            f"(threshold = scale max). Confirm the ratings were transformed.",
            file=sys.stderr,
        )

    try:
        source = args.input.open(newline="", encoding="utf-8-sig")
    except OSError as exc:
        print(f"error: cannot open {args.input}: {exc}", file=sys.stderr)
        return 2

    with source:
        reader = csv.DictReader(source)
        fieldnames = reader.fieldnames or []
        missing = [name for name in REQUIRED if name not in fieldnames]
        if missing:
            print(f"error: missing required columns: {', '.join(missing)}", file=sys.stderr)
            return 2

        rows: list[dict[str, str | Decimal]] = []
        try:
            for row_number, row in enumerate(reader, start=2):
                outcome = (row.get("outcome") or "").strip()
                if not outcome:
                    raise ValueError(f"row {row_number}: outcome is blank")
                importance = parse_score(
                    row.get("importance") or "", "importance", row_number, args.scale_max
                )
                satisfaction = parse_score(
                    row.get("satisfaction") or "", "satisfaction", row_number, args.scale_max
                )
                opportunity = importance + max(importance - satisfaction, Decimal("0"))
                rows.append(
                    {
                        **row,
                        "outcome": outcome,
                        "importance": importance,
                        "satisfaction": satisfaction,
                        "opportunity_score": opportunity,
                        "underserved": "yes" if opportunity >= args.threshold else "no",
                        "overserved": (
                            "yes"
                            if satisfaction - importance > args.overserved_margin
                            else "no"
                        ),
                        "table_stake": (
                            "yes"
                            if importance >= args.table_stake_cutoff
                            and satisfaction >= args.table_stake_cutoff
                            else "no"
                        ),
                    }
                )
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2

    ranked = sorted(
        enumerate(rows),
        key=lambda item: (-item[1]["opportunity_score"], item[0]),  # type: ignore[operator]
    )
    ranks = {original_index: rank for rank, (original_index, _) in enumerate(ranked, start=1)}

    output_fields = list(fieldnames)
    for field in ("opportunity_score", "underserved", "overserved", "table_stake", "rank"):
        if field not in output_fields:
            output_fields.append(field)

    output_handle = None
    try:
        if args.output:
            output_handle = args.output.open("w", newline="", encoding="utf-8")
            target = output_handle
        else:
            target = sys.stdout
        writer = csv.DictWriter(target, fieldnames=output_fields, extrasaction="ignore")
        writer.writeheader()
        for index, row in enumerate(rows):
            rendered = dict(row)
            rendered["importance"] = format_decimal(row["importance"], args.digits)  # type: ignore[arg-type]
            rendered["satisfaction"] = format_decimal(row["satisfaction"], args.digits)  # type: ignore[arg-type]
            rendered["opportunity_score"] = format_decimal(
                row["opportunity_score"], args.digits  # type: ignore[arg-type]
            )
            rendered["rank"] = str(ranks[index])
            writer.writerow(rendered)
    except OSError as exc:
        print(f"error: cannot write output: {exc}", file=sys.stderr)
        return 2
    finally:
        if output_handle is not None:
            output_handle.close()

    print(
        f"Processed {len(rows)} outcomes. Report these settings with the scores: "
        f"input scale 0-{args.scale_max} (opportunity range 0-{args.scale_max * 2}), "
        f"underserved threshold {args.threshold}, table-stakes cutoff "
        f"{args.table_stake_cutoff}, overserved margin {args.overserved_margin}, "
        f"formula importance + max(importance - satisfaction, 0).",
        file=sys.stderr,
    )
    print(
        "note: this script reports point estimates only. It does not weight by n or "
        "compute uncertainty. Report the sample size, response rate, and a sensitivity "
        "run at alternative thresholds separately.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
