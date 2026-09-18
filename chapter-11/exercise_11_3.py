
def most_frequent_letters(string):
    counter = {}
    for character in string:
        counter[character] = counter.get(character, 0) + 1

    # Create an empty variable for items in counter
    dict_items = counter.items()
    # Create a function to get value of the character in the sorted dictionary
    def get_value(x):
        return x[1] # Return the value of X key

    sorted_items = sorted(dict_items, key=get_value, reverse=True)
    # A list for all the values of the dictionary sorted
    sorted_counter = dict(sorted_items) # Put the sorted values into a dictionary
    return sorted_counter # Return the sorted dictionary as value of the function

most_frequent_letters("banana") # {'a': 3, 'n': 2, 'b': 1}