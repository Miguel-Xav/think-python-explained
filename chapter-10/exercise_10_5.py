#import value_counts function from exercise_10_2
from exercise_10_2 import value_counts

def add_counters(dictionary1, dictionary2):
    combined = {} # Create an empty dictionary to combine the two from the function parameter
    #Loop to put each key (letters, not the values) from dictionary1 in combined
    for key in dictionary1:
        combined[key] = dictionary1[key]

    # Loop to put in combined, the sum from each key of dict1 and dict2
    for key in dictionary2:
        combined[key] = combined.get(key, 0) + dictionary2[key]
    # .get() return the value of the key

    return combined # Return the value of combined to the value of the function




value1 = value_counts("banana")
value2 = value_counts("peanut")

print(add_counters(value1, value2))