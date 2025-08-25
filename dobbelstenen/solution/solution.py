import random

# Vraag input van de gebruiker
aantal_dobbelstenen = int(input("Hoeveel dobbelstenen wil je gooien? "))
aantal_beurten = int(input("Hoeveel beurten wil je doen? "))

# Buitenste lus: voor elke beurt
for beurt in range(1, aantal_beurten + 1):
    worpen = []
    # Binnenste lus: gooi elke dobbelsteen
    for i in range(aantal_dobbelstenen):
        worp = random.randint(1, 6)  # 1 t/m 6
        worpen.append(worp)
    
    # Bereken som
    som = sum(worpen)
    
    # Print de worpen en of de som even of oneven is
    if som % 2 == 0:
        print(f"Beurt {beurt}: {worpen} → Som = {som} (even)")
    else:
        print(f"Beurt {beurt}: {worpen} → Som = {som} (oneven)")
