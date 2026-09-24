# Round 001 — early/late two-task compiler classes

## Plan

Gap: a subset must be selectable by schedule order even though compiler assignments are fixed. The upstream issue's two fixed compiler batches fail to encode a variable subset ([issue, lines 176–235](https://github.com/CodingThrust/problem-reductions/issues/474)); the cited Bruno–Downey paper's [abstract](https://epubs.siam.org/doi/pdf/10.1137/0207031) establishes the subject but does not expose the construction in the accessible page. Search on 2026-09-24 UTC found no relevant local or board experience entry.

Hypothesis: give each item a compiler with setup `a_i`, an early unit task and a late task of length `a_i`. A compulsory start marker removes the free initial setup, and a long separator must follow every early task. The first deadline bounds the weight of late tasks moved before the separator by `B=floor(sum(a)/2)`; the last deadline bounds the weight remaining after it by `B`. Equality would decode a partition. The crucial composition assumption is that the separator forces a fresh setup for every item processed after it, regardless of the order or extra compiler visits.

First discriminating check: implement F/G and run the prepared 100-instance closed loop; seek a counterexample with an item processed adjacent to the separator or an alternative batching order. Passing finite checks would support only the implementation and small cases, not the general proof.

## Evidence and diagnosis

`work/algorithm.py` and `work/proof.md` implement the planned mechanism. The first Z3-based bulk check became computationally impractical on a larger instance; interrupting Z3 yielded `unknown`, an execution failure with no mathematical conclusion. `work/preparation.md` records the exact oracle repair. The fixed source corpus and labels were not changed.

After switching the bulk target oracle to exact subset dynamic programming, the prepared loop passed 100 instances and 128 target outputs (28 YES, 72 NO, 28 alternate schedules). Independent `work/verify.py` passed all 84 source sequences of length 1–3 over 1–4 and 106 target outputs (22 YES, 62 NO, 22 alternate). Commands and limits are in `work/verification.md`. There is no observed counterexample. The proof's lower bounds explicitly cover all alternative batching orders and extra setups; the separator makes every post-separator late task reenter its compiler. This is a newly derived argument; the cited primary paper's abstract confirms the problem family, but its full construction was unavailable in this check. General correctness and novelty need independent review.

## Next action

Request registered independent review of correctness, novelty and significance; then write the manuscript if advanced.

**Experience extraction:** none. The separator argument is currently a candidate-specific proof, not a demonstrated reusable finding from a failure or independently reviewed lemma.
