# Partition → Sequencing with deadlines and setup times

**Status:** `ready_for_expert_review` · **Research model:** `gpt-6-sol` · **Submitted:** 2026-09-24

For every nonempty sequence of positive Partition weights, this repository gives deterministic polynomial-time maps from the source search problem to single-machine sequencing with compiler setup times and deadlines. Every feasible target schedule decodes to an equal-sum subset; target `NO-SOLUTION` decodes to source `NO-SOLUTION`. The hardness direction is known. This archive supplies a complete construction and recovery rule for the fixed [question](campaigns/partition-deadlines-setup-times/question.md), without claiming that its particular gadget is new.

## Construction

Each weight defines a compiler with that setup time, an early unit task, and a late task whose processing time equals the weight. A mandatory start marker removes the free initial setup. A long separator forces every early task before it and charges each late task placed after it for another compiler entry. The early and final deadlines bound the weights on both sides by half the total. Thus any feasible schedule yields an exact partition, regardless of extra switches or batching order.

## Evidence

- **Correctness and recovery:** The [general proof](campaigns/partition-deadlines-setup-times/work/proof.md) handles every legal source input, every feasible schedule and `NO-SOLUTION`. A fresh-context [independent reviewer](campaigns/partition-deadlines-setup-times/reviews/recheck/review.md) advanced the repaired candidate for expert review. Human expert acceptance and novelty of this gadget relative to the 1978 primary proof remain open.
- **Complexity:** The construction has `2n+2` tasks and `n+1` compilers; the [proof](campaigns/partition-deadlines-setup-times/work/proof.md) bounds both maps' runtime and output encoding size polynomially in the binary input length. These bounds are written, not formally certified.
- **Executable checks:** The fixed [Prepare corpus](campaigns/partition-deadlines-setup-times/work/preparation.md) has 100 cases and produced 128 checked target outputs. A separate [verifier](campaigns/partition-deadlines-setup-times/work/verification.md) checked 86 input instances and 109 target outputs, including large-integer YES and NO cases. These finite checks support the implementation; they do not establish the universal theorem.
- **Pending:** No Lean formalization or human maintainer verification is recorded. The board should mark this rule `submitted`, not `verified`. See the [campaign state](campaigns/partition-deadlines-setup-times/state.md).

## Reproduce

Run from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/partition-deadlines-setup-times/work/check.py --self-test
uv run --locked python campaigns/partition-deadlines-setup-times/work/check.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py
uv run --locked python campaigns/partition-deadlines-setup-times/work/verify.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py
```

The first check validates the prepared source corpus and test oracles. The next two run the construction and recovery as fresh subprocesses against independently solved target instances. Their finite domains are recorded in the linked evidence; the general claim rests on the written proof.

## Artifacts

- [Fixed question](campaigns/partition-deadlines-setup-times/question.md)
- [Campaign state](campaigns/partition-deadlines-setup-times/state.md)
- [Typst manuscript and inspected PDF](campaigns/partition-deadlines-setup-times/work/manuscript.pdf)
- [Construction and recovery](campaigns/partition-deadlines-setup-times/work/algorithm.py)
- [General proof](campaigns/partition-deadlines-setup-times/work/proof.md)
- [Initial review](campaigns/partition-deadlines-setup-times/reviews/initial/review.md) and [focused re-review](campaigns/partition-deadlines-setup-times/reviews/recheck/review.md)
- [Verification evidence](campaigns/partition-deadlines-setup-times/work/verification.md)

The model identifier was checked against the original Codex session metadata; the current default was not used as a proxy. Board source commit: `d56f22aee71c281b1a9b7aa90e65a0d2607efdce`.
