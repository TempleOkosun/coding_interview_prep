import time
import random


# 1.
# Reversing Strings
# Reversing a string in Python. Some implementations may be more appropriate for the test than others.


def reverse_string1(user_input):
    return user_input[::-1]  # The slice stmt means start at string length, end at position 0, move one step backward).


def reverse_string2(user_input):
    reversed_string = ''
    for character in user_input:
        reversed_string = character + reversed_string
    return reversed_string


def reverse_string3(user_input):
    return ''.join(reversed(input_str))


print('----------------------', "REVERSING STRINGS", '-----------------------')
print("Reversing String Function 1")
input_str = "I love programming in Python."
print("Input is: ", input_str, '|', " The Result is: ", reverse_string1(input_str), '\n')

print("Reversing String Function 2")
print("Input is: ", input_str, '|', " The Result is: ", reverse_string2(input_str), '\n')

print("Reversing String Function 3")
print("Input is: ", input_str, '|', " The Result is: ", reverse_string3(input_str), '\n')


# 2
# Palindrome Directions
# Given a string, return true if the string is a palindrome or not.
# Palindromes ae strings that form the same word if it is reversed. NB: Include space.

def palindrome(user_input):
    reversed_string = user_input[::-1]
    return user_input == reversed_string


print('----------------------', "STRING PALINDROME", '-----------------------')
input_str = "Doctor"
print("Input is: ", input_str, '|', " The Result is: ", palindrome(input_str))
input_str = "wow"
print("Input is: ", input_str, '|', " The Result is: ", palindrome(input_str), "\n")


# 3
# Reversing an Integer 15 === 51, 500 === 5, -15 === -51
def reverse_int1(user_input):
    signbit = 0
    if user_input > 0:
        signbit = 1
        reversed_string = str(user_input)[::-1]
    else:
        signbit = -1
        abs_value = user_input * signbit
        reversed_string = str(abs_value)[::-1]

    return int(reversed_string) * signbit


print('----------------------', "REVERSING INTEGERS", '-----------------------')
print("Reversing Integers Function 1")
user_input1 = 125
print("Input is: ", user_input1, '|', " The Result is: ", reverse_int1(user_input1))
user_input2 = -125
print("Input is: ", user_input2, '|', " The Result is: ", reverse_int1(user_input2))
user_input3 = 500
print("Input is: ", user_input3, '|', " The Result is: ", reverse_int1(user_input3))
user_input4 = -500
print("Input is: ", user_input4, '|', " The Result is: ", reverse_int1(user_input4), '\n')


def reverse_int2(user_input):
    input_to_string = str(user_input)
    if input_to_string.startswith("-"):
        reversed_int = "-" + input_to_string[1:][::-1]
    else:
        reversed_int = input_to_string[::-1]
    return int(reversed_int)


print("Reversing Integers Function 2")
user_input1 = 125
print("Input is: ", user_input1, '|', " The Result is: ", reverse_int2(user_input1))
user_input2 = -125
print("Input is: ", user_input2, '|', " The Result is: ", reverse_int2(user_input2))
user_input3 = 500
print("Input is: ", user_input3, '|', " The Result is: ", reverse_int2(user_input3))
user_input4 = -500
print("Input is: ", user_input4, '|', " The Result is: ", reverse_int2(user_input4), '\n')


# 4
# check if an integer is a palindrome
def int_palindrome(user_input):
    reversed_input = reverse_int1(user_input1)
    return reversed_input == user_input


print('----------------------', "INTEGER PALINDROME", '-----------------------')
user_input1 = 12321
print("Input is: ", user_input1, '|', " The Result is: ", int_palindrome(user_input1))
user_input2 = -125
print("Input is: ", user_input2, '|', " The Result is: ", int_palindrome(user_input2), '\n')


# 5
# Find the maximum occurring character in a string
def max_chars(user_input):
    char_map = {}
    for value in user_input:
        if value in char_map:
            char_map[value] = char_map[value] + 1
        else:
            char_map[value] = 1

    for key, value in char_map.items():
        max_chr_val = max(char_map.values())
        if value == max_chr_val:
            max_chr = key

    return max_chr, max_chr_val


print('----------------------', "FIND MAX CHARACTER", '-----------------------')
arr = "Hello World"
print("Input is:", arr, '|', 'Character with max occurrence is:', max_chars(arr)[0], 'Count=', max_chars(arr)[1], '\n')


# 6
# 7 Classical FizzBuzz
# Console log number 1 to n. But for multiples of 3 print Fizz, for multiples of 5 print Buzz and FizzBuzz for 3 and 5


def fizzbuzz(user_input):
    for number in range(1, user_input):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif (number % 5 == 0):
            print("Buzz")
        elif (number % 3 == 0):
            print("Fizz")
        else:
            print(number)


print('----------------------', "FIZZBUZZ", '-----------------------')
fizzbuzz_input = 35
print("Input is:", fizzbuzz_input, '|', 'Result is Below:')
print(fizzbuzz(fizzbuzz_input))


def fizzbuzzcrack(user_input):
    for number in range(1, user_input):
        if (number % 3 == 0) and (number % 7 == 0):
            print("FizzCrack")
        elif (number % 13 == 0):
            print("Bzz")
        elif (number % 7 == 0):
            print("Crack")
        elif (number % 5 == 0):
            print("Pop")
        elif (number % 3 == 0):
            print("Fizz")
        else:
            print(number)


print('----------------------', "FIZZBUZZCRACK", '-----------------------')
fizzbuzzcrack_input = 35
print("Input is:", fizzbuzzcrack_input, '|', 'Result is Below:')
print(fizzbuzzcrack(fizzbuzzcrack_input), '\n')


# 7
# List Chunker
def list_chunker_1(input_list, chunk_size):
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]


print('----------------------', "CHUNKING LIST INTO N SUBLISTS", '-----------------------')
print("Chunking Function 1")
input_list = ["A", 12, "Love", 67, 'Python']
size = 2
print("Input is:", input_list, '|', 'Result is Below:')
print(list(list_chunker_1(input_list, size)), '\n')


def list_chunker2(list_numbers, n):
    return [list_numbers[i: i + n] for i in range(0, len(list_numbers), n)]


print('Chunking Function 2')
l = ["A", 12, "Love", 67, 'Python']
s = 2
print("Input is:", l, '|', 'Result is Below:')
print(list_chunker2(l, s), '\n')


# 8
# Anagrams
# A string is an anagram of the other if it uses the same characters in the same quantity
# anagrams('rail safety', 'fairy tales') --> True. Consider characters only not special chararacters.
def anagrams(input1, input2):
    from collections import Counter
    input1 = input1.replace(" ", "").lower()
    input2 = input2.replace(" ", "").lower()

    return Counter(input1) == Counter(input2)


print('----------------------', "ANAGRAMS", '------------')
l = 'RAIL safety'
s = 'fairy TALES'
print("Inputs are:", l, '|', s)
print(anagrams(l, s), '\n')


# 9
# Converts the first character of each word to upper case
def capitalize(user_input):
    return user_input.title()


print('----------------------', "CAPITALIZE ", '------------')
sentence = 'rAIL safety'
print("Inputs is:", l, '|', 'The Result is:', capitalize(sentence), '\n')


# 10
def pyramids(n):
    for i in range(n):
        print(' ' * (n - i - 1) + (str('#') + ' ') * (i + 1))


print('----------------------', "PYRAMID ", '------------')
n = 4
print("Inputs is:", n, '|', 'The Result is:')
pyramids(n)


# 11
# Count Vowels
def vowel(my_str):
    str_input = my_str.lower()
    vowels = 'aeiou'
    vowel_counts = {}

    for vowel in vowels:
        if vowel in str_input:
            vowel_counts[vowel] = str_input.count(vowel)

    return vowel_counts, sum(vowel_counts.values())


def vowel_2(my_str_2):
    str_input = my_str_2.lower()
    vowels = 'aeiou'
    vowel_counts = {}
    for vowel in vowels:
        vowel_counts[vowel] = str_input.count(vowel)

    return vowel_counts, sum(vowel_counts.values())


print('----------------------', "FINDING VOWELS", '------------')
print(vowel("Hello World"), '\n')
print(vowel_2("Hello World"))


# 12
def spiral_matrix(matrix):
    result = []
    rows = len(matrix)
    topRow = 0
    btmRow = rows - 1
    leftCol = 0
    rightCol = len(matrix[0]) - 1

    if rows == 0:
        return result

    while topRow <= btmRow and leftCol <= rightCol:
        for i in range(leftCol, rightCol + 1):
            result.append(matrix[topRow][i])
        topRow += 1

        for i in range(topRow, btmRow + 1):
            result.append(matrix[i][rightCol])
        rightCol -= 1

        if topRow <= btmRow:
            for i in range(rightCol, leftCol - 1, -1):
                result.append(matrix[btmRow][i])
        btmRow -= 1

        if leftCol <= rightCol:
            for i in range(btmRow, topRow - 1, -1):
                result.append(matrix[i][leftCol])
        leftCol += 1

    return result


print('----------------------', "SPIRAL MATRIX", '------------')
matrix = [[1, 2, 3, 'a'], [4, 5, 6, 'b'], [7, 8, 9, 'c'], [10, 11, 12, 'd']]
print(spiral_matrix(matrix))


# 13
def fib_recursive(n):
    if n < 2:
        ans = n
    else:
        ans = fib_recursive(n - 1) + fib_recursive(n - 2)
    return ans


print('----------------------', "FIBONACCI SEQUENCE", '------------')
print('\n', "Fibonacci Function 1- Recursion")

n = 50
tic_fib1_a = time.perf_counter()
for i in range(n + 1):
    print(i, "=", fib_recursive(i))
tic_fib1_b = time.perf_counter()
fib1_time = tic_fib1_b - tic_fib1_a
fib1_time = round(fib1_time, 4)
print("\n")

fibonacci_cache = {}


def fib_manual_mem(n):
    if n in fibonacci_cache:
        ans = fibonacci_cache[n]
    elif n < 2:
        ans = n
    else:
        ans = fib_manual_mem(n - 1) + fib_manual_mem(n - 2)
        fibonacci_cache[n] = ans
    return ans


print('\n', "Fibonacci Function 2- Manual Memoization")
n = 50
tic_fib2_a = time.perf_counter()
for i in range(n + 1):
    print(i, '=', fib_manual_mem(i))
tic_fib2_b = time.perf_counter()
fib2_time = tic_fib2_b - tic_fib2_a
fib2_time = round(fib2_time, 4)

#
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib_inbuilt_mem(n):
    if n < 2:  # base case
        value = n
    else:
        value = fib_inbuilt_mem(n - 1) + fib_inbuilt_mem(n - 2)
    return value


print("Fibonacci Function 3- Inbuilt Memoization")
n = 50
tic_fib3_a = time.perf_counter()
for i in range(n + 1):
    print(i, '=', fib_inbuilt_mem(i))
tic_fib3_b = time.perf_counter()
fib3_time = tic_fib3_b - tic_fib3_a
fib3_time = round(fib3_time, 4)
print("\n")

print("It took Fibonacci Recursive function:", fib1_time, 'for n:', n)
print("It took Fibonacci Manual Memoized function:", fib2_time, 'for n:', n, 'time difference:',
      round(fib2_time - fib1_time), 4)
print("It took Fibonacci In-built Memoized function:", fib3_time, 'for n:', n, 'time difference:',
      fib3_time - fib2_time, '|', fib3_time - fib1_time)


def is_subset(l1, l2):
    temp = dict([(e, 1) for e in l2])
    for e in l1:
        if not (e in temp):
            return False
    return True


print(is_subset([1, 2, 4, 7, "a"], ["b", "a", 1, 2, 4, 7]))


def reverse_matrix(m):
    m.reverse()
    for row in m:
        row.reverse()

        m = [[1, 2], [3, 4], [5, 6]]
        reverse_matrix(m)
        print(m)
