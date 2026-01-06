import random
word_list = ["journey", "life", "experience", "venture", "spirit"]
chosen_word = random.choice(word_list)

lives = 6
guessed_word = []
game_over = False

placeholder = "-" * len(chosen_word)
print(placeholder)

while not game_over:
    display = ""
    print(f"\nYou have {lives}/6 Lives Left")
    guess = input("Guess the letter: ").lower()

    if guess not in guessed_word:
        guessed_word.append(guess)

    for letter in chosen_word:
        if letter in guessed_word:
            display += letter
        else:
            display += " _ "

    print("Current Word: ", display)

    if guess not in chosen_word:
        lives -= 1
        print("You've guessed wrong.")

    if "_" not in display:
        print("You guessed the word! You win!")
        game_over = True

    if lives == 0:
        print("You're out of lives. Game Over.")
        print(f"The correct word was: {chosen_word}")
        game_over = True