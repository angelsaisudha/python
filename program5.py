def get_sum_second_largest(even_matrix,odd_matrix):
    #function to calculate the sum of second largest numbers from
    #check if even matrix has at least two elements
    if len(even_matrix) >=2:
        even_second_largest = even_matrix[-2]
    else:
        even_second_largest = float('-inf')
    #check if odd matrix has at least two elements
    if len(odd_matrix) >=2:
        odd_second_largest = odd_matrix[-2]
    else:
        odd_second_largest = float('-inf')
    return even_second_largest + odd_second_largest
size = int(input("Enter the size of array:"))
#input element of matrix
matrix = []
for i in range (size):
    element = int(input(f"Enter element at {i} index:"))
    matrix.append(element)
    #divide the matrix into even and odd sub matrices
even_matrix = matrix[::2]
odd_matrix = matrix[1::2]
even_matrix.sort()
odd_matrix.sort()
print(f"sorted even array:{even_matrix}")
print(f"sorted odd array:{odd_matrix}")
sum_second_largest = get_sum_second_largest(even_matrix,odd_matrix)
print(f"sum of second-largest numbers:{sum_second_largest}")