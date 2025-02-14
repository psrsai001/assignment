import re
from random import randint


def only_digits():
    pattern = r"^\d+$"
    st = "1"
    matched = re.match(pattern, st)
    if matched:
        print(matched.group())
    else:
        print("not matched")


def valid_date():
    pat = r"^(\d{2})\/(\d{2})\/(\d{4})$"
    matched = re.match(pat, "23/12/2000")
    if matched:
        print(matched.groups())
    print("not matched")


def extract_mails():
    pat = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]{2,4}"
    text = "my mail is mymail@gmail.com and my frnds mail is myfrnd@gmail.com"

    print(re.findall(pat, text))


def ings():
    pat = r"\b\w+ing\b"
    text = "raining daining swimming eating"
    print(re.findall(pat, text))


def valid_hex():
    pat = r"^(0x)?[0-9A-Fa-f]+$"
    text = "123FA"
    matched = re.match(pat, text)
    if matched:
        print(matched.span())
    else:
        print("not hex")


def max_list():
    lst = [randint(0, 9) for _ in range(11)]
    print(lst)
    print("Max:", max(lst))


def occurances():

    lst = [randint(0, 2) for _ in range(31)]
    print(lst)
    print("occurance of 0:", lst.count(0))
    print("occurance of 1:", lst.count(1))
    print("occurance of 2:", lst.count(2))


def remove_dup():
    lst = [randint(0, 2) for _ in range(31)]
    print(lst)
    print("deduped:", list(set(lst)))


def find_ind():

    lst = [randint(0, 21) for _ in range(31)]
    print(lst)
    print("first occurance of 0", lst.index(0))


def reverse():
    lst = [randint(0, 21) for _ in range(31)]
    lst.reverse()
    print(lst)


# only_digits()
# valid_date()
# extract_mails()
# ings()
