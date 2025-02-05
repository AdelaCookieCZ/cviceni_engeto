# def nacti_radky(cesta_k_souboru):
#     try:
#         soubor = open(cesta_k_souboru,mode="r")
#     except FileNotFoundError:
#         print(f"Soubor: {cesta_k_souboru} neexistuje!")
#         # vysledek = []
#     else:
#         vysledek = soubor.read()
#         soubor.close()
#     finally:
#         print(vysledek)

# nacti_radky("jazyky.txt")

# test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, '\\n', 4]

# def secti_hodnoty(udaje):
#     vysledek = 0.0
#     for i in test:
#         try:
#             cislo = float(i)
#         except Exception:
#             print(f"{i} nelze prepsat na float, hodnota nebude prictena")
#         else:
#             vysledek += cislo
#     return vysledek

# print("Vysledek:", secti_hodnoty(test))

# muj_slovnik = {
#     'jmeno':'Pepa',
#     'prijmeni': 'Novak',
#     'rok_narozeni': 1990
# }

# def obsahuje_klic_a_hodnotu(klic, hodnota, slovnik):
#     try:
#         nalezena_hodnota = slovnik[klic]
#     except KeyError:
#         print(f'Klíč: {klic}, nenalezen.')
#         vysledek = False
#     else:
#         print(f"Klíč: {klic}, nalezen.")

#         if nalezena_hodnota == hodnota:
#             vysledek = True
#         else:
#             print(f"Hodnota: {hodnota}, nenalezena.")
#             vysledek = False
#     finally:
#         return vysledek


# print(obsahuje_klic_a_hodnotu("jmeno", "Petr", muj_slovnik))

nums = 0
for num in range(10):
    nums += num
print(nums)