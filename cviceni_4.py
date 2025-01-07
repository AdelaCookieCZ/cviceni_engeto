veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'

result = {'souhlasky': 0, 'samohlasky': 0}

for prvek in veta:
     # .. pokud znak není písmeno
    if not prvek.isalpha():
        continue
    elif prvek.lower() in samohlasky:
        result['samohlasky'] += 1
    elif prvek.lower() in souhlasky:
        result['souhlasky'] += 1

print("Pocet souhlasek: ", result['souhlasky'], "| Pocet samohlasek: ", result['samohlasky'])

print(30*"=")
#reseni engeto
# Slovník s evidencí výskytu jednotlivých typů písmen
vysledek = {'souhlasky': 0, 'samohlasky': 0}

# Iterace přes zadanou proměnnou 'veta'
for pismeno in veta:
    # .. pokud znak není písmeno
    if not pismeno.isalpha():
        continue

    # .. pokud je převedený znak mezi hodnotami samohlásek
    elif pismeno.lower() in samohlasky:
        vysledek['samohlasky'] += 1
    # .. pokud je převedený znak mezi hodnotami souhlásek
    elif pismeno.lower() in souhlasky:
        vysledek['souhlasky'] += 1

# Vypiš závěrečný výstup v podobě celkového počtu samohlásek a souhlásek
print('Počet souhlásek:', vysledek['souhlasky'], '| Počet samohlásek:', vysledek['samohlasky'])


print(30*"=")

cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda += cislo
    else:
        licha += cislo

vysledek = abs(suda - licha) #zajisti, ze vysledek bude vzdy kladny
print("Rozdil je: ", vysledek)

print(30*"=")

vysledek = list()
start = 3
stop = 20
delitel = 5

if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print("Zadane rozsah: <", start, ", ", stop,">")
    for number in range(start, stop + 1):
        if number % delitel == 0:
            vysledek.append(number)
    print("Cisla delitelna ", delitel, ":", vysledek)

else:
    print("Zadané vstupy musí být čísla.")

print(30*"=")

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

delka_slov = {slovo: len(slovo) for slovo in seznam_slov}

print(delka_slov)