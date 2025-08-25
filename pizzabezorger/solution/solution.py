# Afstanden en snelheden vragen
afstand_mario = float(input("Geef de afstand voor Mario in km: "))
snelheid_mario = float(input("Geef de gemiddelde snelheid van Mario in km/u: "))

afstand_luigi = float(input("Geef de afstand voor Luigi in km: "))
snelheid_luigi = float(input("Geef de gemiddelde snelheid van Luigi in km/u: "))

# Tijd berekenen in minuten
tijd_mario = (afstand_mario / snelheid_mario) * 60
tijd_luigi = (afstand_luigi / snelheid_luigi) * 60

# Afronden op 1 decimaal
tijd_mario = round(tijd_mario, 1)
tijd_luigi = round(tijd_luigi, 1)

# Vergelijken wie sneller is
if tijd_mario < tijd_luigi:
    print("Mario is de snelste bezorger. Hij doet er", tijd_mario, "minuten over.")
elif tijd_luigi < tijd_mario:
    print("Luigi is de snelste bezorger. Hij doet er", tijd_luigi, "minuten over.")
else:
    print("Beide koeriers zijn even snel. Ze doen er", tijd_mario, "minuten over.")
