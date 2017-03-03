from random import randint
secret = randint(1,10)
print("Wellcome!")
guess = 0
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess > secret:
        print("You High")
    elif guess < secret:
        print("You low")
    else: 
        print("You Correct")
    #print("You lose!")
print("You win!")
print("Game Over!")