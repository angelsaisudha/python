def compress_string(s):
    compressed_string= ""
    count = 1
    #iterate through the characters of the string
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
#if current character is the same as the previous one,increment
            count += 1
        else:
#if current characters is different , append the previous character
            compressed_string += s[i-1] + str(count)
            count = 1
#append the last character and count
    compressed_string += s[-1] + str(count)
    return compressed_string
#input the string
input_string = input("Enter a string:")
str1 =sorted(input_string)
#call the function to compress the string
result = compress_string(str1)
#print the compressed string
print("compressed string:",result)