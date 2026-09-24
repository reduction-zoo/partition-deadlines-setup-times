# Independent executable verification

Candidate: `work/algorithm.py`, round 001 (commit recorded in round record). Exact commands from repository root:

```sh
uv sync --locked
uv run python campaigns/partition-deadlines-setup-times/work/check.py --self-test
uv run python campaigns/partition-deadlines-setup-times/work/check.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py
uv run python campaigns/partition-deadlines-setup-times/work/verify.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py
```

The prepared closed loop passed 100 source instances and 128 target outputs: 28 feasible targets, 72 `NO-SOLUTION` targets, and 28 instances with a second valid schedule. `verify.py` imports neither the prepared checker nor the candidate. It enumerates source subsets and actual target schedules by recursive permutation search, then invokes F and G as fresh subprocesses. Its complete finite family comprises all 84 nonempty sequences of length at most three with entries in 1–4, plus one YES and one NO two-item instance with 4301-digit integers. It passed 86 target instances and 109 target outputs: 23 feasible, 63 `NO-SOLUTION`, and 23 with an alternate schedule. Both oracles check recovered outputs against the source definition. Their tested domain is small; the general claim rests on `proof.md` and independent review, not these counts. Runtime and encoding growth beyond eight source items have not been measured.

The focused large-integer review reproduction initially failed at `json.load` with Python's 4300-digit limit, then passed after `algorithm.py` disabled that limit for its CLI process (`exit=0`, 43,303 output bytes). The expanded independent verifier parses and solves the actual large target instances and invokes extraction on the resulting outputs. The 100-case prepared loop and its self-test were rerun unchanged after the repair and passed.
