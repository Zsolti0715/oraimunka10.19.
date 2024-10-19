def beolvass():
    oldal= int(input("Kérem adja meg a háromszögoldalát!"))
    return oldal
def hat():
    #6.	A program azt dönti el, hogy lehet-e háromszöget szerkezteni a felhasználótól beolvasott adatok alpján. akkor lehet hááromszöget szerkezsteni, ha: A háromszög bármely oldalának hossza kisebb a másik két oldal hosszának összegénél.
    #Azaz: a<b+c és b<a+c és c<a+b és c<a+b. Ügyelj arra, hogy a,b,c értékei 0-nál nagyobbnak pozitív valós számnak kell lennie, ha ez nem teljesül, térj vissza hibaüzenettel: „HIBA: Nem megfelelő bemenő adatok!”!
    a= beolvass()
    b= beolvass()
    c= beolvass()

    if (a>0 and b>0 and c>0):
        if (a < b) + c and (b < a) + c and (c < a) + b and (c < a) + b:
            print("A háromszög megszerkezthető")
        else:
            print("A háromszög nem megszerkezthető")
    else:
        ("HIBA: nem megfelelő bemenőadatok")



