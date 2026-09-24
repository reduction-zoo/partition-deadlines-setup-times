"""Partition to deadline/setup scheduling, with witness recovery."""
import json
import sys

NO = "NO-SOLUTION"


def forward(source):
    numbers = source["numbers"]
    if not numbers or any(type(a) is not int or a <= 0 for a in numbers):
        raise ValueError("numbers must be a nonempty list of positive integers")
    n, total = len(numbers), sum(numbers)
    half = total // 2
    early_deadline = 1 + n + total + half
    last_deadline = early_deadline + 1 + n + 2 * total + half
    tasks = [{"p": 1, "d": 1, "compiler": "marker"}]
    setups = {"marker": 0}
    for i, a in enumerate(numbers):
        compiler = f"item_{i}"
        setups[compiler] = a
        tasks.extend([{"p": 1, "d": early_deadline, "compiler": compiler},
                      {"p": a, "d": last_deadline, "compiler": compiler}])
    tasks.append({"p": early_deadline, "d": 2 * early_deadline, "compiler": "marker"})
    return {"tasks": tasks, "setups": setups}


def extract(source, answer):
    if answer == NO:
        return NO
    separator = 2 * len(source["numbers"]) + 1
    before = set(answer[:answer.index(separator)])
    return [i for i in range(len(source["numbers"])) if 2 + 2 * i in before]


if __name__ == "__main__":
    try:
        request = json.load(sys.stdin)
        result = extract(request["source"], request["target_solution"]) if sys.argv[1:] == ["--extract"] else forward(request)
        json.dump(result, sys.stdout)
        sys.stdout.write("\n")
    except (KeyError, ValueError, TypeError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
