def find_largest_number(numbers):
    numbers_as_strings = list(map(str,numbers))
    numbers_as_strings.sort(reverse=True)
    result = ''.join(numbers_as_strings)
    return int(result) if '.' not in result else float(result)
integer_numbers = [93,68,721,6]
largest_integer = find_largest_number(integer_numbers)
print("largest integer:",largest_integer)