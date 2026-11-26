#!/usr/bin/env python3
"""Validate the minimum evidence chain in a JTBD case-evidence CSV."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path


REQUIRED_COLUMNS = (
    "case_id",
    "episode_id",
    "stakeholder_role",
    "evidence_type",
    "evidence_excerpt",
    "source_locator",
    "circumstance",
    "desired_progress",
    "current_solution",
    "candidate_job_statement",
    "confidence",
    "rival_explanation",
)
REQUIRED_VALUES = (
    "case_id",
    "episode_id",
    "evidence_type",
    "evidence_excerpt",
    "source_locator",
    "circumstance",
    "desired_progress",
)
# Three tiers only, matching references/analysis-and-codebook.md section 5.2.
# "provisional" is the synonym that section uses for the lowest tier, so it is accepted
# but normalized, to stop a fourth de facto tier from appearing in the data.
CONFIDENCE_TIERS = {"low", "moderate", "high"}
CONFIDENCE_ALIASES = {"provisional": "low"}

# Controlled vocabularies from analysis-and-codebook.md section 2.1. Studies may extend
# these, so an unknown value warns rather than fails — but a typo should not pass silently.
KNOWN_EVIDENCE_TYPES = {
    "direct account",
    "observed behavior",
    "observed behaviour",
    "artifact/document",
    "artefact/document",
    "usage trace",
    "researcher inference",
}
KNOWN_STAKEHOLDER_ROLES = {
    "executor",
    "buyer",
    "user",
    "gatekeeper",
    "implementer",
    "supporter",
    "affected party",
}

# Solution-neutrality screen. Both scripts and templates are English-keyed, but job
# statements are routinely written in Traditional Chinese, so both vocabularies run.
SOLUTION_TOKENS_LATIN = re.compile(
    r"\b(app|application|platform|website|portal|device|product|service|feature|brand"
    r"|system|software|tool|dashboard|module)\b",
    re.IGNORECASE,
)
SOLUTION_TOKENS_CJK = re.compile(
    r"(APP|應用程式|平台|平臺|系統|軟體|軟件|網站|網頁|入口網|裝置|設備|儀器"
    r"|產品|服務|功能|品牌|工具|介面|程式|方案|模組)"
)
# CJK ideographs plus kana, used to detect scripts that do not delimit words with spaces.
CJK_CHARS = re.compile(r"[㐀-䶿一-鿿豈-﫿぀-ヿ]")

# A job statement must retain enough context to explain alternatives and trade-offs.
# Space-delimited text is measured in words; CJK text is measured in characters,
# because str.split() returns a single token for an entire Chinese sentence.
MIN_LATIN_WORDS = 3
MIN_CJK_CHARS = 6


def find_solution_terms(statement: str) -> list[str]:
    """Return solution-suggesting terms found in either script."""
    hits = SOLUTION_TOKENS_LATIN.findall(statement) + SOLUTION_TOKENS_CJK.findall(statement)
    seen: dict[str, None] = {}
    for hit in hits:
        seen.setdefault(hit.lower(), None)
    return list(seen)


def is_too_short(statement: str) -> bool:
    """True when the statement is too thin to carry circumstance, in either script."""
    cjk_chars = len(CJK_CHARS.findall(statement))
    latin_words = len(CJK_CHARS.sub(" ", statement).split())
    if cjk_chars and cjk_chars >= MIN_CJK_CHARS:
        return False
    if latin_words >= MIN_LATIN_WORDS:
        return False
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a JTBD evidence-table CSV.")
    parser.add_argument("input", type=Path)
    parser.add_argument(
        "--allow-drafts",
        action="store_true",
        help="Warn instead of fail for blank required cell values",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        handle = args.input.open(newline="", encoding="utf-8-sig")
    except OSError as exc:
        print(f"error: cannot open {args.input}: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    keys: Counter[tuple[str, str, str]] = Counter()
    row_count = 0

    with handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        missing = [name for name in REQUIRED_COLUMNS if name not in fieldnames]
        if missing:
            errors.append(f"missing columns: {', '.join(missing)}")
        else:
            for row_number, row in enumerate(reader, start=2):
                row_count += 1
                for field in REQUIRED_VALUES:
                    if not (row.get(field) or "").strip():
                        message = f"row {row_number}: {field} is blank"
                        (warnings if args.allow_drafts else errors).append(message)

                confidence = (row.get("confidence") or "").strip().lower()
                if confidence in CONFIDENCE_ALIASES:
                    warnings.append(
                        f"row {row_number}: confidence {confidence!r} is the lowest tier; "
                        f"record it as {CONFIDENCE_ALIASES[confidence]!r} so the study "
                        f"keeps three tiers, not four"
                    )
                elif confidence and confidence not in CONFIDENCE_TIERS:
                    errors.append(
                        f"row {row_number}: confidence must be one of "
                        f"{sorted(CONFIDENCE_TIERS)} or blank"
                    )

                evidence_type = (row.get("evidence_type") or "").strip().lower()
                if evidence_type and evidence_type not in KNOWN_EVIDENCE_TYPES:
                    warnings.append(
                        f"row {row_number}: evidence_type {evidence_type!r} is outside the "
                        f"standard set {sorted(KNOWN_EVIDENCE_TYPES)}; confirm it is a "
                        f"deliberate study-specific extension, not a typo"
                    )

                role = (row.get("stakeholder_role") or "").strip().lower()
                if role and role not in KNOWN_STAKEHOLDER_ROLES:
                    warnings.append(
                        f"row {row_number}: stakeholder_role {role!r} is outside the "
                        f"standard set {sorted(KNOWN_STAKEHOLDER_ROLES)}; confirm it is a "
                        f"deliberate study-specific role, not a typo"
                    )

                key = (
                    (row.get("case_id") or "").strip(),
                    (row.get("episode_id") or "").strip(),
                    (row.get("source_locator") or "").strip(),
                )
                if all(key):
                    keys[key] += 1

                statement = (row.get("candidate_job_statement") or "").strip()
                if statement:
                    terms = find_solution_terms(statement)
                    if terms:
                        warnings.append(
                            f"row {row_number}: candidate job may contain a solution term "
                            f"({', '.join(terms)}): {statement!r}"
                        )
                    if is_too_short(statement):
                        warnings.append(
                            f"row {row_number}: candidate job may be too short to retain context"
                        )

                excerpt = (row.get("evidence_excerpt") or "").strip()
                if len(excerpt) > 1200:
                    warnings.append(
                        f"row {row_number}: evidence_excerpt is very long; use a focused excerpt"
                    )

    for key, count in keys.items():
        if count > 1:
            warnings.append(f"duplicate case/episode/locator {key}: {count} rows")

    if row_count == 0:
        errors.append("no data rows")

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)

    if errors:
        print(
            f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s), {row_count} row(s)",
            file=sys.stderr,
        )
        return 1

    print(
        f"OK: {row_count} row(s), {len(warnings)} warning(s), required evidence fields present",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
