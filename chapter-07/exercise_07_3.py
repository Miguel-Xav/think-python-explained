def uses_only(word, available):
    for letter in word.lower(): # create a loop for each letter in word
        if letter not in available.lower(): # if the letter is not in available: return False
            return False
    return True # else: return True

print (uses_only ("banana", "abn") )