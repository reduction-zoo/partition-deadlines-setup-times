"""Regenerate the fixed source corpus, using independent exhaustive labels."""
import json
from pathlib import Path
from check import random_source, source_witnesses, NO

EDGES = [
    [1], [2], [1, 1], [1, 2], [1, 2, 3], [2, 2, 2],
    [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 4],
    [3, 3, 3, 3], [1, 1, 1, 3], [1, 2, 2, 5], [1, 3, 3, 3],
]


def main():
    cases = []
    seen = set()

    def add(source, kind, seed=None):
        key = tuple(source["numbers"])
        if key in seen:
            return False
        seen.add(key)
        witnesses = source_witnesses(source)
        entry = {"source": source, "kind": kind, "expected": witnesses[0] if witnesses else NO}
        if seed is not None:
            entry["seed"] = seed
        cases.append(entry)
        return True

    for numbers in EDGES:
        assert add({"numbers": numbers}, "edge")
    seed = 0
    while sum(case["kind"] == "random" for case in cases) < 86:
        add(random_source(seed), "random", seed)
        seed += 1
    Path(__file__).with_name("cases.json").write_text(json.dumps(cases, indent=2) + "\n")


if __name__ == "__main__":
    main()
