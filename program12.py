def sort_by_frequency(arr):
    frequency_dict = {}
    for element in arr:
        frequency_dict[element] = frequency_dict.get(element,0) + 1
    sorted_arr = sorted(arr, key = lambda x:(frequency_dict[x],x))
    return sorted_arr
t=int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int,input().split()))
    sorted_result = sort_by_frequency(elements)
    print(*sorted_result)