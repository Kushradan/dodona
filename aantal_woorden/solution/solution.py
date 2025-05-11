zin = input("Geef een zin: ")

aantal_spaties = 0

for teken in zin:
    if teken == " ":
        aantal_spaties += 1

aantal_woorden = aantal_spaties + 1
print("Aantal woorden:", aantal_woorden)