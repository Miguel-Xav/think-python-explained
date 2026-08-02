def uses_all(word, required):
    # making all the character of the str on the parameter of the function lower case:
    word = word.lower()
    required = required.lower()
    for letter in required: # traverses required
        if letter not in word: # if the letter in required is NOT in word:
            return False
    return True # else return True

""""
remember that if the lower() is not used, if the letter in available, required and word are not upper case or lowercase
it will cause inaccurate results! (python treats 'R' and 'r' as different characters)
"""

print (uses_all ("banana", "abq"))