prvni_cislo = 5
druhe_cislo = 5

def nasobek(x,y):
    return x*y

vysledek = nasobek(prvni_cislo, druhe_cislo)

print("Vysledek je: " , vysledek)

print(30*"-")

vstup = 'Ahoj všem'

def nasobeni_znaku(x):
    zdvojeny_znak = []
    for i in x:
        zdvojeny_znak.append(i*2)
    return "".join(zdvojeny_znak)
    
vystup = nasobeni_znaku(vstup)

print(vystup)

print(30*"-")

import sys

def je_os_windows():
    return sys.platform.startswith('win')

print(je_os_windows())

print(30*"-")


prvni_cislo_1 = 12
druhe_cislo_2 = 16
def najdi_gcd(x1,x2):
    while x2 > 1:
        zbytek_po_deleni = x1 % x2
        if not zbytek_po_deleni:
            break

        x1, x2 = x2, zbytek_po_deleni
    return x2

print(najdi_gcd(prvni_cislo_1, druhe_cislo_2))
