# HANGMAN
import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# creates a list filled with "_" for every letting in chosen_word
display = []
for ch in chosen_word:
    display.append("_")

# While loop to allow the user to make multiple guesses
while "_" in display:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter?: ").lower()

    # Loop through each position in the chosen_word, If the letter at that position matches 'guess' then reveal that
    # letter in the display at that position.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    letter_found = False
    for ch in chosen_word:
        if ch == guess:
            letter_found = True

    if letter_found:
        print("Correct!")
    else:
        print("Wrong!")

    print(display)
