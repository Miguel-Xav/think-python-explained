def uses_any(word, forbidden):
    for letter in word.lower(): # create a loop for each letter in word
        if letter in forbidden.lower(): # if the current character is forbidden
            return True # return True if the word uses any forbidden character
    return False # return False if the word didn't use any forbidden character

print(uses_any("banana", "xyz"))

