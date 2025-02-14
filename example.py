def reverse_num(n):
    reversed = 0
    while n > 0:
        digit = n % 10
        reversed = reversed * 10 + digit
        n //= 10
    return reversed


def add(x, y):
    return x + y


# 1. Print "Hello, World!" in Python.
def hello():
    print("Hello, World!")


# 2. Write a program to swap two variables.
def swap():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    a, b = b, a


# 3. Find the largest of three numbers.


def largest_of_3_numbers():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))
    print("max:", max(a, b, c))


# 4. Check if a number is even or odd.
def even_odd():
    a = int(input("enter a: "))
    if a & 1 == 0:
        print("even")
    else:
        print("odd")


# 5. Reverse a string without using built-in functions.
def rev_string():
    st = input("Enter a string: ")
    print(st[::-1])


# 6. Find the factorial of a number.


def fact():
    n = int(input("Enter a number: "))
    res = n
    for i in range(2, n):
        res *= i
    print("Factorial:", res)


# 7. Generate a Fibonacci sequence up to n terms.
def fib():
    n = int(input("Enter a number: "))
    a = 0
    b = 1

    if n == 1:
        print(a)
        return
    if n == 2:
        print(a, b)
        return
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# 8. Check if a number is prime.


def is_prime():

    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not prime")
        return
    if n == 2:
        print("Prime")
        return
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Not Prime")
            return
        i += 1
    print("Prime")


# 9. Find the sum of digits of a number.
def sum_digits():
    n = int(input("Enter a number: "))
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    print("Sum of digits:", res)


# 10. Calculate the area of a circle given the radius.
def area_circle():
    r = int(input("Enter radius: "))
    print("Circle area:", 3.14 * r * r)


# Lists and Tuples
#
# 11. Find the largest element in a list.
def largest_ele_in_list():
    lst = list(map(int, input("enter space seperated numbers for list: ").split(" ")))
    print("Max element:", max(lst))


# 12. Remove duplicates from a list.
def remove_dups():
    lst = list(map(int, input("enter space seperated numbers for list: ").split(" ")))
    non_dup = set(lst)
    print("Non dups: ", non_dup)


# 13. Count the frequency of elements in a list.
def freq():
    lst = list(map(int, input("enter space seperated numbers for list: ").split(" ")))
    counter = {}
    for ele in lst:
        if ele in counter:
            counter[ele] += 1
        else:
            counter[ele] = 1

    for k, v in counter.items():
        print(k, "->", v)


def num_of_vowels():
    st = input("enter string: ")

    vowels = "aeiouAEIOU"
    count = 0
    for letter in st:
        if letter in vowels:
            count += 1
    print("Vowel count", count)


def palindrome():
    st = input("Enter a string: ")
    if st == st[::-1]:
        print("palindrome")
    else:
        print("not palindrome")


# 14. Find the second largest number in a list.
def second_largest():
    lst = list(map(int, input("enter space seperated numbers for list: ").split(" ")))
    fst = lst[0]
    sec = -1
    for ele in lst:
        if ele > fst:
            sec = fst
            fst = ele
        if ele > sec:
            sec = ele
    print("Second largest in list:", sec)


# 15. Reverse a list without using built-in functions.
def reverse_list():
    lst = list(map(int, input("enter space seperated numbers for list: ").split(" ")))
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    print("reversed:", lst)


# 16. Sort a list without using sort().
#
#
# 17. Merge two sorted lists.
#
#
# 18. Find the common elements in two lists.
#
#
# 19. Rotate a list by k positions.
#
#
# 20. Find pairs in a list whose sum is equal to a given number.
#
#
#
# Strings
#
# 21. Check if a string is a palindrome.
#
#
# 22. Count vowels and consonants in a string.
#
#
# 23. Find the longest word in a sentence.
#
#
# 24. Remove special characters from a string.
#
#
# 25. Find all permutations of a given string.
#
#
#
# Dictionaries and Sets
#
# 26. Merge two dictionaries.
#
#
# 27. Find the key with the maximum value in a dictionary.
#
#
# 28. Count occurrences of words in a given text.
#
#
# 29. Convert two lists into a dictionary.
#
#
# 30. Remove duplicate elements from a set.
#
#
#
# Functions
#
# 31. Write a function to check if a number is an Armstrong number.
#
#

# 32. Implement a function to check if a string is an an

while True:
    is_prime()
