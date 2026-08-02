"""
The answer of the challenge given on the exercise_07_5.py
"""

# open the .txt and put all the words on a list called all_words
with open('z_english_dictionary.txt', 'r', encoding='utf-8') as english_dictionary:
    # 'r' are for python to read-only the .txt and the encoding is for not bug the open()
    all_words = [word.strip().lower() for word in english_dictionary.read().splitlines()]
    # set a list with all the words of the .txt file

# the check_word function of the exercise_07_5.py
def check_word(word, available, required):
    word = word.lower()
    available = available.lower()
    required = required.lower()
    if len(word) < 4:
        return False
    else:
        for letter in word:
            if letter not in available:
                return False
        for letter in required:
            if letter not in word:
                return False
        return True

# the function to pick a word with the game parameters
import random # to pick a random word in the .txt file

def pangram_selector(available, required):
    available = available.lower()
    required = required.lower()
    permitted_letters = set(available) # set() don't permit duplicate itens on the same list
    possible_words = [] # create an empty list for all the possible words for the pangram
    for word in all_words:
        word = word.lower()
        if required not in word:
            continue
        # the issubset() returns True if all elements of a set are present in another specified set or iterable
        if set(word).issubset(permitted_letters): # set for not allow duplicate words
            possible_words.append(word) # if issubset is true, put the word in the possible_words list
    return random.choice(possible_words) if possible_words else None
    # the random library random choose an iten in the possible_words list
    # and attribute the value of the str to the function, if the list is empty attribute the value of None (nothing)


# the base of the word_score function of the exercise_07_5.py
def word_score(word, available, required):
    word = word.lower()
    available = available.lower()
    valid_word = check_word(word, available, required)
    pangram = pangram_selector(available, required)
    if valid_word == False:
        return 0
    else:
        word_length = len(word)
        if word_length == 4:
            return 1
        elif word == pangram: # now, the function compare the value of word to the value of pangram
            return 15 # if it's the same, give the 15 points of the pangram
        else:
            return word_length
