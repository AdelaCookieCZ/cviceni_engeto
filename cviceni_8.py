def je_anagram(*args) -> bool:
    vzor = sorted(args[0])

    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True
    
print(
    je_anagram("ship", "hips", "hisp"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)

print(30*"-")

adresy = [
   "matous@holinka.com",
   "danek11@seznam.cz",
   "rennud15@gmail.com",
   "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(emails: list):
    vysledek = []
    for email in emails:
        for znak in email:
            if not znak.isnumeric():
                continue
            vysledek.append(email)
            break
    return vysledek

print(filtruj_adresy_s_cisly(adresy))

print(30*"-")

def je_prvocislo(cislo: int, prvocisla: tuple) -> bool:
    return cislo in prvocisla

def generuj_interval_prvocisel(stop: int) -> tuple:
    vsechna_cisla = tuple(range(stop+1))
    vysledek = list()

    for cislo in vsechna_cisla:
        if cislo == 0 or cislo == 1:
            continue
        for filtr_cislo in range(2, cislo):
            if cislo % filtr_cislo == 0:
                break
        else:
            vysledek.append(cislo)
    return tuple(vysledek)


print(je_prvocislo(23, generuj_interval_prvocisel(30)),
    je_prvocislo(233, generuj_interval_prvocisel(300)),
    je_prvocislo(146, generuj_interval_prvocisel(300)),
    sep="\n"
)

print(30*"-")

text = """\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, 
porttitor nec molestie quis, auctor a quam. Quisque b2b@money.fr pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed, luctus lacinia risus. Maecenas posuere leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam erat volutpat. Donec eleifend felis at leo ullamcorper cursus. Pellentesque id dui viverra, auctor enim ut, fringilla est. Maecenas gravida turpis nec ultrices aliquet.
"""

def uloz_emailove_adresy(pozadovany_text: str) -> list:
    text_list = pozadovany_text.split()
    vysledek = list()

    for word in text_list:
        if "@" in word:
            vysledek.append(word)
    return vysledek
        
print(uloz_emailove_adresy(text))