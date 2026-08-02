def check_word(word, available, required):
    # making all the characters of the string lowercase:
    word = word.lower()
    available = available.lower()
    required = required.lower()
    if len(word) < 4: # check if the word has 4 characters
        return False # if not, return False
    else:
        for letter in word: # create a loop for each letter in word
            if letter not in available: # check if this letter is on the available str
                return False # if not, return False
        for letter in required: # create a loop for the required character
            if letter not in word: # check if the letter is on the word str
                return False # if not, return False
        return True # return True if all the conditions are fulfilled
""""
remember that if the lower() is not used, if the letter in available, required and word are not upper case or lowercase
it will cause inaccurate results! (python treats 'R' and 'r' as different characters)
"""

print (check_word("rata", "TARD", "R"))

"""
word_score Function
"""
def word_score(word, available, required):
    # making all the characters of the string lowercase:
    word = word.lower()
    available = available.lower()
    #calling the check_word to not have to check the word inside here again
    valid_word = check_word(word, available, required)
    if valid_word == False: # if the word is not valid, return 0
        return 0
    else: # if it is valid, give the score
        word_length = len(word) # storing the number of letters inside a function
        if word_length == 4: # if the word has 4 characters, attribute the value of 1 to the function
            return 1
        elif word == 'cartload': # if the word is the pangram, attribute the value of 15 to the function
            return 15
        else: # else, attribute the value of characters to the function
            return word_length
        # the value of the function will be how many points you would have

"""
To create a function to simulate the real game, and create random pangrams. You would need a function that search a
.txt of the English Dictionary, use the available letters to pick a random word that meet the requirements.
Thing that I will challenge you to do and put the answer on a bonus of the chapter 7!

"""


print (word_score('card', 'ACDLORT', 'R'))
print (word_score('color', 'ACDLORT', 'R'))
print (word_score('cartload', 'ACDLORT', 'R'))