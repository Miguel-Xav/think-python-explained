# Function to reverse the word the book gave
def reverse_word(word):
    return ''.join(reversed(word))

# Function to know if a word is a palindrome
def is_palindrome(word):
    return word == reverse_word(word) # Check if the word is a palindrome

print(is_palindrome("noon")) # True

# Take all the palindromes with 7 characters in the English Dictionary and print
def is_palindrome_7char_file(file):
    reader = open(file)
    for line in reader: # Loop for each line/word
        word = line.strip() # Take blank spaces
        if len(word) >= 7 and is_palindrome(word): # Check if the word is a palindrome and has 7 characters
            print(word) # Print the word
    reader.close() # Close the reader for memory saving


is_palindrome_7char_file("../chapter-07/z_english_dictionary.txt")
