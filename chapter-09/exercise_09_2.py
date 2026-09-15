
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)
# If the alphabetical order of string1 == string2, they are anagrams. So, return True to te value of the function.
# If not, return False


print(is_anagram("stop", "spot")) # True
print(is_anagram("stop", "peanut"))# False