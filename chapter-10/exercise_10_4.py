# Importing the value_counts function of exercise_10_2
from exercise_10_2 import value_counts



def find_repeats(dictionary):
    counter = {} # Create an empty dictionary for counting the values of the dictionary of the parameter
    for key in dictionary: # For each key in dictionary:
        value = dictionary[key] # store the value (who was caught with the key) in the variable value
        if value > 1: # If the variable is > 1:
            counter[key] = value # It will store the key and its respective value in the counter dictionary
    return counter # Return the counter dictionary as value of the function


result = value_counts("banana")
print(find_repeats(result)) # {'a': 3, 'n': 2}
