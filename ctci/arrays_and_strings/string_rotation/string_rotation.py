def string_rotation(input_string_1: str, input_string_2: str) -> bool:
    already_matched = False
    matched_at = 0
    j = 0
    for i in range(len(input_string_1)):
        if input_string_1[i] == input_string_2[j] and not already_matched:
            already_matched = True
            matched_at = i
            j += 1
        elif input_string_1[i] == input_string_2[j] and already_matched:
            j += 1
        elif input_string_1[i] != input_string_2[j] and already_matched:
            already_matched = False
            j = 0
        if i == len(input_string_1) - 1:
            if input_string_2[j:] in input_string_1[:matched_at] and \
                    len(input_string_2[j:]) == len(input_string_1[:matched_at]):
                return True
    return False

