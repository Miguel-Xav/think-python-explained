"""
In this exercise, I opted for a modular approach—both to allow the trigram search tool to work with any text file
and to save memory in the code—but this made it more complex to understand.
"""

# Import unicodedata as the book suggest to make the punc_marks dictionary
import unicodedata

# The load_file function, it reads the file only once throughout the entire code, making it faster and saving memory
def load_file(filename):
    reader = open(filename) # Create a reader
    lines = reader.readlines() # Store all the file lines in a list
    reader.close() # Close the reader
    return lines # Return the lines
# The clean_line is necessary because the line comes with '\n' and blank spaces

# "Why don't clean the lines in the load_file function?", because on the modular approach, you want the function to
# have fewer features possible. If you receive a file that is already clean, just don't pass the lines in the clean_line
# and this will prevent the information break

# The second_element function from the book
def second_element(t):
    return t[1]

# The clean_line function from the book
def clean_line(lines):
    cleaned = []

    for line in lines:
        cleaned.append(line.strip())

    return cleaned

# The split_line function from the book
def split_line(line):
    return line.replace('-', ' ').split()

# The used_punctuation function from the book
def used_punctuation(lines):
    punc_marks = {}

    for line in lines:
        for char in line:
            category = unicodedata.category(char)
            if category.startswith('P'):
                punc_marks[char] = 1
    return ''.join(punc_marks)

# The clean_word function take a word and clean all the punctuations from punc_marks and pass to lowercase
def clean_word(word, punctuation):
    return word.strip(punctuation).lower()

# The process word function from the book
def process_word(lines, punctuation):
    words = []

    for line in lines:
        for word in split_line(line):
            cleaned = clean_word(word, punctuation)
            if cleaned:
                words.append(cleaned)

    return words

# This function is the same as the count_bigram, but for trigrams. Using the process_trigram function
def count_trigram(trigram, trigram_counter):
    key = tuple(trigram)

    if key not in trigram_counter:
        trigram_counter[key] = 1
    else:
        trigram_counter[key] += 1

    return trigram_counter

# The process_trigram is the same as the process_word from the book, but the window is here
def process_trigram(words):
    window = []
    trigram_counter = {}

    for word in words:
        window.append(word)
        if len(window) == 3:
            count_trigram(window, trigram_counter)
            window.pop(0)

    return trigram_counter

# The print_most_common function from the book
def print_most_common(item, num=5):
    items = sorted(item.items(), key=second_element, reverse=True)

    for word, freq in items[:num]:
        print(freq, word, sep='\t')


# The orchestrator that will use all function to show all most_commn_trigram in a txt file
def most_common_trigram(filename):
    lines = load_file(filename) # Throughout the code, the file is read only this time.
    # lines stores all the lines from the file in a list

    punctuation = used_punctuation(lines) # Use the list of lines to register all the punctuation in the file
    words = process_word(lines, punctuation) # Separate all the list of lines in list of words
    trigram_counter = process_trigram(words) # Use the words list to encounter trigrams
    print_most_common(trigram_counter) # Use the print_most_common function to print the most commons trigrams

most_common_trigram('pg43.txt') # Call the function with the file you want it to read


