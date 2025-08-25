import os
import random
import json

# Vastzetten van de seed zodat resultaten reproduceerbaar zijn
random.seed(12345)

# Output directories
evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

solutiondir = os.path.join("..", "solution")
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# Functie om JSON te schrijven
def write_json(data: dict):
    with open(os.path.join(evaldir, "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# Testcases configuratie
# Gebruik exact dezelfde parameters als in de oefening
testcases_params = [
    {"seed": 12345, "n_dice": 3, "n_turns": 2},
    {"seed": 67890, "n_dice": 5, "n_turns": 3},
    # Voeg hier andere testcases toe
]

exportdata = {"tabs": [{"name": "Feedback", "contexts": []}]}

for test in testcases_params:
    random.seed(test["seed"])
    context = {}

    # "before" code voor Dodona
    context["before"] = {"python": {"data": f"import random; random.seed({test['seed']})"}} 

    context["testcases"] = []
    
    # Output genereren
    output_lines = []
    for beurt in range(test["n_turns"]):
        dobbelstenen = [random.randint(1,6) for _ in range(test["n_dice"])]
        som = sum(dobbelstenen)
        evenoneven = "even" if som % 2 == 0 else "oneven"
        output_lines.append(f"Beurt {beurt+1}: {dobbelstenen} → Som = {som} ({evenoneven})")
    
    outputtxt = "\n".join(output_lines) + "\n"
    
    testcase = {
        "description": f"Uitvoeren met seed {test['seed']}, {test['n_dice']} dobbelstenen, {test['n_turns']} beurten",
        "input": {"stdin": {"type": "text", "data": f"{test['n_dice']} {test['n_turns']}" }},
        "output": {"stdout": {"type": "text", "data": outputtxt}}
    }
    
    context["testcases"].append(testcase)
    exportdata["tabs"][0]["contexts"].append(context)

write_json(exportdata)
