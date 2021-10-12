import random

def roll_dice():
    random_getal = random.randrange(1, 6)
    print("Ik rol een getal")
    return random_getal

r1 = roll_dice()
print(r1)