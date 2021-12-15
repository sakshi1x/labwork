import random
x = random.randint(1,9)

while True:
    y = int(input("guess a number between 1 to 9: "))
    if x == y :
       print("well guessed")
       break
    else:
        print("guess again")
    