def duplicate_characters(input_string):
    characters_of_input_string = {}
    for character in input_string:
        if character in characters_of_input_string:
            return True
        characters_of_input_string[character] = character
    return False
