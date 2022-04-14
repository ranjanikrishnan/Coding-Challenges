# given two strings, write a method to determine if one is a permutation of the other

def string_permutation(string_1, string_2):
    sorted_string_1 = sorted(string_1)
    sorted_string_2 = sorted(string_2)
    if sorted_string_1 == sorted_string_2:
        return True
    return False

