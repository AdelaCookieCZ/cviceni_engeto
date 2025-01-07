index = 0

while index < 5:
    if index % 2 == 1:
        print("index:", index)
    index = index + 1

print("Smyčka skončila")

print(30*"-")

slova = set()

while len(slova) != 3:
    slovo = str(input("Zadej slovo o 4 znacich: ".upper()))
    if slovo in slova:
        print(f"Slovo {slovo} už je uložené")
    elif len(slovo) == 4:
        slova.add(slovo)
    else:
        print("Slovo neni dlouhe 4 znaky")
else:
    print("Uz mam ulozene 3 slova")

print(30*"-")

ovoce = {"jablko", "banan", "citron", "pomeranc"}

print(f"Dostupne ovoce:", ", ".join(ovoce))

while True:
    vyber = input("Vyber z uvedeneho ovoce: ")
    if vyber not in ovoce:
        print("Vyber neni v nabidce.")
    else:
        print("Bezva, toto ovoce je v nabídce.")
        break

print(30*"-")

while True:
    operator = input(f"Vlozte aritmeticky operator + nebo -: ")
    if operator not in ('-', '+'):
        print("Zadany operator neni v nabidce")
    else:
        cislo_1 = int(input(f"Vlozte prvni cislo: "))
        cislo_2 = int(input(f"Vlozte druhe cislo: "))
        if operator == "+":
            print(f"{cislo_1} + {cislo_2} = {cislo_2 + cislo_1}")
        elif operator == "-":
            print(f"{cislo_1} - {cislo_2} = {cislo_1 - cislo_2}")
        pokracovat = input("Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne): ")
        if pokracovat == 'a':
            continue
        else:
            print("Ukoncuji program")
            break