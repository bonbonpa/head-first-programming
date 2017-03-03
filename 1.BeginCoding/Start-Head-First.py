print("Wellcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
    print("You win!")
else:
    if guess > 5:
        print("You High")
    else: 
        print("You low")
    print("You lose!")
print("Game Over!")