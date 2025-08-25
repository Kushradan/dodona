# Vraag de gebruiker hoe vaak de bel moet gaan
aantal = int(input("Hoe vaak moet de bel gaan? "))

# Gebruik een for-lus
for i in range(1, aantal + 1):
    # Elke 3e keer DONG, anders DING
    if i % 3 == 0:
        print("DONG")
    else:
        print("DING")
