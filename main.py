# HANGMAN
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

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

    # Loop through each position in the chosen_word, If the letter at that position matches 'guess' then reveal that
    # letter in the display at that position.
    letter_found = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            letter_found = True

    if not letter_found:
        lives -= 1

    print(display)

if lives > 0:
    print("You win!")
else:
    print("You lost!")
