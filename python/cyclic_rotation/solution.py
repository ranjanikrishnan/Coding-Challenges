def rotate_array(A,k):
    old = A
    new = [0] * len(A)
    for i in range(k):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new.copy()
    return new

A=[11,12,13,14]
k=1
rotated = rotate_array(A,k)
print(rotated)