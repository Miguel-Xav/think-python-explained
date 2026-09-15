# Function to take each line of a .txt file into a list object
def file_to_list(file):
    reader = open(file)
    words_list = [] # Create an empty list
    for line in reader: # For each line in the file
        words_list.append(line.strip()) # Put the str in the list as an object
    reader.close() # Close the reader for saving memory
    return words_list # Return the list as the function value

# Function to tell the total length of a list, grouping the str objects and counting how many characters it has
def total_length(str_list):
    giant_str = ''.join(str_list) # Group the str objects of the list in one giant string
    return len(giant_str) # Return the value of the string (how many characters) as the value of the function