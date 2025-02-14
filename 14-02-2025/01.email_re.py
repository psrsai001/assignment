import re

pat = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

pattern = re.compile(pat)

emails = [
    "simple@example.com",
    "very.common@example.com",
    "disposable.style.email.with+symbol@example.com",
    "other.email-with-hyphen@example.com",
    "user.name+tag+sorting@example.com",
    "admin@mailserver1",
    "user%example.com@example.org",
    "x@example.com",
    'very.unusual.@.unusual.com"@example.com',
    "example-indeed@strange-example.com",
    "admin@mailserver1",
    "user%example.com@example.org",
    "simple@example.com",
    "very.common@example.com",
    "disposable.style.email.with+symbol@example.com",
    "other.email-with-hyphen@example.com",
    "user.name+tag+sorting@example.com",
    "x@example.com",
    "example-indeed@strange-example.com",
]

for email in emails:
    matched = pattern.match(email)
    if matched:
        print("Valid email:", matched.group())
    else:
        print("Invalid email:", email)
