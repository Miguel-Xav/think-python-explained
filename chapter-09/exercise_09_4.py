# Function to reverse sentences
def reverse_sentence(sentence):
    words_list = sentence.split() # Create a list with words of the sentence given
    print(' '.join(reversed(words_list)).capitalize()) # print the reversed list with spaces and capitalized letters


reverse_sentence("Hello World") # World hello