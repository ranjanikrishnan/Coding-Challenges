def one_away(input_string_1: str, input_string_2: str) -> bool:
    len_string_1 = len(input_string_1)
    len_string_2 = len(input_string_2)
    i = 0
    j = 0
    edited = False
    if abs(len_string_1 - len_string_2) > 1:
        return False
    while i < len_string_1 and j < len_string_2:
        if input_string_1[i] == input_string_2[j]:
            i = i + 1
            j = j + 1
        elif not edited:
            edited = True
            if len_string_1 == len_string_2:  # assume a string replacement
                i = i + 1
                j = j + 1
            elif len_string_1 < len_string_2:  # one extra character at j
                j = j + 1
            elif len_string_1 > len_string_2:  # one extra character at i
                i = i + 1
        else:
            return False
    return True



