# given two strings, write a method to determine if one is a permutation of the other

def string_permutation_one(string_1, string_2):
    sorted_string_1 = sorted(string_1)
    sorted_string_2 = sorted(string_2)
    if sorted_string_1 == sorted_string_2:
        return True
    return False


def string_permutation_two(string_1, string_2):
    string_1_characters = {}
    string_1_count = 1
    string_2_count = 1
    for character in string_1:
        print(character)
        if character in string_1_characters:
            string_1_characters[character] = [string_1_count+1]
        else:
            string_1_characters[character] = [string_1_count]

    for character in string_2:
        if character in string_1_characters:
            string_1_characters[character].append(string_2_count)
        else:
            return False

    for value in string_1_characters.values():
        print(value)
        if len(value) != 2:
            return False
        elif value[0] != value[1]:
            return False
        return True


