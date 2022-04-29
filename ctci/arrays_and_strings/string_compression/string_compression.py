def string_compression(input_string: str) -> str:
    len_input_string = len(input_string)
    string_list = []
    character_count = 0
    string_list_index = 0
    for i in range(len_input_string):
        if i == 0:
            character_count += 1
            continue

        previous = input_string[i - 1]
        if previous == input_string[i]:
            character_count += 1
        elif previous != input_string[i]:
            string_list.insert(string_list_index, previous)
            string_list.insert(string_list_index + 1, str(character_count))
            string_list_index = string_list_index + 2
            character_count = 1
        if i == len_input_string - 1:
            string_list.insert(string_list_index, previous)
            string_list.insert(string_list_index + 1, str(character_count))
            if len(string_list) >= len_input_string:
                return input_string
    return ''.join([character for character in string_list])


