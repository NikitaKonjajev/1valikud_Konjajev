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



