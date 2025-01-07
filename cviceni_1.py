import datetime

aktualni_cas = datetime.datetime.now()

print("Ahoj na první lekci. Dneska máme", aktualni_cas.strftime("%d/%m/%Y"))

print(5%2)

print("adela.kolackova@gmail.com"[6:15]) #vcetne:bez
print("adela.kolackova@gmail.com"[6:15:2]) #::2 krok
print("adela.kolackova@gmail.com"[::-1])  #prepise se mi to zprava doleva



print("0123456789","|","0123456789"[::-1],"|","0123456789"[::3],"|","0123456789"[7:12])
