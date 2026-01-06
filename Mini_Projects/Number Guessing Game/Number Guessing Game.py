import random

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Invalid choice! Defaulting level to 'easy' mode")
        return 10

def check_guess(guess, answer, attempts):
    if guess > answer:
        print("Too high!")
        return attempts - 1
    elif guess < answer:
        print("Too low!")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}. You win!")
        return 0

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)
    attempts = set_difficulty()
    
    guess = 0
    while guess != answer and attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts = check_guess(guess, answer, attempts)
        
        if attempts == 0 and guess != answer:
            print(f"You've run out of guesses. The correct number was {answer}.")
            break
        elif guess != answer:
            print("Guess again...")

game()
