print("Je wekker gaat af, slaap(SLAPEN) je verder of sta je op(OPSTAAN)?")
choice = input()
if choice == 'Opstaan':
    print("Je staat op en maakt je klaar voor de dag")
elif choice == 'Slapen':
    print("Slaap lekker")
else:
    print(choice, " Dat was niet een keuze")

print("Je bent wakker, ga je DOUCHEN of ONTBIJTEN?")
choice = input()
if choice == 'Douchen':
    print("Je gaat lekker warm douchen")
elif choice == 'Ontbijten':
    print("Je maakt en broodje kaas en eet het op.")
else:
    print(choice, " Dat was niet een keuze")

print("Je pizza is aangebrand in de oven, maak je een nieuwe(NIEUWE MAKEN) of eet je hem alsnog op(OPETEN)?")
choice = input()
if choice == 'Opeten':
    print("Je eet de pizza en krijgt buikpijn.")
elif choice == 'Nieuwe Maken':
    print("Je maakt nog een pizza en laat deze niet verbranden. Goed werk. ")
else:
    print(choice, " Dat was niet een keuze")


print("Je valt van een gebouw af. Pak je je PARAPLU of ga je DOOD?")
choice = input()
if choice == 'Dood':
    print("Je valt te pletter maar je bent built different dus je overleeft het.")
elif choice == 'Paraplu':
    print("Je pakt je paraplu erbij en land veilig op de weg.")
else:
    print(choice, " Dat was niet een keuze")


print("Je gaat naar de supermarkt, koop je spullen voor NASI of voor PIZZA")
choice = input()
if choice == 'Nasi':
    print("Je maakt een nasi en je eet het op.")
elif choice == 'Pizza':
    print("Je maakt een pizza en laat het aanbranden in de oven.")
else:
    print(choice, " Dat was niet een keuze")