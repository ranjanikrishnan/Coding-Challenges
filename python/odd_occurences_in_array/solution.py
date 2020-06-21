def odd_occurences(A):
    print(A)
    for x in A:
        if A.count(x) == 1:
            print(x)


A = [9,3,9,3,9,7,9] 
odd_occurences(A)