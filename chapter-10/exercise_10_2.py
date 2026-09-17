# Function to count if the str has repeated characters
def value_counts(string):
    counter = {} # create an empty dictionary
    for letter in string: # loop for each letter in the string
        counter[letter] = counter.get(letter, 0) + 1
        # for each letter get will return 0, but the code has the + 1, so, for each letter that the string has, it will
        # be store 'character': 1. When the character apper again, get will return 1, and the + 1 sum, giving 2 appearances
        # counter[letter] will simply record this count
    return counter # return the dictionary as value of the function


#print(value_counts('banana')) # {'b': 1, 'a': 3, 'n': 2}