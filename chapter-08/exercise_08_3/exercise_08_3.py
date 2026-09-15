"""
Wordle in Python!
A function that you can play Wordle in Python
"""
# The book doesn't specify what list of words you will use to create the function, I will use the english dictionary
# file in the chapter 7, with a separator that will put all 5 letters words of the dictionary on the list_of_words.txt

import random # Library necessary to pick a random word in the list_of_words.txt


def word_separator(file_read, file_write, letters): # Simple function to separate words by quantity of char
    reader = open(file_read) # The variable that stores the file you want to read
    writer = open(file_write, 'w') # The variable that stores the file you want to write
    for word in reader:
        word = word.strip().lower()
        if len(word) == letters: # Checking if each word have the number of characters you want
            only_char = True # Check if are only alphabetical characters in the word
            for char in word: # loop to check if all the characters are alphabetical
                if not ('a' <= char <= 'z'):
                    only_char = False # if it doesn't, update the condition
                    break
            if only_char: # If the condition of only alphabetical characters are true:
                writer.write(word + '\n') # write that word and break the line (to not make a giant line)
    reader.close()
    writer.close() # close the reader and writer to save memory


word_separator('../../chapter-07/z_english_dictionary.txt', 'list_of_words.txt', 5)


def random_word(list_of_word): # Function to select a randon word from a .txt file
    reader = open(list_of_word, 'r')
    words = reader.readlines() # read all the lines of the file
    reader.close() # close the reader
    selected = random.choice(words) # select a random word
    return selected.strip().lower() # store the word as value of the function


def check_word(secret, guess): # Function to check the user guess
    leftovers = secret # Variable to keep track of the leftovers characters
    result = ["", "", "", "", ""] # Blank result

    for i in range(5): # Loop of 5 tries to check if the letter is green
        if guess[i] == secret[i]: # if the letter is the same, and it's in the same position ass the correct word:
            result[i] = "GREEN" # give the blank result the GREEN on the character position
            leftovers = leftovers[:i] + "*" + leftovers[i + 1:] # Update the leftovers characters

    for i in range(5): # Loop to check if the result is Yellow or Grey
        if result[i] != "GREEN": # If the letter is not GREEN
            letter = guess[i]
            if letter in leftovers: # Check all the leftovers
                result[i] = "YELLOW" # If it has the letter, but not on the same position, give YELLOW on the result
                position = leftovers.find(letter)
                leftovers = leftovers[:position] + "*" + leftovers[position + 1:] # Keep track of the leftovers
            else:
                result[i] = "GREY" #If it's not GREEN or Yellow, give GREY to result

    return result # Return the result of the guess as value of the function


def wordle(): # Function to play the Wordle Game
    secret = random_word("list_of_words.txt") # Calls the function to take a secret random word
    won = False # Won variable is False
    attempts = 0 # Variable to keep track of the attempts

    while attempts < 6: # While you have attempts
        guess = input("Enter your 5-letter guess: ") # Enter the user guess

        if len(guess.strip()) != 5: # If the guess not have 5 letters, tell to enter a valid word and not count an attempt
            print("Please enter a valid 5-letter word.")
            continue

        result = check_word(secret, guess.strip().lower()) # Use the check_word function to check the guess
        print(result) # print the result on the terminal

        attempts += 1 # count an attempt

        if result == ["GREEN", "GREEN", "GREEN", "GREEN", "GREEN"]: # if the result is all letters GREEN
            print("You've won the game!") # Tell the user he won the game
            won = True # Update the won status to True (if you don't do that will drop in the if statement to lose the game)
            break # Break the loop

    if not won: # If you take all attempts and the won status is False:
        print("You've lost the game!") # Tell the user he lost the game
        print(f"The secret word was: {secret}") # And tell the secret word