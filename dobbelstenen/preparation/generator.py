import os
import json
import random

# Waar tests.json weggeschreven wordt
EVAL_DIR = os.path.join("..", "evaluation")
os.makedirs(EVAL_DIR, exist_ok=True)

def write_json(data: dict):
    with open(os.path.join(EVAL_DIR, "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# Kies hier je testcases (seed, aantal_dobbelstenen, aantal_beurten)
TESTS = [
    (12345, 3, 2),
    (54321, 2, 3),
    (11111, 1, 5),
    (22222, 4, 2),
    (33333, 5, 1),
    (13579, 3, 3),
    (24680, 6, 2),
    (42424, 2, 4),
    (98765, 5, 2),
    (10101, 4, 3),
]

export = {"tabs": [{"name": "Feedback", "contexts": []}]}

for seed, n_dice, n_turns in TESTS:
    # Context: zet de seed vóór de studenten-code draait
    context = {
        "before": {"python": {"data": f"import random; random.seed({seed})"}},
        "testcases": []
    }

    # Bepaal verwachte stdout met dezelfde seed en regels als de oefening
    random.seed(seed)
    lines = []
    for turn in range(1, n_turns + 1):
        rolls = [random.randint(1, 6) for _ in range(n_dice)]
        s = sum(rolls)
        parity = "even" if s % 2 == 0 else "oneven"
        lines.append(f"Beurt {turn}: {rolls} → Som = {s} ({parity})")
    expected_stdout = "\n".join(lines) + "\n"

    testcase = {
        "description": f"Uitvoeren met seed {seed}, {n_dice} dobbelstenen, {n_turns} beurten:",
        "input": {
            # BELANGRIJK: newline-gescheiden inputs (zoals twee keer input())
            "stdin": {"type": "text", "data": f"{n_dice}\n{n_turns}\n"}
        },
        "output": {
            "stdout": {"type": "text", "data": expected_stdout}
        }
    }

    context["testcases"].append(testcase)
    export["tabs"][0]["contexts"].append(context)

write_json(export)
