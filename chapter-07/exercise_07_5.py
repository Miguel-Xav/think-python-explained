def check_word(word, available, required):
    if len(word) < 4: # check if the word has 4 characters
        return False # if not, return False
    else:
        for letter in word.lower(): # create a loop for each letter in word
            if letter not in available.lower(): # check if this letter is on the available str
                return False # if not, return False
        for letter in required.lower(): # create a loop for the required character
            if letter not in word.lower(): # check if the letter is on the word str
                return False # if not, return False
        return True # return True if all the conditions are fulfilled
""""
remember that if the lower() is not used, if the letter in available, required and word are not upper case or lowercase
it will cause inaccurate results! (python treats 'R' and 'r' as different characters)
"""

print (check_word("rata", "TARD", "R"))