# 1.feladat
#Írjuk ki 0-tól 150-ig a páros számokat!
def feladat1():
    i=0
    while i<=150:
        if i != 150:
            print(i,end=";")
        else:
            print(i,end=" ")

        i+=2
#Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
def feladat2():
    i=0
    harommal_osztható=0
    while( i<=10):
        szam:int=int(input("Adj meg egy számot:"))
        if szam % 3 ==0:
           harommal_osztható+=1
        i+=1
    print("3-mal osztható számok száma",harommal_osztható)

#Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
def feladat3():
    szam:int=int(input("Adje meg egy 10-zel osztható számot"))
    while not(szam % 10 == 0):
            szam:int=int(input("Ez a szám nem osztható 10-zel! Adj meg egy másikat:"))
    print("Végre jó számot adtál meg")

#Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def feladat4():
    szam = 0

    while szam < 10 or szam > 99 or szam % 2 != 0:
        szam = int(input("Kérem adjon meg egy kétjegyű páros számot: "))
    print("A megadott szám megfelel:", szam)
def feladat5():
    szam=int(input("Kérlek adj meg egy pozitív páratlan számot"))
    while szam <= 0 or szam % 2 == 0:
        szam= int(input("A megadott szám nem felel meg, adj meg egy másikat"))
    print("A megadott szám",szam)
def feladat6():
    szam = int(input("Kérem adjon meg egy számot: "))

    while szam % 3 != 0 and int(szam ** 0.5) ** 2 != szam:
        szam = int(input("A megadott szám nem felel meg. Kérlek adj meg egy másik számot: "))

    print("A megadott szám 3-mal osztható vagy négyzetszám:", szam)

def feladat7():
    a:int=int(input("Adj meg ey számot"))
    b:int=int(input("Adj meg egy számot"))
    c:int=int(input("Adj meg gy számot"))
    while not