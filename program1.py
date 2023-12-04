def count_preety_numbers(l,r):
    preety_count=0
    #iterate through the range and count preety numbers
    for num in range(l,r+1):
        last_digit=num%10
        if last_digit ==5:
            preety_count +=1
    return preety_count
    #input the number of test cases
t=int(input())
#process each test case
for _ in range(t):
    #input the range L and R for each test case
    l,r = map(int,input().split())
    #call the function to count pretty numbers in the given range
    result = count_preety_numbers(l,r)
    #print the result for each test case
    print(result)
