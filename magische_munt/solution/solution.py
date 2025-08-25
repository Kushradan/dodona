import math

doel = float(input("Hoeveel munten wil je bereiken? "))
doel = math.ceil(doel)  # werk met een geheel doel (naar boven afronden)

munten = 1
dag = 0

print(f"Dag {dag}: je hebt {munten} munt(en).")

# Blijf verdubbelen tot het doel bereikt/overschreden is
while munten < doel:
    dag += 1
    munten *= 2
    print(f"Dag {dag}: je hebt {munten} munt(en).")

# Samenvatting
if doel <= 1:
    print("Je had het doel al bereikt bij de start.")
else:
    print(f"Doel bereikt (≥ {doel}) na {dag} dag(en).")
