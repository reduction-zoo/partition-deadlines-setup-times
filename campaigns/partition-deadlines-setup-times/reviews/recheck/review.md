# Independent recheck of candidate b18ecdd

Reviewed 2026-09-24 UTC. Decision: **advance for expert review**. The repair resolves the sole correctness defect in `reviews/initial/review.md`; the mathematical construction, proof, and previously reviewed literature position are unchanged. Advance is not publication acceptance.

## Correctness

`work/algorithm.py:36` now calls `sys.set_int_max_str_digits(0)` before `json.load` and `json.dump` in the CLI process. This removes Python 3.12's process-local 4300-decimal-digit conversion cap for both F and `--extract` G without narrowing the legal source domain or changing either map's formula. Arbitrary finite JSON integers remain subject to ordinary finite memory and time, as required by the polynomial-time model; the conversion has polynomial bit cost. No scheduling premise changes, so the initial review's audit of `work/proof.md:20-30` applies: the pre-separator and final-completion bounds force an exact partition for every feasible schedule, and the constructed schedule proves the converse and the `NO-SOLUTION` case.

I reran the original independent reproduction, `uv run python campaigns/partition-deadlines-setup-times/reviews/initial/check_large_integer.py`: it now reports `exit=0` and `output_bytes=43303` for equal 4301-digit weights. I also ran the changed full injected-instance verifier, `uv run python campaigns/partition-deadlines-setup-times/work/verify.py --candidate campaigns/partition-deadlines-setup-times/work/algorithm.py`: `{"alternate":23,"instances":86,"no":63,"outputs":109,"yes":23}`. Its new cases at `work/verify.py:58-69` are independently labeled by subset enumeration, solve the actual target schedules, and invoke the CLI recovery for a large YES pair and a large odd-total NO pair. It includes alternate valid schedules for the YES pair. `work/verification.md` accurately reports these counts. The unchanged prepared 100-case loop remains prior evidence; I did not rerun it.

The digit-limit repair addresses the failure in the initial review at the correct shared CLI entry point. I found no new output-legality, no-solution, determinism, or encoding-size gap from this change.

## Novelty

The assessment in `reviews/initial/review.md` remains applicable. Garey and Johnson, [Appendix A5.1, SS6, p. 238](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf), attributes a PARTITION transformation for this scheduling problem to [Bruno and Downey (1978)](https://epubs.siam.org/doi/10.1137/0207031). The hardness direction is known. The original paper's full proof was inaccessible in the 2026-09-24 search, so equivalence or novelty of this particular separator gadget remains unresolved and is not claimed. The fixed task explicitly accepts a complete reconstruction of a published construction. No new literature claim arose from the repair.

## Significance

The contribution remains a complete, reproducible instance map, schedule decoder, and proof that handles arbitrary batching orders, filling the fixed rule-completion request. The repair restores the promised arbitrary finite integer domain. Overhead remains `2n+2` tasks, `n+1` compilers, and polynomial encoding size and F/G bit time. The independent target solver is exponential in worst case, and no practical scaling claim is supported. There is no fixed resource threshold to meet before expert review.

## Isolation and model route

This follow-up used the registered reviewer role and inherited the parent's GPT-6 route without a model override; the exact model identifier was unavailable in this reviewer context. No tool denial or enforced depth cap was visible. Filesystem sandbox mode was `danger-full-access`, approval policy `never`, and the write and no-spawn boundaries were instructions only. I wrote only this file in `reviews/recheck/`; I did not edit candidate artifacts, tests, or earlier evidence. These isolation mechanisms are distinct from evidence for the judgments above.
