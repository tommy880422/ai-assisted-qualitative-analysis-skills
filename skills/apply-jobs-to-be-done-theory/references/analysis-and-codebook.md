# JTBD Analysis and Codebook

## Contents

1. Analytic stance
2. Preparation and case structure
3. First-cycle coding frame
4. Second-cycle displays
5. Deriving job statements
6. Switching-forces analysis
7. Stakeholder and system analysis
8. Desired outcomes and ODI
9. Cross-case interpretation
10. Negative cases and rival explanations
11. Team coding and reflexivity
12. Findings package

## 1. Analytic stance

Choose and state one of these stances:

- **Deductive framework analysis:** Apply pre-defined JTBD constructs while allowing an “other/emergent” channel.
- **Combined qualitative content analysis:** Begin with theory-led main categories and develop subcategories from data.
- **Abductive analysis:** Move iteratively between surprising episodes, JTBD propositions, and rival explanations.
- **Case-oriented narrative/process analysis:** Preserve temporal switching stories before comparing mechanisms.

Do not call the analysis grounded theory merely because coding is inductive. Do not call it reflexive thematic analysis if the goal is to populate a fixed JTBD codebook. Match labels to the method actually used.

Once the stance is chosen, run it with the dedicated skill rather than this file's summary: `do-qualitative-content-analysis` for Kuckartz-style QCA, `do-reflexive-thematic-analysis` for RTA, `select-and-code-qualitative-data` for coding craft generally. This file contributes the JTBD construct layer those methods will carry.

## 2. Preparation and case structure

### 2.1 Create identifiers

Use:

- `case_id`: one analytic case or participant, depending on design;
- `episode_id`: one bounded job episode;
- `source_locator`: transcript/field-note/document plus line, paragraph, timestamp, or page;
- `stakeholder_role`: executor, buyer, gatekeeper, implementer, supporter, affected party;
- `evidence_type`: direct account, observed behavior, artifact/document, usage trace, researcher inference.

Keep identity keys outside the analytic file.

### 2.2 Write a case summary before fragmenting data

For each episode, summarize:

1. Circumstance and setting.
2. Trigger/struggling moment.
3. Prior/current approach.
4. Alternatives and non-action.
5. Decision and trade-offs.
6. First and repeated use.
7. Perceived result and unresolved struggle.
8. Functional, emotional, and social evidence.
9. Other actors and institutional constraints.
10. Candidate job and rival interpretations.

### 2.3 Preserve evidence layers

Store separately:

- concise participant wording or quotation;
- researcher paraphrase;
- code;
- higher-order interpretation;
- confidence and unresolved question.

Never replace the source excerpt with the final job statement.

## 3. First-cycle coding frame

> Use `select-and-code-qualitative-data` for segmentation rules, memoing, recoding, and the move from codes to categories, and `use-nvivo-for-qualitative-analysis` to operationalize this frame as an NVivo project. What follows is the JTBD-specific content of the codebook, not a coding method in itself.

Use this as a starting frame, then adapt and version the codebook.

| Code | Include | Exclude | Key distinction |
|---|---|---|---|
| CIRCUMSTANCE | Concrete temporal, social, material, institutional, life-stage conditions | Demographics without episode relevance | Context that changes what progress/trade-offs matter |
| TRIGGER | Event or accumulation moving the issue into active consideration | General dissatisfaction with no transition | Start of a decision/change process |
| STRUGGLE | Experienced gap, friction, or unresolved tension | Proposed feature request | What makes current state no longer good enough |
| DESIRED_PROGRESS | Change the actor is trying to make | Solution or generic value | Movement from current to preferred state |
| FUNCTIONAL_DIMENSION | Practical accomplishment or performance | Feeling or reputation | What must work |
| EMOTIONAL_DIMENSION | Desired/avoided feeling or sense of self | Social perception by others | How the actor wants to feel |
| SOCIAL_DIMENSION | Desired/avoided perception, relationship, or belonging | Private emotion only | How the actor wants to be seen or relate |
| CURRENT_SOLUTION | Existing product, service, routine, person, workaround, or non-action | Hypothetical future concept | What is currently hired/tolerated |
| ALTERNATIVE | Option considered or plausible in the episode | Same solution feature | Job-defined competition |
| COMPENSATING_BEHAVIOR | Improvised combination or workaround caused by inadequate solutions | Ordinary preferred workflow | Evidence of unsatisfied job/constraint |
| NONCONSUMPTION | Deliberate, constrained, or satisfied non-use | Missing data | Distinguish reason for no adoption |
| PUSH | Force making the present situation less tolerable | Attraction to a new option | Compels change from current state |
| PULL | Attraction or expected progress offered by an alternative | Dissatisfaction with current state | Draws actor toward new state |
| HABIT_INERTIA | Familiarity, routine, sunk setup, coordination, or status quo | Fear about new solution | Favors staying because current path is established |
| ANXIETY_UNCERTAINTY | Perceived risk, unknown, learning cost, identity/reputation concern | General dislike of old solution | Opposes change because new path is uncertain |
| TRADE_OFF | Accepted loss/cost to obtain another benefit | Unprioritized wish list | Reveals decision criteria |
| BIG_HIRE | Purchase, enrollment, formal adoption, or selection | Mere awareness | Acquisition decision |
| LITTLE_HIRE | Actual, repeated, or embedded use | Ownership without use | Consumption/implementation decision |
| FIRE | Abandoned, reduced, or displaced solution/behavior | Addition with no displacement | What gives way to new solution |
| SUCCESS_CRITERION | How the actor judges satisfactory progress | Product specification stated by researcher | Basis of evaluation |
| OUTCOME_METRIC | Specific direction/metric/object/context criterion | Broad success phrase | Candidate ODI outcome |
| ADOPTION_OBSTACLE | Barrier to trying, buying, approving, or enrolling | Difficulty during actual use | Pre-use barrier |
| USE_OBSTACLE | Barrier to effective or repeated use | Awareness barrier | Post-adoption barrier |
| STAKEHOLDER_JOB | Another actor's desired progress | Focal actor's assumption about them without evidence | Analyze by role/source |
| HANDOFF_DEPENDENCY | Required coordination or transfer between actors | Independent action | System coupling |
| CONSEQUENCE | Perceived or observed result after action | Desired result before action | Keep reported and measured outcomes separate |
| CONTRADICTION | Mismatch across statements, actions, sources, or times | Minor wording variation | Analytic lead, not error |
| RIVAL_EXPLANATION | Non-JTBD account that could explain behavior | Additional JTBD code | Price, access, rule, social desirability, etc. |

`assets/jtbd-codebook-template.csv` ships with all 28 codes already populated from this table, so do not retype them. It adds three things the table above does not carry:

- `definition`: a one-line operational definition per code, distinct from the include rule.
- `parent_code`: a suggested nine-group structure (CONTEXT, PROGRESS, SOLUTION_LANDSCAPE, FORCES, DECISION, EVALUATION, OBSTACLES, SYSTEM, ANALYTIC_FLAGS). This grouping is a starting structure for import into CAQDAS, not a finding. Restructure it when the data warrant.
- `version` / `last_updated`: stamped `v1.0-seed` with a blank date. Set your own version and date the moment you change any definition.

`positive_example` and `negative_example` are deliberately blank. Fill them with real coded excerpts from your own corpus; never seed them with invented examples, which would defeat the purpose of an anchor example and violate the fabrication rule.

Add operational definitions, positive examples, negative examples, and decision rules for any study-specific subcodes.

## 4. Second-cycle displays

> Use `analyze-qualitative-data-with-displays` for display craft, evidence linking, and cross-case comparison generally. The four displays below are the ones that are diagnostic for JTBD specifically.

### 4.1 Episode timeline

| Stage | Evidence | Interpretation | Missing evidence |
|---|---|---|---|
| Baseline/current approach | | | |
| Trigger/first thought | | | |
| Passive consideration | | | |
| Active search | | | |
| Decision/non-decision | | | |
| Big Hire | | | |
| First Little Hire | | | |
| Repeated use/abandonment | | | |
| Aftermath | | | |

Do not force absent stages.

### 4.2 Case-by-construct matrix

Use rows as episodes and columns as:

- circumstance;
- progress;
- functional/emotional/social dimensions;
- current solution and alternatives;
- push/pull/habit/anxiety;
- success criteria;
- Big/Little Hire;
- stakeholder dependencies;
- outcome;
- rival explanation;
- candidate job;
- confidence.

### 4.3 Circumstance-by-job matrix

Use to determine whether apparently identical jobs differ by context or whether varied participants share a common job in similar circumstances. Avoid averaging across circumstances prematurely.

### 4.4 Job-by-solution matrix

Place candidate jobs in rows and all hired/fired alternatives in columns. Record strengths, weaknesses, cost, accessibility, anxiety reduction, and evidence. This reveals job-defined competition.

### 4.5 Stakeholder alignment matrix

Place stakeholder roles in rows and job, success criteria, cost bearer, value recipient, decision authority, dependency, conflict, and evidence in columns.

## 5. Deriving job statements

### 5.1 Generate candidates

For each recurring pattern:

1. Identify the common circumstance or triggering structure.
2. State the desired movement without a solution.
3. Check whether the statement explains considered alternatives.
4. Check functional, emotional, and social evidence.
5. Check what the actor fired, retained, or avoided.
6. Compare with negative cases.
7. Draft a narrower and a broader alternative.
8. Select the level that best explains decisions without losing context.

### 5.2 Score analytic confidence qualitatively

Use:

Use exactly three tiers, recorded in the `confidence` column as `high`, `moderate`, or `low`:

- **High:** repeated across independent episodes; direct and behavioral/documentary evidence; alternatives fit; negative cases addressed.
- **Moderate:** repeated direct accounts but limited triangulation or boundary evidence.
- **Low:** single episode, interviewer-shaped answer, abstract opinion, or unresolved rival explanation. "Provisional" is a synonym for this tier in prose, but do not record it as a fourth value in the data.

Do not turn this into a false numerical precision unless the study predefines and validates a rating procedure.

`assets/jtbd-worked-example.md` sections 4 and 5 show this generate-and-choose step on one constructed episode, including the narrower and broader versions that were rejected and why. Read it if candidate generation is producing either solutions or platitudes.

### 5.3 Reject weak statements

Reject if the candidate:

- names the focal product, feature, or channel;
- is only an activity with no sought progress;
- is so abstract that every case fits;
- combines several unrelated jobs;
- has no circumstance where context is theoretically central;
- explains no actual alternatives or trade-offs;
- comes only from researcher intuition.

## 6. Switching-forces analysis

For each episode, write evidence-based statements for:

- `PUSH`: Why the present became insufficient.
- `PULL`: Why the alternative promised progress.
- `HABIT/INERTIA`: What made the present easy to continue.
- `ANXIETY`: What made the alternative risky or uncertain.

Then examine:

- whether push and pull were both required;
- which force changed immediately before the decision;
- which experience reduced anxiety;
- whether habit explains non-switching better than satisfaction;
- whether a Big Hire occurred without Little Hire because use-stage anxiety or friction remained;
- whether the decision involved another stakeholder's force pattern.

Use a force diagram as a display, not as proof. Retain quotations/locators behind each arrow.

## 7. Stakeholder and system analysis

Do not create one blended “customer job” in multi-actor settings.

For every role:

1. Identify the job and circumstance.
2. Identify the success criteria and accountabilities.
3. Identify decision rights and resources.
4. Identify adoption and use forces.
5. Identify costs, value, and risk distribution.
6. Identify dependencies and handoffs.
7. Compare where jobs align, conflict, or remain invisible.

Distinguish:

- user value from buyer value;
- clinical/public value from operational value;
- implementation workload from intervention benefit;
- formal authority from practical influence;
- local adaptation from loss of the intervention's core function.

## 8. Desired outcomes and ODI

### 8.1 Build a job map

Use define, locate, prepare, confirm, execute, monitor, modify, and conclude as prompts. Replace each with study-specific goal statements. Exclude product actions and consumption-chain stages unless the latter are a separate analytic object.

### 8.2 Draft outcome statements

Use:

> direction of improvement + performance metric + object of control + contextual clarifier

Check each statement for:

- one criterion only;
- solution neutrality;
- stable language relative to the study horizon;
- clarity to the target respondent;
- evaluability for importance and satisfaction;
- no double negative;
- no causal claim;
- no embedded “and” joining two outcomes.

Net the list by removing exact duplicates while preserving substantively different conditions or metrics. Keep a decision log of merges and splits.

### 8.3 Collect ratings

Define the rating scale explicitly. If using a 1–5 response scale, specify how it becomes a 0–10 ODI input. One common source-specific procedure uses the percentage rating 4 or 5, divided by 10. Do not assume raw 1–5 means can be inserted into a threshold calibrated for 0–10 scores.

### 8.4 Calculate opportunity scores

Use the non-negative-gap form reported in the supplied Ulwick glossary:

> opportunity = importance + max(importance − satisfaction, 0)

Run `scripts/calculate_odi_scores.py` for deterministic calculation. With 0–10 inputs the opportunity score ranges from 0 to 20; the underserved threshold of 10 sits inside that range and is not the top of it.

```bash
python3 scripts/calculate_odi_scores.py outcomes.csv --output scored.csv
```

The defaults reproduce Ulwick: 0–10 inputs, underserved at `score >= 10`, overserved when satisfaction exceeds importance. If ratings are on another scale, declare every parameter rather than relying on defaults calibrated for 0–10:

```bash
python3 scripts/calculate_odi_scores.py outcomes.csv --scale-max 5 --threshold 5 --table-stake-cutoff 4
```

The script refuses parameter sets that could never fire, because that failure is otherwise silent — every outcome is simply labelled `no`.

Treat `score >= 10` as an ODI heuristic for “underserved,” not an inferential test. Also classify:

- table stakes: high importance and high satisfaction. The script's `--table-stake-cutoff` default of 8 is an operationalization, not a value stated in the source; declare whichever cutoff the study uses.
- appropriately served: neither underserved nor overserved;
- overserved: satisfaction exceeds importance. The default reproduces Ulwick's opportunity landscape, where the overserved region is simply satisfaction > importance. Use `--overserved-margin` if the study requires a stricter "materially exceeds" rule, and report the margin.

Run sensitivity checks with alternative thresholds and report the rank stability. Never report only a score without the underlying importance, satisfaction, sample, and uncertainty.

**Tool limitation.** The script produces point estimates only. It does not read the `n` column, weight by sample size, or compute confidence intervals. Calculate uncertainty separately in a statistics package, and produce the sensitivity run by executing the script repeatedly with different `--threshold` values and comparing the `rank` column.

### 8.5 Segment cautiously

If performing outcome-based segmentation:

- use respondent-level outcome data, not only aggregate scores;
- justify distance/model/cluster choices;
- avoid selecting a solution solely because it is interpretable;
- examine size, stability, separation, and resampling/external validation;
- profile clusters after—not before—the outcome structure is identified;
- avoid renaming demographic personas as outcome segments;
- retain uncertainty in membership and number of segments.

## 9. Cross-case interpretation

Move through:

1. Within-case summaries.
2. Pattern coding within stakeholder/circumstance groups.
3. Comparison across theoretically selected contrasts.
4. Candidate mechanisms and boundary conditions.
5. Negative-case revision.
6. Relationship to the selected JTBD formulation.
7. Rival theory or non-JTBD explanation.
8. Practical implication only after the analytic claim is stable.

Use wording that matches evidence:

- “Participants described…” for reported experience.
- “Observed episodes showed…” for observation.
- “The pattern is consistent with…” for theoretical interpretation.
- “This suggests…” for cautious inference.
- “The data do not establish…” for limits.

## 10. Negative cases and rival explanations

Search for:

- the same circumstance with a different job;
- the same proposed job with a different choice;
- strong push/pull but no switch;
- switching without a clear struggle;
- adoption without use;
- successful use despite predicted anxiety;
- stakeholder success that harms another role;
- workarounds that are preferred, not merely compensatory;
- nonconsumption caused by irrelevance rather than constraint;
- behavior explained by price, access, mandate, default, social desirability, or recall bias.

Revise the job statement, add a boundary condition, split the pattern, or downgrade confidence. Do not hide the case.

## 11. Team coding and reflexivity

> Use `select-and-code-qualitative-data` for team-coding procedure and intercoder work, including whether an agreement metric is appropriate at all. The reflexive memo prompts below are the JTBD-specific additions.

If using a structured codebook:

- train on the same small set of episodes;
- compare segmentation as well as code labels;
- discuss disagreements with source context visible;
- revise definitions and log decisions;
- double-code a purposeful subset if required by the methodology;
- use agreement metrics only when the analytic tradition and study purpose justify them.

Keep reflexive memos on:

- prior product or theory commitments;
- participant/researcher role asymmetry;
- assumptions about “progress” and rational choice;
- commercial language imported into academic analysis;
- translation choices;
- which cases feel persuasive and why;
- how solution exposure may have shaped accounts.

## 12. Findings package

For each main job or mechanism, provide:

1. Concise analytic claim.
2. Circumstances and boundary conditions.
3. Functional, emotional, and social dimensions where evidenced.
4. Timeline or current approach.
5. Alternatives, workaround, and nonconsumption.
6. Forces or desired outcomes.
7. Cross-case pattern and variation.
8. Negative/deviant case.
9. Evidence excerpts with anonymized locators.
10. Confidence and rival explanation.
11. Theoretical implication.
12. Applied implication, clearly separated.

Validate the structured evidence CSV with `scripts/validate_evidence_table.py` before drafting the narrative:

```bash
python3 scripts/validate_evidence_table.py case-evidence.csv
```

Blank required cells fail the run. While the table is still being filled, use `--allow-drafts` to downgrade those failures to warnings; never use it on the version behind reported findings. The solution-neutrality and statement-length screens run over both English and Traditional Chinese wording, but they are keyword screens, not a substitute for reading the statement.
