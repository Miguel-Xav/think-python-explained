def uses_only(word, available):
    # making all the character of the str on the parameter of the function lower case:
    word = word.lower()
    available = available.lower()
    for letter in word: # create a loop for each letter in word
        if letter not in available: # if the letter is not in available: return False
            return False
    return True # else: return True

""""
remember that if the lower() is not used, if the letter in available, required and word are not upper case or lowercase
it will cause inaccurate results! (python treats 'R' and 'r' as different characters)
"""

print (uses_only ("banana", "abn") )