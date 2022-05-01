# # Examples: Given A=6, B=1 and C=1, your function may return "aabaacaa". Note that "aacaabaa" would also be correct
#
def can_append(input_str, char):
    if len(input_str) >= 2 and input_str[len(input_str)-1] == char and input_str[len(input_str)-2] == char:
        return False
    return True


def can_prepend(input_str, char):
    if len(input_str) >= 2 and input_str[0] == char and input_str[1] == char:
        return False
    return True


def position_to_add_within(input_str, char):
    # input_str = 'aabcaa'
    # char = 'a'
    for index, value in enumerate(input_str):
        print(index, value)
        can_add_within = True
        # todo: left 2 a or right 2 a then false, left one a and right one a then false
        if (input_str[index] == char and input_str[index-1] == char) or (input_str[index] == char and input_str[index+1] == char):
            can_add_within = False
        if input_str[index+1] == char and input_str[index-1] == char:
            can_add_within = False
        if input_str[index-1] == char and input_str[index-2] == char:
            can_add_within = False
        if can_add_within:
            return index


def solution(int_a, int_b, int_c):
    count_a = int_a
    count_b = int_b
    count_c = int_c
    total = int_a+int_b+int_c
    output = ''
    for i in range(total):
        for i in range(int_a):
            if can_append(output, 'a') and count_a>0:
                output = (output+'a').strip()
                count_a = count_a - 1
            if can_prepend(output, 'a') and count_a>0:
                output = ('a'+output).strip()
                count_a = count_a - 1
            # elif count_a>0 and len(output)>2:
            #     position = position_to_add_within(output, 'a')
            #     output = output[:position] + 'a' + output[position+1:].strip()
            #     count_a = count_a - 1
        for i in range(int_b):
            if can_append(output, 'b') and count_b>0:
                output = (output+'b').strip()
                count_b = count_b - 1
            elif can_prepend(output, 'b') and count_b>0:
                output = ('b'+output).strip()
                count_b = count_b - 1
            # if count_b>0 and len(output)>2:
            #     position = position_to_add_within(output, 'b')
            #     output = output[:position] + 'b' + output[position+1:].strip()
            #     count_b = count_b - 1
        for i in range(int_c):
            if can_append(output, 'c') and count_c>0:
                output = (output+'c').strip()
                count_c = count_c - 1
            elif can_prepend(output, 'c') and count_c>0:
                output = ('c'+output).strip()
                count_c = count_c - 1
            # if count_c>0 and len(output)>2:
            #     position = position_to_add_within(output, 'c')
            #     output = output[:position] + 'c' + output[position+1:].strip()
            #     count_c = count_c - 1
    print(output)
    return output


class Solution:
    def longest_diverse_string(self, a, b, c):
        count_a = 0
        count_b = 0
        count_c = 0
        generated_result = []
        for i in range(a+b+c):
            max_count = max(a, b, c)
            if (a==max_count and count_a < 2) or (count_b==2 and a>=1) or (count_c==2 and a>=1):
                generated_result.append('a')
                count_a = count_a+1
                a = a - 1
                count_b = 0
                count_c = 0
            elif (b==max_count and count_b < 2) or (count_a==2 and b>=1) or (count_c==2 and b >=1):
                generated_result.append('b')
                b = b - 1
                count_b = count_b + 1
                count_a=0
                count_c=0
            elif (c==max_count and count_c <2) or (count_a==2 and c>=1) or (count_b==2 and c>=1):
                generated_result.append('c')
                c = c -1
                count_c = count_c+1
                count_a=0
                count_b=0
        return "".join(generated_result)




