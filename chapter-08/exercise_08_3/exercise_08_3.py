"""
Wordle in Python!
A function that you can play Wordle in Python
"""
# The book doesn't specify what list of words you will use to create the function, I will use the english dictionary
# file in the chapter 7, with a separator that will put all 5 letters words of the dictionary on the list_of_words.txt

import random


def word_separator(file_write, letters):
    reader = open("../../chapter-07/z_english_dictionary.txt")
    writer = open(file_write, 'w')
    for word in reader:
        word = word.strip().lower()
        if len(word) == letters:
            only_char = True
            for char in word:
                if not ('a' <= char <= 'z'):
                    only_char = False
                    break
            if only_char:
                writer.write(word + '\n')
    reader.close()
    writer.close()


word_separator('list_of_words.txt', 5)


def random_word(list_of_word):
    reader = open(list_of_word, 'r')
    words = reader.readlines()
    reader.close()
    selected = random.choice(words)
    return selected.strip().lower()


def check_word(secret, guess):
    leftovers = secret
    result = ["", "", "", "", ""]

    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "GREEN"
            leftovers = leftovers[:i] + "*" + leftovers[i + 1:]

    for i in range(5):
        if result[i] != "GREEN":
            letter = guess[i]
            if letter in leftovers:
                result[i] = "YELLOW"
                position = leftovers.find(letter)
                leftovers = leftovers[:position] + "*" + leftovers[position + 1:]
            else:
                result[i] = "GREY"

    return result


def wordle():
    secret = random_word("list_of_words.txt")
    won = False
    attempts = 0

    while attempts < 6:
        guess = input("Enter your 5-letter guess: ")

        if len(guess.strip()) != 5:
            print("Please enter a valid 5-letter word.")
            continue

        result = check_word(secret, guess.strip().lower())
        print(result)

        attempts += 1

        if result == ["GREEN", "GREEN", "GREEN", "GREEN", "GREEN"]:
            print("You've won the game!")
            won = True
            break

    if not won:
        print("You've lost the game!")
        print(f"The secret word was: {secret}")