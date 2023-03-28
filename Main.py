import Bil

looping = True
BMW_svart = Bil.bil("BMW", "svart", 3)
Merca_gul = Bil.bil("Merca", "gul", 6)
Ferarri_grön = Bil.bil("Ferarri", "grön", 20)
Bugatti_brun = Bil.bil("Bugatti", "brun", 1)

billista = [BMW_svart, Merca_gul, Ferarri_grön, Bugatti_brun]

print(BMW_svart.getFabrikat())

while looping:

    i = 0

    for Bil in billista:
        print(str(i+1) + "Fabrikat: " + Bil.getFabrikat() + "färg:" + Bil.getColor())
        i += 1

    bil_nr = input("\nMata in bilNr för vald bil:")

    print("En" + billista[int(bil_nr)-1].fabrikat + ", färg" + billista[int(bil_nr)-1].color )

    svar_anvandare = input("\nvill du avsluta programmet? j/n : ")

    if (svar_anvandare == "j"):
        break