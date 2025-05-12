getallen = []
for i in range(5):
    invoer = int(input(f"Geef getal {i+1}: "))
    getallen.append(invoer)

som_even = 0

for getal in getallen:
    if getal % 2 == 0:
        som_even += getal

print(f"De som van de even getallen is: {som_even}")