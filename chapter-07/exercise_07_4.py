def uses_all(word, required):
    for letter in required.lower(): # traverses required
        if letter not in word.lower(): # if the letter in required is NOT in word:
            return False
    return True # else return True

print (uses_all ("banana", "abq"))