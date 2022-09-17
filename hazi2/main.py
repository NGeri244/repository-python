kezdo = "Adjon meg egy számot és egy mértékegységet (cm/inch): "
print(kezdo)
ertek = str(input())
mertekE = str(input())
vegeredmeny = 0

if mertekE == "cm" or mertekE == "inch":
    if mertekE == "cm":
        vegeredmeny = float(ertek) * 0.393700787
        print(str(vegeredmeny) + " inches")
    else:
        vegeredmeny = float(ertek) / 0.393700787
        print(str(vegeredmeny) + " centimeters")
else:
    print("Not correct unit!")




