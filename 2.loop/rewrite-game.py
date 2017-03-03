from random import randint
secret = randint(1,10)
print("Wellcome!")
guess = 0
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("You High!")
        else:
            print("You low!")
print("Game Over!")