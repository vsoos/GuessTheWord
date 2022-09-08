import random
import words
import string

word = random.choice(words)
letters = set(word)
letters_used = set()
all_letters = set(string.ascii_lowercase)
