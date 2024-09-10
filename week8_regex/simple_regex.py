import re

result = re.search(
    r"[^a-zA-Z ]",
    "This is the sentene with. space kahekaSeRotonin",
)
print(result)

print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"o+l+", "gooollllldfish"))


def check_web_address(text):
    pattern = r"^\w+.+\.(\w+)$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True


def check_time(text):
    pattern = r"[1-9][0-2]?:[0-5][0-9]( )?[am|AM|pm|PM]"
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
print(check_time("6:02 am"))  # True
print(check_time("6:02km"))  # False


def contains_acronym(text):
    pattern = r"\([A-Z0-9][A-Za-z0-9]{1,}\)"
    result = re.search(pattern, text)
    return result != None


print(
    contains_acronym(
        "Instant messaging (IM) is a set of communication technologies used for text-based communication"
    )
)  # True
print(
    contains_acronym(
        "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"
    )
)  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(
    contains_acronym("PostScript is a fourth-generation programming language (4GL)")
)  # True
print(
    contains_acronym(
        "Have fun using a self-contained underwater breathing apparatus (Scuba)!"
    )
)  # True
