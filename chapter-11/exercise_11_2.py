# letter_map given by the book
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

# Function to shift words in the alphabet based on how many steps you want
def shift_word(string, step):
    shifted_word = "" # Empty shifted word
    for char in string: # Loop for each character in string
        if char in letter_map: # If the character is a key in letter_map dictionary:
            current_value = letter_map[char] # Get it's current value on the alphabet (letter_map)
            new_value = (current_value + step) % 26 # Set the new value to the step you want
            # To shift Z back to 0, you want to use the module operator
            # If the X < 26, the count result on X. When Z achieve 26 (on step = 1) or any higher number,
            # the rest is the leftover (27 % 26 = 1, z = b, etc.)

            for key, value in letter_map.items(): # Loop to find the letter in the letter_map based on the new_value
                if value == new_value: # When the loop find the key (letter) that corresponds on the value:
                    shifted_word += key # Add the letter based on the letter_map key
                    break
    return shifted_word


shift_word('banana', 2) # dcpcpc

