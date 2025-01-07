import random

moznosti = ["kamen", "nuzky", "papir"]
hrac = "kamen"
pocitac = random.choice(moznosti)

print("Hrac: ", hrac, ", Pocitac: ", pocitac)
if pocitac == "papir":
    print("Vyhral jsi!")
elif pocitac == "nuzky":
    print("Prohral jsi :(")
else:
    print("Nerozhodne")


print(30*"-")

import os

jmena_slozek = ("obrazky", "texty", "gify")

for jmeno in jmena_slozek:
    if os.path.exists(jmeno) and os.path.isdir(jmeno):
        print("Slozka jiz existuje")
    else:
        print("Vytvarim  novou slozku.")
        os.mkdir(jmeno)

print("Vsechny slozky existuji")

print(30*"-")

min_hodnota = int(1)
max_hodnota = int(6)

while True:
    print("Hazim kostkou: ")
    kostka = random.randint(min_hodnota, max_hodnota)

    print("Vysledek na kostce je: ", kostka)
    if kostka == 6:
        continue
    else:
        break