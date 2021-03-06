# HANGMAN
import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# creates a list filled with "_" for every letting in chosen_word
display = []
for ch in chosen_word:
    display.append("_")

lives = 6
# While loop to allow the user to make multiple guesses
while "_" in display and lives > 0:
    print(stages[lives])
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter?: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Loop through each position in the chosen_word, If the letter at that position matches 'guess' then reveal that
    # letter in the display at that position.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # if the letter is not in the chosen word, reduce number of lives
    if guess not in chosen_word:
        print(f"You've guessed {guess}, which is not in the word.")
        lives -= 1

    print(f"{' '.join(display)}")

if lives > 0:
    print("\nYou win!")
else:
    print(stages[0])
    print("You lost!")
