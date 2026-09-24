# A two-deadline separator reduction

## Rule

Let the Partition input be positive integers `a_0,...,a_{n-1}`, with `n≥1`, total `A`, and `B=⌊A/2⌋`. Set `T=1+n+A+B` and `D=T+1+n+2A+B`. Make a marker compiler of setup zero and one compiler `i` of setup `a_i` for each item. The tasks, in the index order used by `algorithm.py`, are:

| Task | Processing time | Deadline | Compiler |
|---|---:|---:|---|
| start `M` | 1 | 1 | marker |
| early `E_i` | 1 | `T` | `i` |
| late `L_i` | `a_i` | `D` | `i` |
| separator `H` | `T` | `2T` | marker |

All values are positive where required; all setups are nonnegative. The first task pays no setup, and every later change charges the *new* compiler's setup. The index of `L_i` is `2+2i`; the index of `H` is `2n+1`.

For target `NO-SOLUTION`, `G` returns source `NO-SOLUTION`. For any valid schedule, `G` returns the indices `i` for which `L_i` precedes `H`.

## Correctness for every valid output

Any feasible schedule begins with `M`: a positive-length task before it would make its completion exceed deadline 1. No `E_i` can follow `H`: since `M` is first and `H` itself takes `T` time, such an `E_i` would finish after `T`. Thus all early tasks precede `H`. Let `P` be the indices with `L_i` before `H` and write `w(P)=Σ_{i∈P}a_i`.

The start time of `H` is at most `T`, by its deadline `2T` and length `T`. Before `H`, processing takes at least `1+n+w(P)` and entering each item compiler at least once costs `A` in setups (the first task was the marker). Hence `1+n+A+w(P)≤T`, or `w(P)≤B`.

All processing in the schedule totals `1+n+A+T`. Setup time is at least `A` for entering each item compiler before `H`, plus `A-w(P)` for entering again after `H` each compiler whose late task is there. This second charge is unavoidable because `H` has the marker compiler, regardless of other batching or task order. The final completion is at least `T+1+n+2A+(A-w(P))`. Every task has deadline at most `D`, so that completion is at most `D=T+1+n+2A+B`. Thus `A-w(P)≤B`. Together with `w(P)≤B`, this is impossible when `A` is odd and forces `A=2B` and `w(P)=B` when a feasible schedule exists. Every feasible schedule therefore decodes a source witness, including those with extra setups or reordered batches.

Conversely, suppose `P` is a partition witness, so `A=2B` and `w(P)=B`. Schedule `M`; then, in arbitrary item order, schedule `E_i,L_i` consecutively for `i∈P` and `E_i` alone for `i∉P`; then `H`; then the remaining `L_i` in arbitrary order. The first setup for each item contributes `A`. The work before `H` is exactly `1+n+A+B=T`; every `E_i` meets deadline `T`. The separator finishes at `2T`. Each late item incurs one fresh setup; its remaining processing and setup total `2(A-B)=2B=A`. Consequently the schedule finishes at `2T+A=D`, and all late tasks meet `D`. This establishes target feasibility exactly when Partition is feasible. Therefore target `NO-SOLUTION` decodes correctly as well.

## Complexity and scope

`F` computes `A,B,T,D`, creates `2n+2` tasks and `n+1` compilers, and writes integers bounded by `O(n+A)`. Since the input includes binary-encoded positive `a_i`, these numbers have `O(log n+log A)` bits, and the complete output has `O(n(log n+log A))` bits. Arithmetic and serialization are polynomial in input length. `G` locates the separator and scans the schedule, using `O(n+|y|)` index operations and polynomial bit time. It reconstructs all metadata from the source input; no earlier process state is used. The rule uses no solver or randomness. The construction is derived here; it does not claim novelty against the inaccessible body of Bruno and Downey's 1978 [paper](https://doi.org/10.1137/0207031).
