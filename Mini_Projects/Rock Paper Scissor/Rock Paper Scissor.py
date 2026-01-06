import random

choices = ["rock", "paper", "scissor"]

try:
    user_input = int(input("Enter 0 for rock, 1 for paper and 2 for scissor: "))

    if user_input not in [0, 1, 2]:
        print("Invalid input. Please enter only 0, 1, or 2.")
    else:
        user_choice = choices[user_input]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("Draw")
        elif ((user_choice == "paper" and computer_choice == "rock") or
              (user_choice == "scissor" and computer_choice == "paper") or
              (user_choice == "rock" and computer_choice == "scissor")):
            print("You win!")
        else:
            print("You lose!")

except ValueError:
    print("Please enter a valid integer input (0, 1, or 2).")