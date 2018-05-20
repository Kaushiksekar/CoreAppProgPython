import re

m = re.search(r"\bthe", "bite the dog")
if m:
    print("1st")
    print(m.group())

m = re.search(r"\bthe", "bitethe dog")
if m:
    print("2nd")
    print(m.group())

m = re.search(r"the\b", "bitethe dog")
if m:
    print("3rd")
    print(m.group())
