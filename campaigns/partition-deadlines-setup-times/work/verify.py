"""Second implementation: brute-force injected source and target instances."""
import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

NO = "NO-SOLUTION"


def call(path, payload, extract=False):
    command = [sys.executable, str(path)] + (["--extract"] if extract else [])
    return json.loads(subprocess.run(command, input=json.dumps(payload), text=True, capture_output=True, check=True).stdout)


def source_truth(numbers):
    total = sum(numbers)
    return any(2 * sum(numbers[i] for i in subset) == total
               for r in range(len(numbers) + 1)
               for subset in itertools.combinations(range(len(numbers)), r))


def source_valid(numbers, output, possible):
    if output == NO:
        return not possible
    return (type(output) is list and all(type(i) is int and 0 <= i < len(numbers) for i in output)
            and len(set(output)) == len(output)
            and 2 * sum(numbers[i] for i in output) == sum(numbers))


def schedules(target, limit=2):
    jobs, setup = target["tasks"], target["setups"]
    found = []

    def search(path, time, previous):
        if len(found) == limit:
            return
        if len(path) == len(jobs):
            found.append(list(path))
            return
        for i, job in enumerate(jobs):
            if i in path:
                continue
            changed = previous is not None and previous != job["compiler"]
            end = time + job["p"] + (setup[job["compiler"]] if changed else 0)
            if end <= job["d"]:
                search(path + [i], end, job["compiler"])

    search([], 0, None)
    return found


def main(path):
    inputs = [(a,) for a in range(1, 5)]
    inputs += list(itertools.product(range(1, 5), repeat=2))
    inputs += list(itertools.product(range(1, 5), repeat=3))
    counts = {"instances": 0, "outputs": 0, "yes": 0, "no": 0, "alternate": 0}
    for numbers in inputs:
        source = {"numbers": list(numbers)}
        feasible = source_truth(numbers)
        target = call(path, source)
        answers = schedules(target)
        assert bool(answers) == feasible, (source, target, answers)
        for answer in answers or [NO]:
            recovered = call(path, {"source": source, "target_solution": answer}, True)
            assert source_valid(numbers, recovered, feasible), (source, answer, recovered)
            counts["outputs"] += 1
        counts["instances"] += 1
        counts["yes" if answers else "no"] += 1
        counts["alternate"] += len(answers) > 1
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    main(parser.parse_args().candidate)
