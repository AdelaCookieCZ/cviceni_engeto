# # jmeno_souboru = "novy_soubor.txt"
# # pozdrav = "Ahoj, toto je první zápis do textového souboru"

# # txt_soubor = open(jmeno_souboru, mode="w")
# # txt_soubor.write(pozdrav)

# # # řádné zavření souboru
# # txt_soubor.close()

# # print(txt_soubor.closed) #overeni, zda je soubor skutecne zavreny

# # txt_soubor = open("novy_soubor.txt", mode="r")
# # obsah_txt = txt_soubor.read()
# # print(obsah_txt)
# # txt_soubor.close()

# druhy_radek = "Ted pridavas druhy radek"

# txt_soubor = open("novy_soubor.txt", mode="r+")
# obsah_txt = txt_soubor.read()
# txt_soubor.write(druhy_radek)

# txt_soubor.close()


# treti_radek = "Toto je treti radek tveho puvodniho souboru souboru ^.^"

# txt_soubor = open("druhy_soubor.txt", mode="a")
# txt_soubor.write(treti_radek)
# txt_soubor.close()


# def zobraz_slova(textovy_soubor):
#     zadana_slova = open(textovy_soubor, "r")

#     data = zadana_slova.read()
#     slova = data.split()

#     for slovo in slova:
#         if len(slovo) >= 7:
#             print(slovo, end=" ")
#     zadana_slova.close()

# if __name__ == "__main__":
#     zobraz_slova("slova.txt")
print("-"*30)

# prvni_radek = "První řádek v souboru,\n"
# druhy_radek = "druhý řádek v souboru,\n"
# treti_radek = "třetí řádek v souboru."

# txt_soubor = open("txt_soubor.txt", mode="w")
# txt_soubor.write(prvni_radek)
# txt_soubor.write(druhy_radek)
# txt_soubor.write(treti_radek)

# txt_soubor.close()

# cteni_txt = open("txt_soubor.txt")
# obsah_txt = cteni_txt.readlines()
# print(obsah_txt)


print("-"*30)
# Vstupní proměnné
kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567

# Přesnost pro číselné znaky
formatovana_presnost = \
    f"|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|"

# Přesnost a ostatní specifikátory
formatovana_kombinace = f"|{kombinace:$<6.4}|"

# Přesnost u stringu
formatovana_presnost_str = f"|{presnost_str:.4}|"

# Výpis hodnot
print(f"""\
Naformátovaná přesnost: \t{formatovana_presnost},
Naformátovaná kombinace: \t{formatovana_kombinace},
Naformátovaný string: \t\t{formatovana_presnost_str}.""")

# Ulož proměnné do souboru 'vysledek.txt'
print("Zapisuji do souboru")

with open("vysledek.txt", mode="w") as txt:
    txt.write("\n".join(
        (formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)
        )
    )