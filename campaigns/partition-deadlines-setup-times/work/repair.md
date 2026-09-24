# Large-integer CLI repair

The initial independent review (commit `5ba7924`) reproduced a legal two-item, 4301-digit source instance for which F exited before producing a target. Python 3.12's default decimal integer conversion limit, rather than the reduction, caused the failure. The command `uv run python campaigns/partition-deadlines-setup-times/reviews/initial/check_large_integer.py` reported `exit=1` and the 4300-digit conversion error before repair.

`algorithm.py` now disables that process-local limit before reading or writing JSON. The same command reports `exit=0` and 43,303 output bytes. `verify.py` now includes both a YES pair of equal 4301-digit integers and a NO pair differing by one, and checks actual target solving and G extraction for them. Its run passed 86 instances and 109 target outputs. The unchanged prepared self-test and 100-instance/128-output candidate loop also passed. The mathematical construction and proof were not changed.
