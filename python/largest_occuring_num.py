def largest_occuring_number(input_array):
    n = len(input_array)
    temp = input_array[0]
    count = 1
    for i in range(1, n):
        if input_array[i] == temp:
            count = count + 1
        else:
            count = count - 1
            temp = input_array[i]
            count = 1
    print(f"Answer: {temp}")


if __name__ == '__main__':
    test_array = [1,3,1,4]
    sorted_test_array = test_array.sort()
    largest_occuring_number(test_array)
