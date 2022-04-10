import random

def rolldice(min,max):
    while True:
        number = random.randint(min,max)
        print(f"Your number is {number}")
        break

rolldice(1,6)