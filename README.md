# Partition → Sequencing with deadlines and setup times

A complete deterministic instance map and schedule-to-partition decoder for the [fixed question](campaigns/partition-deadlines-setup-times/question.md). The [proof](campaigns/partition-deadlines-setup-times/work/proof.md), [algorithm](campaigns/partition-deadlines-setup-times/work/algorithm.py), and [four-page paper](campaigns/partition-deadlines-setup-times/work/manuscript.pdf) are ready for human expert review. The known hardness direction is reconstructed here; novelty of the particular gadget remains unresolved.

[State and evidence](campaigns/partition-deadlines-setup-times/state.md) · [Independent re-review](campaigns/partition-deadlines-setup-times/reviews/recheck/review.md)

From this repository root:

```sh
uv sync --locked
uv run python campaigns/partition-deadlines-setup-times/work/check.py --self-test
uv run python campaigns/partition-deadlines-setup-times/work/check.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py
uv run python campaigns/partition-deadlines-setup-times/work/verify.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py
```

The fixed corpus contains 100 source cases; an independent verifier checks 86 more, including large integers. The target oracles and finite checks do not substitute for the general proof. Board source commit: d56f22aee71c281b1a9b7aa90e65a0d2607efdce. No remote or publication has been created.
