import re

m = re.match(r"foo", "foo")
if m:
    print("1st")
    print(m.group())

m = re.match(r"foo", "The world is fooooool of morons")
if m:
    print(m.group())

m = re.search(r"foo", "The world is fooooool of morons")
if m:
    print("3rd")
    print(m.group())
