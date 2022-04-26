def permutation_of_palindrome(input_string):
    input_string = input_string.lower().replace(' ', '')
    input_string_characters = {}
    count_odd = 0
    for i in input_string:
        if i in input_string_characters:
            input_string_characters[i] = input_string_characters[i] + 1
        else:
            input_string_characters[i] = 1
    for value in input_string_characters.values():
        if value % 2 != 0:
            count_odd = count_odd + 1
            if count_odd > 1:
                return False
        # if value % 2 == 0:
        #     continue
        # else:
        #     count_odd = count_odd + 1
    return True
