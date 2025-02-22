def palindrome():
    st = input("Enter a string: ")
    if st == st[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
