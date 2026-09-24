# Campaign state

Budget: 20 rounds. Used: 1 (round 001 closed).
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

Capability probe (2026-09-24 UTC):

| Capability | Provider / path and version | Status |
|---|---|---|
| Python | `/Users/xiweipan/.local/bin/python3`, 3.12.14 | available |
| uv | `/Users/xiweipan/.local/bin/uv`, 0.12.17 | available |
| SMT | `/opt/homebrew/bin/z3`, 5.1.0; uv locked `z3-solver==5.1.0.0` | available |
| SAT | `/opt/homebrew/bin/kissat`, 4.0.4 | available |
| CP-SAT | no executable found | pending |
| Typst | `/opt/homebrew/bin/typst`, 0.15.1 | available |
| Lean / Lake | `/opt/homebrew/bin/lean`, 4.34.0; `/opt/homebrew/bin/lake`, 5.0.0 | available |
| Mathlib | no local installation found | pending; only formalization needs it |
| External writing skill | `sci-brain:how-to-technical-writing`, local 0.5.0 plugin | available |

Prepare complete: [contract](work/contract.md), [100-case corpus](work/cases.json), [checker](work/check.py), [evidence](work/preparation.md). Self-test passed on 2026-09-24 UTC.
Current claim: executable F/G and a general proof candidate in [work](work/proof.md); 100 prepared and 84 additional source instances pass closed-loop checks. Independent review and paper remain.
Next action: registered independent review of round 001, then manuscript if advanced.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Early/late two-task compiler classes with separator | Prepared 100-case closed loop | supported | [round](rounds/001/round.md) |
