# guess the word game with more functions
import string
import random
from hangman import *

words = ["apple", "house", "man", "cat", "politics", "bell", "lamp", "three"]
attempt = 9

# random word from the word list
random_word = random.choice(words)

# all letters from the English alphabet that can be used
possible_letters = set(string.ascii_letters)

# the guesses that match the letters of the word
correct_letters = set(random_word)

# the letters that were guessed
guessed_letters = set()


def add_guess(random_word):
    for letter in random_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    return letter


def join_guess(guessed_letters):
    joined_guess = ', '.join(guessed_letters)

    return joined_guess


def join_sol(letters):
    joined_sol = " ".join(letters)

    return joined_sol


while True:
    play = input("Do you want to play? (yes/no)\n")

    if play == "yes":
        # introduction to the game
        print("Welcome to a 'Guess the word game'!")
        print("The word list exclusively contains lower case words, so use lower case letters only!")
        print("-----------------------------------\n")

        while attempt and len(correct_letters) > 0:

            if attempt == 1:
                print(f"You have 1 attempt left, you have used: {join_guess(guessed_letters)}")
            else:
                print(f"You have {attempt} attempts left, you have used: {join_guess(guessed_letters)}")

            # use function to collect letters F1
            letters = []
            add_guess(random_word)

            # print remaining attempts
            print(hangman[attempt])

            print(f"Guess the word {join_sol(letters)}")

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
                print(f"You have ran out of attempts, {random_word} was the correct solution.\n")

            # if the player wins the correctly guessed word is printed
            else:
                print(f"The correct solution was {random_word}.\n")

    # if the player chooses no the game ends
    elif play == "no":
        exit()

    else:
        print("Invalid input\n")
