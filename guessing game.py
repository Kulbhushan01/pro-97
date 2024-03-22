import random

number = random.randint(1, 9)
chances = 0

while chances < 5:  
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! YOU WON!!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    
    chances += 1

if chances == 5:
    print("YOU LOSE!!,The number is ", number)