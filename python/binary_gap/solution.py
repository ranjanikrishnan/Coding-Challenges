def binary_gap(n):
    xs = bin(n)[2:].strip('0').split('1')
    return max([len(x) for x in xs])


if __name__ == '__main__':
    n = int(input())
    gap = binary_gap(n)
    print(gap)