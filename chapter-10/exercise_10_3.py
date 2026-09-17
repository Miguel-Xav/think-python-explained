# Function to check if a sequence (string or list) has duplicated characters
def has_duplicates(sequence):
    seen = {} # Create an empty dictionary
    for letter in sequence: # Loop for each character
        if letter in seen: # If the character already in the seen group
            return True # Return True (the word has duplicates)
        seen[letter] = True # Store the letter in the seen dictionary
    return False # Return False if the word doesn't have duplicates



print(has_duplicates('banana')) # True