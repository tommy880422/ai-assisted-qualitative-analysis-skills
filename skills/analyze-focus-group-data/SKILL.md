---
name: analyze-focus-group-data
description: Analyze, interpret, compare, and report completed focus-group data while preserving group interaction and context. Use when the user provides transcripts, recordings, chat logs, field notes, debriefs, or coded exports and needs a focus-group-specific analytic plan, coding frame, within-group summary, cross-group comparison, interaction analysis, treatment of consensus, disagreement, silence, intensity, or absences, quality audit, findings narrative, or NVivo implementation plan. Do not use as the primary workflow for recruiting or moderating future groups.
---

# Analyze Focus-Group Data

Treat focus-group data as layered interactional evidence. Do not flatten the corpus into a bag of decontextualized quotations or participant counts.

## Workflow

1. **Inventory the corpus.** List groups, dates, categories, participants, moderators, mode, recording quality, transcripts, field notes, activities, artifacts, and debriefs. Record missing or uneven material.
2. **Preserve interaction.** Retain speaker, turn, group, question or activity, overlap, pauses when relevant, laughter, visible response, and moderator intervention. Read [analytic-units-and-interaction.md](references/analytic-units-and-interaction.md).
3. **Revisit the design.** Restate research questions, group-comparison logic, sampling decisions, and claims the design can support.
4. **Familiarize group by group.** Write a contextual memo for each session before cross-group coding.
5. **Code content and interaction.** Use substantive codes for what is discussed and interaction codes for how positions are formed, supported, contested, silenced, or transformed.
6. **Build within-group accounts.** Summarize central positions, variations, episodes, language, group dynamics, moderator effects, and negative or absent evidence.
7. **Compare groups.** Follow [workflow-and-matrices.md](references/workflow-and-matrices.md). Compare patterns by planned group categories and emergent contextual differences without turning groups into statistical replicates.
8. **Develop interpretations.** Distinguish participant accounts, interactional accomplishments, analyst interpretations, and broader theoretical claims.
9. **Test the account.** Examine exceptions, rival explanations, group composition effects, question-order effects, moderator influence, and data-quality limitations.
10. **Report transparently.** Use [quality-and-reporting.md](references/quality-and-reporting.md). Present interaction and comparison, not only isolated quotes.
11. **Implement in software if needed.** Read [nvivo-handoff.md](references/nvivo-handoff.md), then invoke `use-nvivo-for-qualitative-analysis` for operational steps.

## Required Output

Scale the answer to the request. A narrow question — one decision, one section, one paragraph to revise — gets a direct answer plus only the items that bear on it. Produce the full set below when the user is planning or writing up the whole study, or asks for it.

Return:

- corpus and design audit;
- declared analytic unit or units;
- code or analytic-frame proposal;
- one within-group summary template;
- one cross-group comparison matrix;
- candidate findings with supporting and counter-evidence;
- quality, ethics, and limitation notes;
- reporting outline and quotation plan.

Write in the user's language. When the user writes Chinese, reply in 正體中文 using Taiwanese methodological terminology, and give every method, criterion, and software term its English original in parentheses at first use — the literature, the thesis examiners, and the software interface all use the English form.

## Guardrails

- Do not report the number of speakers as population prevalence.
- Do not treat consensus as truth or disagreement as analytical failure.
- Do not infer individual silence as agreement, ignorance, or discomfort without contextual evidence.
- Do not remove moderator questions and interventions when they shaped the response.
- Do not merge all groups before writing within-group memos.
- Do not use quotations as self-explanatory proof; describe their group and interactional context.
- Do not overclaim independence when participants, settings, moderators, or recruitment networks overlap.

## Sources

Read [sources.md](references/sources.md) for the supplied-book chapter map.
