def tel_klinkers(zin):
    aantal = 0
    for letter in zin:
        if letter.lower() in "aeiou":
            aantal += 1
    return aantal
