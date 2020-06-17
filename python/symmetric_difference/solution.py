# https://www.hackerrank.com/challenges/symmetric-difference/problem


def find_symmetric_diff(list_m, list_n):
    set_m = set(list_m)
    set_n = set(list_n)
    symmetric_diff = set_m.symmetric_difference(set_n)
    for value in sorted(symmetric_diff):
        print(value)


if __name__ == '__main__':
    num_values_m = int(input())
    list_m = list(map(int, input().split()))
    num_values_n = int(input())
    list_n = list(map(int, input().split()))
    find_symmetric_diff(list_m, list_n)
