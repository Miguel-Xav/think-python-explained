

# Function to create a dictionary with all the words in a respective given file (any language)
def create_dictionary(file):
    word_dict = {} # Create the dictionary
    reader = open(file) # Open the given file
    # Loop for each line in the file, store the word as key and 0 as value
    for line in reader:
        word_dict[line.strip()] = 0
    reader.close() # Close the reader for saving memory
    return word_dict # Return the dictionary as value of the function


def is_interlocking(word, word_dict):
    first = word[::2] # Make the first word of even characters, in python logic that starts counting on 0
    second = word[1::2] # Make the second word of odd characters, in python logic that starts counting on 0
    # Check if the two words are in the given dictionary and return if the given word is interlocked
    return first in word_dict and second in word_dict