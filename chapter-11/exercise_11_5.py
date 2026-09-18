# Function to see how many character the two given words differ
def word_distance(word1, word2):
    counter = 0 # Counter to count the characters that differ

    word1_list = list(word1) # List with all character of word1 separated
    word2_list = list(word2) # List with all character of word2 separated

    for a, b in zip(word1_list, word2_list): # Loop for zip and make pairs
        if a != b: # If the pair has different letters:
            counter -= 1 # Takes -1 from the counter

    return counter # Return the counter

word_distance('salted', 'slated') # -2