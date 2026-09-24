# Fixed question

```json
{
  "source": "Partition",
  "target": "Sequencing with deadlines and setup times",
  "category": "Construction open",
  "summary": "The construction isolates how switching overhead and deadlines make scheduling difficult, beyond ordinary single-machine sequencing.",
  "source_definition": "Given positive binary-encoded integers, return a subcollection with sum equal to half the total. Return NO-SOLUTION exactly when no such witness exists. Graphs, families and strings are explicit; numerical parameters use binary encodings.",
  "target_definition": "Tasks have positive processing times, deadlines and assigned compilers; each compiler has a nonnegative setup time. Return a nonpreemptive single-machine schedule meeting all deadlines, adding the new compiler's setup time whenever consecutive tasks use different compilers. There is no initial setup charge in this formulation. A valid output is a witness satisfying these conditions, or NO-SOLUTION exactly when none exists.",
  "required_result": "Construct deterministic polynomial-time maps F and G. F must produce a legal target instance, and G(x,y) must return a valid source output for every valid target output y, including NO-SOLUTION. A complete rule may reconstruct a published construction or give a new one; it must specify every gadget, numerical parameter and decoding step.",
  "acceptance": "Deliver executable instance construction and output recovery, a general proof covering all legal inputs and target outputs, and worst-case polynomial time and encoding-size bounds. Cite the actual proof used, or identify a newly derived argument. Check small positive and negative instances with independent solvers; finite tests alone do not establish correctness.",
  "importance": "The construction isolates how switching overhead and deadlines make scheduling difficult, beyond ordinary single-machine sequencing.",
  "difficulty": "Difficulty is not yet established by a construction attempt. Specify every task and deadline so that unequal partitions cannot exploit a different batching order. Initial and inter-batch setup conventions must be explicit.",
  "openness": "This is a rule-completion task from the imported catalog. The requested contribution is a complete, reproducible construction, proof and implementation; the existing hardness attribution is not presented as an unsolved complexity classification. The references are leads to check, not a verified solution.",
  "literature_checked": "2026-09-18",
  "coverage": "Import inventory review of the cited sources. Primary proofs have not been independently re-audited; availability of a complete reconstruction elsewhere remains unassessed.",
  "references": [
    {
      "title": "Problem-Reductions: Partition \u2192 Sequencing with deadlines and setup times",
      "url": "https://github.com/CodingThrust/problem-reductions/issues/474",
      "note": "Upstream task and discussion checked on 2026-09-18. Reported reference: Garey & Johnson, *Computers and Intractability*, Appendix A5.1, p.238"
    }
  ],
  "solutions": [],
  "equation": ""
}
```
