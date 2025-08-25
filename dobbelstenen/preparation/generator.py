import random
import json

# testcases die we willen genereren: (seed, aantal_dobbelstenen, aantal_beurten)
cases = [
    (12345, 3, 2),
    (54321, 2, 3),
    (11111, 1, 5),
    (22222, 4, 2),
    (33333, 5, 1)
]

exportdata = {"tabs": [{"name": "Feedback", "contexts": []}]}

for seed, n_dobbelstenen, n_beurten in cases:
    random.seed(seed)
    stdout_lines = []
    for beurt in range(1, n_beurten + 1):
        worpen = [random.randint(1,6) for _ in range(n_dobbelstenen)]
        som = sum(worpen)
        pariteit = "even" if som % 2 == 0 else "oneven"
        stdout_lines.append(f"Beurt {beurt}: {worpen} → Som = {som} ({pariteit})")
    outputtxt = "\n".join(stdout_lines) + "\n"
    
    context = {
        "before": {"python": {"data": f"import random; random.seed({seed})"}},
        "testcases": [
            {
                "description": f"Uitvoeren met seed {seed}, {n_dobbelstenen} dobbelstenen, {n_beurten} beurten:",
                "input": {
                    "stdin": {"type": "text", "data": f"{n_dobbelstenen}\n{n_beurten}\n"}
                },
                "output": {"stdout": {"type": "text", "data": outputtxt}}
            }
        ]
    }
    exportdata["tabs"][0]["contexts"].append(context)

with open("tests.json", "w", encoding="utf-8") as f:
    json.dump(exportdata, f, indent=2)
