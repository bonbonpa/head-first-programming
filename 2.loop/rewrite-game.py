print("Wellcome!")
guess = 0
while guess != 5:
    g = input("Guess the number: ")
    guess = int(g)
    if guess > 5:
        print("You High")
    else: 
        print("You low")
    #print("You lose!")
print("You win!")
print("Game Over!")