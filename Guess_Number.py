import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print(" Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print(" Guess must be between 1 and 10.")
                continue

            if guess == number_to_guess:
                print(f" Correct! You guessed it in {attempts} attempts!")
                break
            else:
                print(" Wrong guess. Try again!")

        except ValueError:
            print(" Invalid input! Please enter a valid number.")

number_guessing_game()