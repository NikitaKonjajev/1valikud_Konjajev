from random import *
from math import *


#Работа Артема М
try: 
    vanus=int(input("Kui vana sa oled? "))
    if vanus>=18:
        print("Kas te annate vanematele loa oma Tahvelit vaadata?")
        o=(input("Jäh või Ei. "))
        if o.lower()=="jäh":
            print({o})
            print("See on ligipääs teie vanematele.")
            print("Tahvel on kinni. ")
        elif o.upper()=="EI":
            print("sissepääs puudb.")
            print("Tahvel on kinni. ")
    if vanus <18:
        print("Juurdepääs vanematele on automaatselt antud. ")
except:
    print("Tahvel on kinni")
print()


#Работа Лехи
try:
    päev=int(input("Mis päev ja  itu tundi täna on?"))
    if päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisipäev"
        n="8 tundi"
    elif päev==3:
        n="Kolmapäev"
        n="6 tundi"   
    elif päev==4:
        n="Neljapäev"
        n="5 tundi" 
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==6:
        n="Pühapäev"
        n="0 tundi"
    else: 
        n="vale number"
    print(n)
except:
    print("!!!!!!!!")

    print()


#Määrata ja tuletada suurem kahest sisestatavast arvust.
print("Määrata ja tuletada suurem kahest sisestatavast arvust")
a=randint(-100,100)
b=randint(-100,100)
print(f"a={a}\nb={b}")
if a>b:
    print(f"arv {a} on suurem arv {b}")
elif b>a:
    print(f"arv {b} on suurem arv {a}")

print()


#Isikukoodi kontrollimine
print("Isikukoodi kontrollimine")
text=input("Palun kirjuta teie isikukod: ")
n=len(text)
if n==11 and text.isdigit(): 
    print("Teie hagikood on sisestatud õigesti")
else:
    print("iskukoodis lubamatud väärtused!")

print()


#13/12/22
r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr: 
       print(f"Rudu pindala {Skv} m^2 on suurem ringi pindala {Skr} m^2")
    elif Skr>Skv:
       print(f"Rindi pindala {Skr} m^2 on suurem ruudu pindala {Skv} m^2")
    else:
       print("Pindala ov võrsed. {Skr} m^2")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")
print()


#2 версия только лучш чем "2"
print("Nädalapäevad")
try:
    p=int(input("Mis päev täna on?"))
    if   p==1:
        n="Esmaspäev"
    elif p==2:
        n="Teisipäev"
    elif p==3:
        n="Kolmapäev"
    elif p==4:
        n="Neljapäev"
    elif p==5:
        n="Reedel"
    elif p==6:
        n="Pühapäev"
    elif p==7:
        n="Laupäev"
    else:
        n="Vale Number"  
    print(n)
except:
    print("Viga")


#2
try:
    päev=int(input("Mis päev täna on?"))
except:
    print("!!!!!!")
if päev==1:
    print("Esmaspäev")
elif päev==2:
    print("Teisipäev")
elif päev==3:
    print("Kolmapäev")
elif päev==4:
    print("Neljapäev")
elif päev==5:
    print("Reedel")
elif päev==6:
    print("Pühapäev")
elif päev==7:
    print("Laupäev")
else:
    print("Viga!")


#1
try:
    hinne=int(input("Mis hinne täna said koolid"))
except:
    print("!!!!")
if hinne==5:
    print("väga hea")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2 or hinne==1: #and, or,not !=ei võrdu,<,>,>=,<=
    print("Mitte rahuldav") 
else:
    print("Viga!")


a=6
b=4
a=2*a+3*b 
b=a/2*b