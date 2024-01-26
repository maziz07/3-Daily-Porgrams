import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")

    print("Congratulations! You guessed the right number.")

guess_the_number()
