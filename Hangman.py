import random

words = ["apple", "tiger", "python", "school", "orange"]
word = random.choice(words)

guessedLetters = []
incorrectGuesses = 0
maxGuesses = 6

print("          Welcome to Hangman          ")

while incorrectGuesses < maxGuesses:
    display = ""
    for letter in word:
        if letter in guessedLetters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord: ", display)

    if "_" not in display:
        print("Congratulations, you guessed the word: ", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessedLetters:
        print("You've already guessed that letter")
        continue

    guessedLetters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        incorrectGuesses += 1
        print("Wrong!")
        print("Incorrect guesses:", incorrectGuesses, "/", maxGuesses)

if incorrectGuesses == maxGuesses:
    print("\nGame Over!")
    print("The correct word was:", word)













