import numpy


def min_max():
    N, M = map(int, input().split())
    A = numpy.array([input().split() for _ in range(N)], int)
    return numpy.max(numpy.min(A, axis=1), axis=0)


if __name__ == '__main__':
    min_max_value = min_max()
    print(min_max_value)
