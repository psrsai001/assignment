import re


def start_with_a():
    pat = r"^a+"
    pattern = re.compile(pat)
    strings = ["avacado", "apple", "banana", "pine"]
    for st in strings:
        matched = pattern.match(st)
        if matched:
            print("Matched:", matched.group(), "in", st)
        else:
            print("Not matched:", st)


def match_all_digits():
    pat = r"\d+"
    pattern = re.compile(pat)
    st = "my phone number is 1231231231 and dob is 23-05-2000"
    matched = pattern.findall(st)
    print(matched)


def check_if_alpha():
    pat = r"\d+"
    pattern = re.compile(pat)
    st = "this is my string without numbers"
    matched = pattern.findall(st)
    if matched:
        print("string contain numbers")
    else:
        print("String does not contain numbers")


def all_words():
    pat = r"\b[a-zA-z]+\b"
    pattern = re.compile(pat)
    st = "my phone number is 1231231231 and dob is 23-05-2000"
    matched = pattern.findall(st)
    print("all words", matched)


def validate_email():
    pat = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]{2,4}$"
    pattern = re.compile(pat)
    emails = ["valid@gmail.com", "invalid@mail", "another+mail@with_plus.com"]
    for email in emails:
        matched = pattern.match(email)
        if matched:
            print("Matched:", matched.group(), "in", email)
        else:
            print("Not matched:", email)


def ends_with_com():
    pat = r".*\.com$"
    pattern = re.compile(pat)
    emails = [".com", "valid@gmail.com", "invalid@mail", "another+mail@with_plus.com"]
    for email in emails:
        matched = pattern.match(email)
        if matched:
            print("Matched:", matched.group(), "in", email)
        else:
            print("Not matched:", email)


def replace_space_with_hyphens():
    pat = r"\s"
    st = "my phone number is 1231231231 and dob is 23-05-2000"
    matched = re.sub(pat, "-", st)
    print("replaced space:", matched)


def year_from_date():
    pat = r"[0-9]{4}"
    date = "01-02-2005"
    matched = re.search(pat, date)
    if matched:
        print(matched.group())
    else:
        print("not a valid date")


def valid_number():
    pat = r"^-?[0-9]+(\.[0-9]+)?$"
    nums = ["a3a", "3.14", "-3.14", "abc", "3", "-3"]
    for num in nums:
        matched = re.search(pat, num)
        if matched:
            print(matched.group())
        else:
            print("not a valid number", num)


def repeated_chars():
    pat = r"(.)\1"
    st = "hello world www"
    matched = re.findall(pat, st)
    print(matched)


start_with_a()
# match_all_digits()
# check_if_alpha()
# all_words()
# validate_email()
# ends_with_com()
# replace_space_with_hyphens()
# year_from_date()
# valid_number()
# repeated_chars()
