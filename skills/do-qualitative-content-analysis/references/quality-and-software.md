# Quality, Documentation, and Software

## Internal Quality Checklist

Internal quality covers the data as well as the analysis. Work through both parts.

### Part A: Data Collection and Transcription

- How was the material recorded?
- Was a postscript prepared describing the interview or group situation, and when?
- Was the material transcribed in full, or selectively by an explicit rule?
- Which transcription rules were followed, and will they be disclosed?
- Who transcribed, and was transcription software involved?
- Was the transcript proof-read against the recording?
- Has the material been anonymized, and how?
- Can the recording still be synchronized with the transcript for re-checking?

See [transcription-and-anonymization.md](transcription-and-anonymization.md).

### Part B: Implementation of the Analysis

From the book's checklist (b), p. 196:

- The selected QCA method fits the research question, and the choice is justified.
- The data were coded by multiple independent coders — or the report says they were not.
- How consistency of the codings was achieved, and how inconsistencies were handled, is stated.
- The category system is coherent and well structured; definitions are precise and include typical examples.
- Memos were written during the analysis.
- Unusual or abnormal cases are identified and analyzed.
- The analysis takes the whole dataset into account rather than a subset of striking passages.
- The number of coding passes is recorded, and every assignment is traceable to its passage.
- Quotations were selected by a stated rule that admits contradictions and counter-examples, not only plausible illustrations.
- Conclusions can be justified from the data.
- What was documented and archived, how, and in what form, is recorded.

This skill adds (not in the book's checklist):

- The rules for the scope of coded segments are stated.
- Deductive categories were tested against data, and pilot coding led to documented revisions.
- Recoding followed changes to the category system.
- Cases remain visible in the category analysis.
- Counts, if used, have meaningful denominators and do not replace interpretation.

## Intercoder Comparison

Agreement between two or more coders in applying the category system is desirable and is a quality criterion (p. 201). The book advises working with two or more coders who code independently; coding by one person alone is sub-optimal and should be avoided. Where that is not possible — a thesis written alone, for instance — improve the explicit category definitions and prototypical examples, and say so (p. 106).

There are two ways to secure agreement in QCA (pp. 201–206):

**Consensual coding (qualitative).**

1. Two coders code the same text independently.
2. They compare their codings together, discuss the differences, and consult the category definitions.
3. Where they agree, that coding is recorded; suggestions for improving a definition are noted.
4. Where they cannot agree, a third person — ideally a supervisor for the coding phase named in advance — decides after hearing the arguments.
5. Avoid fixed coding pairs and “the wiser head gives in”.

**Calculating agreement (quantitative).** Because QCA does not segment the data in advance — segmenting and coding form a unity (p. 201) — coefficients cannot be transferred directly from quantitative content analysis. Calculation is most useful early in coding: percentage agreement per category shows which categories are problematic and need work (pp. 205–206). Consensual coding of all material is usually too laborious and is practicable mainly at the beginning of the coding phase.

Neither procedure guarantees the validity of the results (p. 206).

This skill adds: compare segmentation as well as category decisions; record whether a difference came from the definition, the context, or a legitimate difference of interpretation; recode affected material after revising a definition.

## Ethics During Analysis

This section is this skill's own; the book says little about ethics at the analysis stage. Anonymizing the transcripts does not settle the matter; see [transcription-and-anonymization.md](transcription-and-anonymization.md) for that stage. Three exposures are specific to this method:

- **Case summaries and case profiles reassemble the person.** Each is a condensed portrait of one participant across every category. Details that are individually harmless become identifying once gathered into one paragraph, particularly in a small organization or a single ward.
- **Evaluative categories assign a judgement.** Recording that a named case shows a "low" level of something is an assessment made against the researcher's standard, not a neutral description. Say whose standard it is, and consider what follows if the case is recognized.
- **Cross-tabs with small cells identify people.** A cell containing one case is not anonymous because the name was removed.

If the skill `analyze-qualitative-data-with-displays` is installed, its ethics section gives a general framework; it is not part of this package.

## Journal Reporting Checklists

This section is this skill's own; the book does not mention these checklists. Where the corpus came from interviews or focus groups and the target is a health journal, COREQ will usually be required; SRQR is the broader alternative. Neither replaces the documentation this method demands of itself — category development, coding-guide versions, and post-coding analysis. Complete the checklist, and where an item assumes a design you did not use, state what you did instead rather than leaving the cell blank or claiming compliance you cannot evidence. See the reporting-guideline section in `design-qualitative-study`.

## Validity Checks

Passing the internal checklist does not guarantee valid results. The book names four checks (pp. 206–207):

- discussion with experts outside the research team (peer debriefing);
- discussion of the results with research participants (member checking);
- an extended stay in the field, or a return to it;
- triangulation, or the use of mixed methods.

This skill adds: compare categories with source context and case summaries; examine negative and deviant cases; test alternative category boundaries; assess the conditions under which the findings transfer.

## QDA Software

Use software for:

- import, transcription linkage, anonymization, and organization;
- comments, memos, highlighting, and case summaries;
- category-system versions and coding;
- retrieval, summary grids, matrices, cross-tabs, and visualizations;
- team comparison and documentation;
- export of evidence and reports.

Do not let software folder structures dictate the category system. Invoke `use-nvivo-for-qualitative-analysis` for NVivo-specific implementation.
