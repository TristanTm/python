import sys
import time


def callMe(name, number, name2, number2):
    print("&: Hello its"+ name2)
    time.sleep(1)
    print("&: Wie is dit?")
    time.sleep(1)
    print("#: It's me "+ name)
    time.sleep(1)
    print("&:Hi "+ name+ " Sorry ben nu bezig, kan ik je later terug bellen?")
    time.sleep(1)
    print("#: Ja dat kan.")
    time.sleep(1)
    print("&: Wat is je nummer?")
    time.sleep(1)
    print("#Het is "+number+ " wat is jouw nummer?")
    time.sleep(1)
    print("Mijn nummer is"+ number2)
    time.sleep(1)
    print("&: Top, zal je later terug bellen!")
    time.sleep(1)
    print("#: Doei!")
    time.sleep(1)
    print("click...")

callMe(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

