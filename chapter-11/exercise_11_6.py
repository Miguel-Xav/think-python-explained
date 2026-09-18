# All metathesis pairs are anagrams to! So I will reutilize the anagram functions from exercise_11_4
import exercise_11_4
# And I will the word_distance to see if the word are only -1 character different
import exercise_11_5


# Function to find all metathesis pairs from a given list of words and dictionary file
def metathesis_encounter(list_of_words, file):
    list_of_anagrams = exercise_11_4.anagram_from_list(list_of_words, file)  # List with all anagram groups found
    metathesis_pairs = []  # List to store the valid metathesis pairs

    for group in list_of_anagrams:  # Loop through each anagram group
        for i in range(len(group)):  # Loop to get the first word index
            for j in range(i + 1, len(group)):  # Loop to get the second word index without duplicates
                w1 = group[i]  # First word of the pair
                w2 = group[j]  # Second word of the pair

                distance = exercise_11_5.word_distance(w1, w2)  # Distance between the two words

                if distance == -2:  # If the distance is -2 (two character differences):
                    metathesis_pairs.append((w1, w2))  # Adds the pair to the metathesis list

    return metathesis_pairs  # Return the list of metathesis pairs



