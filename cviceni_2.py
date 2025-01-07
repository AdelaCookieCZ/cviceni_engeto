zamestnanci = ['František','Anna','Jakub','Klára']

print("Zamestnanci na zacatku:", zamestnanci)

zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anezka')

print("Nova pridana jmena:", zamestnanci_a)


zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, 'Bruno')

print("Nova jmena vlozena:", zamestnanci_b)

print("="*30)

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = 3 

if cislo_dne in vstupni_cisla:
    print("Spravna vstupni hodnota!")
    den_tydne = tyden[cislo_dne-1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne-1]):
        print("Spravne pismeno")
    else:
        print("Nespravne pismeno")
else:
    print("Spatna vstupni hodnota!")


print("="*30)


print(id(11))
jmeno = "Petr"

print(id(jmeno))
print(id("Petr"))


l_1 = [1,3,4]
l_2 = l_1
l_3 = l_1.copy()

l_1.append(5)

print(l_2)
print(l_3)

print("="*30)

# cislo = int(input("Vlozte cele cislo:"))

# if cislo % 3 == 0 and cislo % 5 == 0:
#     print("FizzBuzz")
# elif cislo % 3 == 0:
#     print("Fizz")
# elif cislo % 3 == 0:
#     print("Buzz")
# else:
#     print(cislo)

print("="*30)
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

heslo = heslo_2

if not heslo:
    print("Vynechal jsi pole s heslem!")
elif heslo[0].isdigit() or heslo.isdigit():    
#elif heslo[0].isdigit() and not heslo.isnumeric():
    print("Heslo nesmí začínat číselným znakem")
elif len(heslo)<8:
    print("Heslo musí být alespoň 8 znaků dlouhé")
elif "@" in heslo:
#elif heslo.find('@') != -1:    
    print("Heslo nesmí obsahovat '@'")
elif heslo.isnumeric() or heslo.isalpha():
    print("Heslo musí obsahovat jak číselné znaky, tak písmena")
else:
    print("Heslo je v pořádku")