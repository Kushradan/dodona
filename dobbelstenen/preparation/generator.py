import os
import math
import random
import json

# fixed seed for reproducible test generation
random.seed(123456789)

evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

solutiondir = os.path.join("..", "solution")
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

def write_json(data: dict):
    with open(os.path.join("..", "evaluation", "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# Generate seed & n pairs
cases = []
for i in range(3, 15):
    exp = math.ceil(i / 2)
    seed = random.randint(1, 100000)
    n = 10 ** exp
    cases.append((seed, n))

exportdata = {"tabs": [{"name": "Feedback", "contexts": []}]}

for seed, n in cases:
    # prepare context dictionary directly
    context = {
        "before": {"python": {"data": f"import random; random.seed({seed})"}} ,
        "testcases": []
    }

    # calculate expected output
    random.seed(seed)
    aantal = 0
    for _ in range(n):
        dice = [random.randint(1,6) for _ in range(5)]
        m, M = min(dice), max(dice)
        if (m == 1 and M == 5) or (m == 2 and M == 6):
            if len(set(dice)) == 5:  # geen dubbele
                aantal += 1

    kans = round(aantal / n * 100, 2)
    outputtxt = f"De kans op grote straat is ongeveer {kans} %\n"

    # create testcase
    testcase = {
        "description": f"Uitvoeren met seed {seed} en invoer {n} leidt tot:",
        "input": {"stdin": {"type": "text", "data": str(n)}},
        "output": {"stdout": {"type": "text", "data": outputtxt}}
    }

    context["te]()
