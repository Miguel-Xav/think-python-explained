
# Function to register all possible anagrams from a .txt file
def anagram_register(dictionary_file):
    dict_words = {} # Empty dictionary for all possibles anagrams of given file
    reader = open(dictionary_file) # Reader for read the file

    for line in reader: # Loop to each line of the file
        clean_line = line.strip() # Take off spaces and \n
        sorted_word = ''.join(sorted(clean_line)) # Sort the word alphabetically
        if sorted_word in dict_words: # Check if the sorted word already exists as key in dict_words
            if clean_line not in dict_words[sorted_word]: # If the unscrambled word is not as value of it alphabetical order:
                dict_words[sorted_word].append(clean_line) # Put the unscrambled word in the list of anagram
        else: # If the sorted word is not a key, create an item putting the sorted as key and unscrambled as value
            dict_words[sorted_word] = [clean_line]

    filtered_dict = {} # Filter for real anagrams (sorted_word contains all words on the list, not only real anagrams)
    for key, value in dict_words.items(): # Check if the value list has 2 items
        if len(value) >= 2:
            filtered_dict[key] = value # If it has, put the value list as item on the filtered_dict
    reader.close() # Close the reader for saving memory
    return filtered_dict # Return the filtered dictionary as value of the function

anagram_register("../chapter-07/z_english_dictionary.txt") # Return all english anagrams

# Function that give all possibles of anagrams to each item in the list
def anagram_from_list(list_of_words, dictionary_file):
    dict_words = anagram_register(dictionary_file) # Take all possible real anagrams from the given file
    list_of_anagrams = list() # Create an empty list to put the anagrams of the word you want to know

    for item in list_of_words: # A loop for each item in the list given
        sorted_word = ''.join(sorted(item)) # Take the alphabetical order of the word
        if sorted_word in dict_words: # See if it exists as key in the dictionary of the language
            list_of_anagrams.append(dict_words[sorted_word]) # Put all possible anagrams with that word in a list

    return list_of_anagrams



list_of_words = ['deltas', 'retainers', 'generating', 'resmelt']
english_dictionary_file = "../chapter-07/z_english_dictionary.txt"

anagram_from_list(list_of_words, english_dictionary_file)
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'stadle', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening', 'renegating']




