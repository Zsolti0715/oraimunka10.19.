import math

def negy():
   # 4.	feladat: Proth-számok
# A számelmélet területén a François Proth matematikusról elnevezett Proth-számok a következő alakban felírható egész számok:
# ahol k pozitív egész páratlan szám és n pozitív egész, amire    Ha a feltételek nem teljesülnek térjen vissza hibaüzenettel: „HIBA: Nem megfelelő számok!”
# Írd ki a sorozat első 10 elemét vesszővel elválasztva egy sorba, hogy az utolsó után ne legyen vessző! (Az első néhány Proth-szám:  3, 5, 9, 13, 17, 25, 33, 41, 49, 57, 65, 81, 97, 113, 129, 145, 161, 177, 193, 209, 225, 241, etc.)
# pl1.:Kimenet: Proth-számok:  3, 5, 9, 13, 17, 25, 33, 41, 49, 57

    k=1
    n=1
    if (k % 2 == 1) and (n > 0) and (math.pow(2,n) > k):
        print("Proth-számok: ",end="")
        for n in range(0,10,1):
            proth = (k * math.pow(2, n)) + 1
            print(str(proth)+", ",end="")
        proth = (k * math.pow(2, 10)) + 1
        print(proth)

    else:
     print("HIBA:Nem megfelelő számnokt!")

def negyb():
    k = 1
    n = 1
    print("Proth-számok: ", end="")
    while n < 10:
        if (k % 2 == 1) and (k>0) and (n > 0) and (math.pow(2, n) > k):
            proth = (k * math.pow(2, n)) + 1
            print(str(proth) + ", ", end="")
            n += 1
            proth = (k * math.pow(2, 10)) + 1
            print(proth)

        else:
            print("HIBA:Nem megfelelő számnokt!")
            proth = (k * math.pow(2, 10)) + 1
            print(proth)

