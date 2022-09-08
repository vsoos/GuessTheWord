# guess the word game
import string
import random
from hangman import *


def add(random_word):
    for letter in random_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    return letter


words = ["apple", "house", "man", "cat", "politics", "bell", "lamp", "three"]
attempt = 10

# random word from the word list
random_word = random.choice(words)

# all letters from the English alphabet that can be used
possible_letters = set(string.ascii_letters)

# the guesses that match the letters of the word
correct_letters = set(random_word)

# the letters that were guessed
guessed_letters = set()


while True:
    play = input("Do you want to play? (yes/no)\n")

    if play == "yes":
        # introduction to the game
        print("Welcome to a guess the word game!\n")
        print("The word list exclusively contains lower case words, so use lower case letters only!\n")

        while len(correct_letters) > 0 and attempt > 0:
            guesses = ', '.join(guessed_letters)
            if attempt == 1:
                print(f"You have 1 attempt left, you have used: {guesses}")
            else:
                print(f"You have {attempt} attempts left, you have used: {guesses}")

            # use function to collect letters
            letters = []
            add(random_word)

            # print remaining attempts
            print(hangman[attempt])
            filled_in = " ".join(letters)
            print(f"Guess the word {filled_in}")

            guess = input("Enter a letter: ")

            # error message is received when the same letter is entered multiple times
            if guess in guessed_letters:
                print("You already used this letter! Try another one.\n")

            else:
                # it's checked whether the guessed word is a letter of the English alphabet
                if guess in possible_letters - guessed_letters:
                    guessed_letters.add(guess)

                    # correct letters are added to the word
                    if guess in correct_letters:
                        correct_letters.remove(guess)
                        print("")

                    # if attempt is incorrect the player has one less attempts
                    else:
                        attempt = attempt - 1
                        print(f"Your letter, {guess}, is not in the word.\n")

                # error message is printed if the input is not part of the English alphabet
                else:
                    print("Invalid input.\n")

        # if the user runs out of lives the word is printed and the game ends
        if attempt == 0:
            print(hangman[0])
            print(f"You have ran out of attempts, {random_word} was the solution.")

        # if the player wins the correctly guessed word is printed
        else:
            print(f"The correct word was {random_word}. Congrats!")

    # if the player chooses no the game ends
    elif play == "no":
        exit()

    else:
        print("Invalid input")
