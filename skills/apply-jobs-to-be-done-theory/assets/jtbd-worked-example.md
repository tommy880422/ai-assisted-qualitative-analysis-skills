# Worked Example: One Episode from Transcript to Opportunity Score

> **THIS IS A CONSTRUCTED TEACHING EXAMPLE. THE PARTICIPANT, QUOTATIONS, RATINGS, AND SCORES ARE INVENTED.**
> Nothing here is data. Do not cite it, do not reuse its job statements as findings, and do not carry its
> stakeholder categories into a real study as predetermined truth. It exists to show the shape of the
> evidence chain, not its content. Replace every cell with your own corpus before any analysis.

Domain: post-discharge care coordination. It is used because the executor, the patient, and the payer are
three different people, which is where most JTBD analyses collapse.

---

## 1. Scope the episode

| Field | Value |
|---|---|
| `case_id` | C07 |
| `episode_id` | C07-E01 |
| Job executor | 家庭照顧者（女兒），非病人本人、非付費者 |
| `stakeholder_role` | executor |
| Episode boundary | 從出院前一日的出院準備說明，到返家後第 10 天第一次回診 |
| Unit of analysis | 此一 job episode，而非「照顧者」這個人 |

Note the executor is not the patient. Under Christensen's sense the executor is whoever seeks the progress;
if this study used Ulwick's ODI instead, the buyer's financial outcomes would be a separate interview.

## 2. Segment and code close to the data

Constructed excerpt, `source_locator` C07-T01:112–140:

> 「出院那天護理師講了一大串，我手機一直錄但回到家整個亂掉。藥有三種要分開時間，我媽又聽不懂。
> 我後來自己拿一張紙畫格子貼在冰箱上，早中晚打勾。其實醫院有給衛教單，但那張單是講衛教，不是講我
> 家的時間表。我最怕的是漏掉哪一次，又不好意思一直打去護理站問。」

| Segment | Code | Why this code and not the neighbouring one |
|---|---|---|
| 「護理師講了一大串…回到家整個亂掉」 | `CIRCUMSTANCE` | 具體時間、地點、資訊負荷；不是人口學屬性 |
| 「藥有三種要分開時間，我媽又聽不懂」 | `STRUGGLE` | 已經歷的落差，不是功能許願 |
| 「自己拿一張紙畫格子貼在冰箱上」 | `COMPENSATING_BEHAVIOR` | 因既有方案不足而自製；若這是她原本就偏好的作法則不算 |
| 「醫院有給衛教單，但…不是講我家的時間表」 | `CURRENT_SOLUTION` + `ALTERNATIVE` | 現行方案存在但未解決該 job，構成 job 定義下的競爭 |
| 「最怕的是漏掉哪一次」 | `EMOTIONAL_DIMENSION` | 想避免的感受；若說「怕被鄰居說沒照顧好」則改 `SOCIAL_DIMENSION` |
| 「不好意思一直打去護理站問」 | `USE_OBSTACLE` | 發生在採用之後、影響持續使用；非 `ADOPTION_OBSTACLE` |

Do not code 「畫格子」 as `DESIRED_PROGRESS`. It is an activity. The progress must be inferred across
segments and checked against alternatives.

## 3. Timeline (the section 4.1 display)

| Stage | Evidence | Interpretation | Missing evidence |
|---|---|---|---|
| Baseline | 無用藥管理需求 | — | 入院前既有習慣未問到 |
| Trigger | 出院衛教當下資訊超載 | 問題進入主動處理 | 是否有他人在場未確認 |
| Active search | 翻衛教單、問親戚 | 搜尋範圍侷限於院方素材 | 未問是否搜尋過網路 |
| Decision | 自製冰箱時間表 | 選擇自製而非求助 | — |
| Little Hire | 每日打勾，持續 10 天 | 實際重複使用 | 無行為軌跡佐證，僅自述 |
| Aftermath | 未漏服，但持續焦慮 | 功能達成、情緒未解 | 回診紀錄未取得 |

The Little Hire row is the one that matters: an intervention could win the Big Hire (照顧者收下衛教單)
and still fail here.

## 4. Derive the job statement

Generate a narrower and a broader version, then choose (section 5.1):

- Too narrow: 「製作一張分時段的用藥打勾表」 → rejected, this is the solution she improvised.
- Too broad: 「照顧好我媽」 → rejected, every case fits; explains no alternative and no trade-off.
- **Selected**: 「當長輩出院返家、用藥與回診安排一次湧入時，我想要把這些安排轉換成我每天能確實執行
  的步驟，以免漏掉任何一次而傷害到她。」

Check it against the section 5.3 rejection list: no product named ✓; carries circumstance ✓; explains why
衛教單 lost and 自製表格 won ✓; explains the trade-off (自己做很累，但比一直打電話問來得不尷尬) ✓.

Status: `provisional` (one case). Analytic confidence: `low`. Both are required — they are different axes.

## 5. Convert to Ulwick grammar, if the study has an ODI phase

Job statement — `[verb] + [object] + [contextual clarifier]`:

> 「銜接出院後的用藥與回診安排」

Desired outcomes — `[direction] + [metric] + [object of control] + [clarifier]`:

| Draft | Verdict |
|---|---|
| 「讓出院衛教更容易理解」 | ✗ 形容詞未定義，且不可評分 |
| 「減少確認下一次服藥時間所需的時間」 | ✓ |
| 「降低漏服任一劑量的可能性」 | ✓ |
| 「減少確認用藥時間的時間並降低詢問護理站的尷尬」 | ✗ 一句兩個 outcome，必須拆開 |

## 6. Rate and score, with the scale declared

Scale: 受訪者以 1–5 評定重要度與滿意度；轉換規則為「評 4 或 5 的百分比 ÷ 10」，得 0–10 輸入。

| outcome | importance | satisfaction | opportunity |
|---|---:|---:|---:|
| 降低漏服任一劑量的可能性 | 8.6 | 3.1 | 14.1 |
| 減少確認下一次服藥時間所需的時間 | 7.2 | 4.8 | 9.6 |

Reproduce with:

```bash
python3 scripts/calculate_odi_scores.py outcomes.csv
```

Both inputs are 0–10, so the opportunity score runs 0–20 and the underserved threshold of 10 sits inside
that range. The first outcome clears it; the second does not. With one constructed case behind them these
numbers mean nothing — real scores need the sampling frame, n, response rate, and a sensitivity run.

## 7. Look for the negative case before believing any of it

Rival explanations to test, recorded in `rival_explanation`: 照顧者本身是行政職、習慣做表格（則自製行為
反映職業習慣而非方案不足）；或護理站電話等待過久（則問題是 access，不是 job）。

Negative case to hunt: 同樣情境但**未**自製任何工具、也未漏服的照顧者。If found, the candidate job is
either too narrow or the circumstance is doing less work than claimed.

## 8. The resulting evidence row

```csv
case_id,episode_id,stakeholder_role,evidence_type,evidence_excerpt,source_locator,circumstance,desired_progress,current_solution,candidate_job_statement,confidence,rival_explanation
C07,C07-E01,executor,direct account,"我後來自己拿一張紙畫格子貼在冰箱上，早中晚打勾",C07-T01:112-140,長輩出院返家當週用藥與回診安排一次湧入,把院方交代的安排轉成每天能確實執行的步驟,醫院衛教單與自製冰箱時間表,"當長輩出院返家、用藥與回診安排一次湧入時，我想要把這些安排轉換成我每天能確實執行的步驟，以免漏掉任何一次",low,照顧者職業習慣使然；或護理站電話等待過久屬 access 問題
```

Validate before drafting any narrative:

```bash
python3 scripts/validate_evidence_table.py case-evidence.csv
```
