print("Hello You!, ik ben Tristan ")

Name = input("Wie ben jij? ")
print("Hello " + Name ) 




Vraag = input("Waar woon ik in Noord Holland: A) Zaandam. B) Alkmaar. C) Den Helder. [A/B/C]? : " )

if Vraag == "A" :
    print("Yes dat klopt! Ik woon nu al 14 jaar in Zaandam ")
elif Vraag == "B" : 
    print("Nee ik woon niet in Alkmaar, ik ben er wel een paar keer geweest ")
elif Vraag == "C" : 
    print("Ik woon niet in Den Helder, ik kom er wel vaak als ik naar texel ga!")



Vraag2 = input("Welke games speel ik het meest: A) Overwatch. B) Apex Legends. C) GTA 5. [A/B/C]? :")

if Vraag2 == "A" :
    print("Helaas niet, ik speel het wel veel maar ik speel het niet het meest ")
elif Vraag2 == "B" :
    print("Jup! Ik speel APex legends als sinds de dag dat het uit kwam! ")
elif Vraag2 == "C" :
    print("Ik speel het de laatste tijd wel meer maar het is niet wat ik het meeste speel ")


Vraag3 = input("Welke huisdieren heb ik: A) Hond en Kat. B) Vogels en Kat. C) Alleen een kat. [A/B/C]? :")

if Vraag3 == "A" : 
    print("Nope ik heb er hier maar een van de twee, ik zou wel graag een hond willen ")
elif Vraag3 == "B" :
    print("Jup! Ik heb zelf 2 vogels en we hebben dan ook nog een kat! Niet de beste combo haha ")
elif Vraag3 == "C" : 
    print("Ik heb wel een hele lieve kat maar daarnaast ook nog andere dieren dus niet alleen een kat ")





print("Je bent opeens op een gebouw wat doe je?")
Spel = input("Wat doe je?: A) Spring naar beneden en hoop op het beste. B) Neem rustig de trap naar beneden. [A/B]? :")

if Spel == "A" :
    print("Aparte keuze maar je valt op de grond en breekt je benen")
    Spell = input("Roep je om hulp of bel je zelf een ambulance? A) Ambulance. B) Roep voor hulp. [A/B]? :")
    if Spell == "A" : 
        print("Top de ambulance haalt je op en je bent opgelapt")
    elif Spell == "B" :
        print("Mensen horen je niet en je eindigt in een steegje achter een gebouw")


if Spel == "B" : 
    print("Je komt beneden aan en je kan naar het strand of naar huis")
    Spelll = input("Je kan kiezen of je naar huis wil of naar het strand A) Het strand. B) Naar Huis. [A/B]? :")
    
    if Spelll == "A" :
        print("Op Het strand staan een boot en vliegtuig klaar")
        Spellll = input("Neem je het vliegtuig of de boot A) Vliegtuig. B) Boot. [A/B]? :")
        if Spellll == "A" : 
            print("Waarom zou je dat doen? Het vliegtuig zinkt in het zand en je overleeft het niet")
        if Spellll == "B" : 
            print("Je gaat er vandoor met de boot en je word nooit meer gezien.")


    if Spelll == "B" : 
        print("Je loopt naar huis en thuis kan je gaan slapen of op de bank netflix kijken")
        Spel2 = input("Wat wordt de keuze A) Netflix kijken. B) Slapen. [A/B]? :")
        if Spel2 == "A" :
            print("je kijkt de hele series van Aroow en krijgt er de rest van je leven spijt van")
        elif Spel2 == "B" :
            print("Slaap lekker")

