def num_of_vowels():
    st = input("enter string: ")

    vowels = "aeiouAEIOU"
    count = 0
    for letter in st:
        if letter in vowels:
            count += 1
    print("Vowel count", count)
