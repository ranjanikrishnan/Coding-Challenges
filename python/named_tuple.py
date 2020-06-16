# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

import collections


(n, columns) = (int(input()), input(). split())
Student = collections.namedtuple('Student', columns)
marks = [int(Student._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks)/len(marks))
