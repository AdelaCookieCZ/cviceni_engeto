user_1 = {"name":"Marek", "surname":"Parek"}
user_email = {"user_email":"marek.parek@gmail.com"}
user_1.update(user_email)
print("User #01 ", user_1)

print("="*30)

jmeno = 'Marek'
heslo = '1236'
uzivatel = {'Marek': '1234'}

if heslo == uzivatel[jmeno]:              #muze byt i jako uzivatel.get(jmeno) == heslo:
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")

print("="*30)

cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)

cisla_1 = set(cisla_1)
cisla_2 = set(cisla_2)

sjednocene_sety = cisla_1.union(cisla_2)
print("Sjednocene sety ze zadani:", sjednocene_sety)
print("="*30)

cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = set(cisla_1)-set(cisla_2)          #cisla_1.difference(cisla_2)
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)


print("="*30)
usernames = ["Petr", "Jan", "Pavel", "Kristyna", "Helena"]
passwords = ["Heslo1", "Heslo2", "Heslo3", "Heslo4", "Heslo5"]

cities = ['Brno', 'Plzeň', 'Olomouc', 'Liberec', 'České Budějovice', 'Hradec Králové', 'Ústí nad Labem', 'Pardubice', 'Zlín', 'Ostrava', 'Karlovy Vary', 'Jihlava', 'Praha', 'Paskov', 'Kladno']
distances = [
    [0, 296, 77, 307, 216, 168, 296, 146, 96, 169, 337, 93, 208, 176, 240],
    [296, 0, 369, 200, 137, 208, 181, 213, 388, 462, 81, 217, 92, 469, 100],
    [77, 370, 0, 236, 290, 139, 370, 135, 63, 98, 411, 167, 282, 104, 314],
    [309, 198, 237, 0, 249, 98, 96, 155, 401, 434, 233, 230, 110, 449, 135],
    [217, 137, 290, 250, 0, 253, 239, 258, 309, 383, 218, 138, 151, 389, 183],
    [167, 209, 140, 97, 253, 0, 190, 24, 206, 238, 240, 112, 116, 245, 143],
    [298, 181, 371, 96, 238, 190, 0, 196, 390, 463, 122, 219, 93, 470, 87],
    [146, 214, 135, 154, 193, 24, 196, 0, 201, 234, 246, 90, 121, 240, 149],
    [96, 389, 62, 400, 308, 206, 389, 202, 0, 124, 430, 186, 300, 131, 333],
    [170, 463, 94, 440, 383, 239, 463, 235, 125, 0, 504, 261, 375, 14, 407],
    [337, 82, 410, 234, 218, 241, 121, 246, 429, 502, 0, 258, 127, 509, 105],
    [93, 218, 167, 229, 138, 113, 218, 90, 186, 259, 259, 0, 130, 266, 162],
    [209, 91, 282, 109, 150, 116, 92, 121, 301, 375, 128, 130, 0, 382, 31],
    [176, 469, 100, 451, 388, 244, 469, 240, 131, 13, 510, 266, 380, 0, 412],
    [240, 99, 313, 135, 181, 143, 86, 148, 332, 406, 105, 161, 31, 412, 0]
    ]

user = input("Zadej svoje jmeno:")
password = input("Zadej svoje heslo:")

if user in usernames and usernames.index(user) == passwords.index(password):
    print("Ahoj! Vyber si 2 z nasledujicich destinaci ", cities)
    destination_A = input("Destinace A:")
    destination_B = input("Destinace B:")
    if destination_A not in cities or destination_B not in cities:
        print("Jedna ze zadanych destinaci neni na seznamu.")
    else:
        index_A = cities.index(destination_A)
        index_B = cities.index(destination_B)
        value = distances[index_A][index_B]
        print("Vzdalenost mezi mesty je ", value, " km.")
else:
    print("Nespravne zadane uzivatelske jmeno nebo heslo!")