def urlify(input_string, true_length):
    character_array = string_to_chars(input_string)
    i = 0
    while i < true_length:
        if character_array[i] == ' ':
            shift_characters_two_ahead(character_array, i, true_length)
            true_length = true_length + 2
        i = i + 1
    return character_array


def shift_characters_two_ahead(character_array, index, true_length):
    for i in reversed(range(true_length)):
        character_array[i+2] = character_array[i]
        if i == index:
            character_array[i] = '%'
            character_array[i+1] = '2'
            character_array[i+2] = '0'
            break


def string_to_chars(input_str: str):
    character_array = []

    for character in input_str:
        character_array.append(character)

    return character_array
