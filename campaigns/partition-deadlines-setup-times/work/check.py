"""Independent small-instance oracles and injected F/G checks."""
import argparse
import json
import itertools
import random
import subprocess
import sys
from pathlib import Path

import z3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NO = "NO-SOLUTION"


def random_source(seed):
    rng = random.Random(seed)
    n = 1 + seed % 8
    return {"numbers": [rng.randint(1, 18) for _ in range(n)]}


def source_witnesses(source, limit=2):
    a = source["numbers"]
    if not a or any(type(v) is not int or v <= 0 for v in a):
        raise ValueError("invalid source")
    total = sum(a)
    if total % 2:
        return []
    out = []
    for mask in range(1 << len(a)):
        if sum(v for i, v in enumerate(a) if mask >> i & 1) * 2 == total:
            out.append([i for i in range(len(a)) if mask >> i & 1])
            if len(out) == limit:
                break
    return out


def valid_source(source, answer, feasible):
    if answer == NO:
        return not feasible
    a = source["numbers"]
    return (isinstance(answer, list) and all(type(i) is int and 0 <= i < len(a) for i in answer)
            and len(set(answer)) == len(answer) and 2 * sum(a[i] for i in answer) == sum(a))


def validate_target(target):
    tasks, setups = target["tasks"], target["setups"]
    if not isinstance(tasks, list) or not tasks or not isinstance(setups, dict):
        raise ValueError("invalid target shape")
    if any(type(v) is not int or v < 0 for v in setups.values()):
        raise ValueError("invalid setup")
    for task in tasks:
        if (type(task["p"]) is not int or task["p"] <= 0 or
                type(task["d"]) is not int or task["d"] <= 0 or
                task["compiler"] not in setups):
            raise ValueError("invalid task")


def valid_schedule(target, order):
    tasks, setups = target["tasks"], target["setups"]
    n = len(tasks)
    if not isinstance(order, list) or len(order) != n or any(type(i) is not int or i < 0 or i >= n for i in order) or len(set(order)) != n:
        return False
    clock = 0
    previous = None
    for i in order:
        task = tasks[i]
        compiler = task["compiler"]
        if previous is not None and compiler != previous:
            clock += setups[compiler]
        clock += task["p"]
        if clock > task["d"]:
            return False
        previous = compiler
    return True


def target_witnesses(target, limit=2):
    validate_target(target)
    tasks, setups = target["tasks"], target["setups"]
    n = len(tasks)
    at = [z3.Int(f"at_{i}") for i in range(n)]
    solver = z3.Solver()
    solver.add(z3.Distinct(at), *(z3.And(v >= 0, v < n) for v in at))

    def field(position, key):
        return z3.Sum(*(z3.If(at[position] == i, task[key], 0) for i, task in enumerate(tasks)))

    def compiler(position, name):
        return z3.Or(*(at[position] == i for i, task in enumerate(tasks) if task["compiler"] == name))

    clock = z3.IntVal(0)
    for pos in range(n):
        if pos:
            setup = z3.Sum(*(z3.If(z3.And(compiler(pos, name), z3.Not(compiler(pos - 1, name))), value, 0)
                             for name, value in setups.items()))
            clock += setup
        clock += field(pos, "p")
        solver.add(clock <= field(pos, "d"))
    answers = []
    for _ in range(limit):
        status = solver.check()
        if status == z3.unsat:
            break
        if status != z3.sat:
            raise RuntimeError(f"inconclusive target solver: {status}")
        model = solver.model()
        order = [model.eval(v).as_long() for v in at]
        if not valid_schedule(target, order):
            raise AssertionError("solver produced invalid schedule")
        answers.append(order)
        solver.add(z3.Or(*(at[pos] != order[pos] for pos in range(n))))
    return answers


def run_candidate(path, payload, extract=False):
    command = [sys.executable, str(path)] + (["--extract"] if extract else [])
    completed = subprocess.run(command, input=json.dumps(payload), text=True, capture_output=True, check=True)
    return json.loads(completed.stdout)


def self_test():
    subprocess.run([sys.executable, str(ROOT / "research/validate_preparation.py"), str(HERE / "cases.json")], check=True)
    cases = json.loads((HERE / "cases.json").read_text())
    yes = no = multiple = 0
    for case in cases:
        source = case["source"]
        if case["kind"] == "random":
            assert source == random_source(case["seed"])
        witnesses = source_witnesses(source)
        expected = witnesses[0] if witnesses else NO
        assert case["expected"] == expected
        assert valid_source(source, expected, bool(witnesses))
        assert not valid_source(source, NO if witnesses else [], bool(witnesses))
        yes += bool(witnesses)
        no += not witnesses
        multiple += len(witnesses) > 1
    # Hand-checkable truth and deliberately wrong source outputs.
    assert source_witnesses({"numbers": [1, 1]}) == [[0], [1]]
    assert source_witnesses({"numbers": [1, 2, 4]}) == []
    assert not valid_source({"numbers": [1, 1]}, [0, 0], True)
    assert not valid_source({"numbers": [1, 2, 4]}, [0], False)
    # Hand-checkable target schedules: setup is charged on entry, never initially.
    target = {"tasks": [{"p": 2, "d": 2, "compiler": "a"}, {"p": 1, "d": 5, "compiler": "b"}], "setups": {"a": 4, "b": 2}}
    assert target_witnesses(target) == [[0, 1]]
    assert not valid_schedule(target, [1, 0])
    assert not target_witnesses({"tasks": [{"p": 2, "d": 1, "compiler": "a"}], "setups": {"a": 0}})
    assert not valid_schedule(target, [[0], 1])
    assert not valid_schedule(target, [0, 0])
    rng = random.Random(7331)
    for _ in range(30):
        small = {"tasks": [{"p": rng.randint(1, 3), "d": rng.randint(1, 12), "compiler": rng.choice(["a", "b"])} for _ in range(4)],
                 "setups": {"a": rng.randint(0, 3), "b": rng.randint(0, 3)}}
        exhaustive = any(valid_schedule(small, list(order)) for order in itertools.permutations(range(4)))
        assert bool(target_witnesses(small, 1)) == exhaustive
    print(f"self-test passed: {len(cases)} cases; YES={yes}, NO={no}, multiple={multiple}")


def candidate_test(path):
    cases = json.loads((HERE / "cases.json").read_text())
    instances = outputs = yes = no = alternate = 0
    for case in cases:
        source = case["source"]
        target = run_candidate(path, source)
        target_answers = target_witnesses(target)
        answers = target_answers or [NO]
        for answer in answers:
            result = run_candidate(path, {"source": source, "target_solution": answer}, True)
            if not valid_source(source, result, case["expected"] != NO):
                raise AssertionError(f"recovery mismatch: {source=}, {answer=}, {result=}")
            outputs += 1
        instances += 1
        yes += bool(target_answers)
        no += not target_answers
        alternate += len(target_answers) > 1
    print(f"candidate passed: {instances} instances, {outputs} outputs; target YES={yes}, NO={no}, alternate={alternate}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--self-test", action="store_true")
    choice.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    self_test() if args.self_test else candidate_test(args.candidate)
