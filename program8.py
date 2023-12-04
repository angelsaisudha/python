def reorder(A):
    k = 0
    for i in A:
        if i:
            A[k] = i
            k = k + 1
    for i in range (k,len(A)):
        A[i] = 0
A = [6,0,8,2,3,0,4,1]
reorder(A)
print(A)