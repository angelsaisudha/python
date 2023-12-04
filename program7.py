def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = A[i]
def rearrangeArray(A):
    for i in range(1,len(A),2):
        if A[i - 1] > A[i]:
            swap(A, i - 1, i)
        if i + 1 < len(A) and A[i + 1] > A[i]:
            swap (A,i + 1, i)
A = [9,6,8,3,2]
rearrangeArray(A)
print(A)