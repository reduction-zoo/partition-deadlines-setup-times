# Campaign state

Status: **ready_for_expert_review** (agent assessment, not human certification).
Budget: 20 rounds. Used: 1. Remaining: 19. Distinct construction mechanisms: 1.
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

## Result and evidence

The separator rule supplies executable [F and G](work/algorithm.py), a [general proof](work/proof.md), and a four-page [Typst manuscript](work/manuscript.pdf). It maps Partition to the fixed sequencing problem and recovers a source witness from every feasible schedule, with the no-solution case covered. The hardness direction is known; novelty of this particular gadget relative to Bruno and Downey's inaccessible full proof is unresolved. The contribution is a complete reproducible rule, not a new classification.

[Prepare](work/preparation.md) fixed 100 distinct source cases before construction: 86 seeded random and 14 edge cases. Its self-test and closed loop passed, with 128 target outputs (28 feasible, 72 `NO-SOLUTION`, and 28 alternate schedules). [Additional verification](work/verification.md) passed 86 source instances and 109 target outputs, including large-integer YES/NO cases. The initial [independent review](reviews/initial/review.md) found a legal-input CLI defect; [repair evidence](work/repair.md) and [focused re-review](reviews/recheck/review.md) record its resolution and an advance decision. Finite checks support implementation behavior; the proof carries the universal claim. Review isolation relied on instructions, without an enforced write sandbox or tool denial.

The manuscript was compiled with Typst 0.15.1 using `typst compile manuscript.typ manuscript.pdf` in `work/`, then all four rendered pages were visually inspected after the final editorial edit. The title, theorem, equations, tables, citations and reproduction appendix rendered legibly without clipping. No formal verification was requested. Target-solver scale beyond eight source items was not measured. No remote, publication or board change was made.

Experience extraction: 0 entries created, 0 updated, 0 pending. Round 001 found no qualifying generalizable failure record beyond its candidate-specific proof and oracle execution repair. Next action: human expert review of the proof and literature relationship; publication requires separate approval.

## Capability probe (2026-09-24 UTC)

| Capability | Provider / path and version | Status |
|---|---|---|
| Python | `/Users/xiweipan/.local/bin/python3`, 3.12.14 | available |
| uv | `/Users/xiweipan/.local/bin/uv`, 0.12.17 | available |
| SMT | `/opt/homebrew/bin/z3`, 5.1.0; uv locked `z3-solver==5.1.0.0` | available |
| SAT | `/opt/homebrew/bin/kissat`, 4.0.4 | available |
| CP-SAT | no executable found | pending; unused |
| Typst | `/opt/homebrew/bin/typst`, 0.15.1 | available |
| Lean / Lake | `/opt/homebrew/bin/lean`, 4.34.0; `/opt/homebrew/bin/lake`, 5.0.0 | available |
| Mathlib | no local installation found | pending; only formalization needs it |
| External writing skill | `sci-brain:how-to-technical-writing`, local 0.5.0 plugin | available |

## Round table

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Early/late two-task compiler classes with separator | Prepared 100-case closed loop | supported | [round](rounds/001/round.md) |
