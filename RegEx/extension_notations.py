import re

print("Without ignore case")
print(re.findall(r"yes", "yes? Yes. YES!!"))

print("With ignore case extension notation")
print(re.findall(r"(?i)yes", "yes? Yes. YES!!"))

print("With ignore case")
print(re.findall(r"(?i)th\w+", "The quickest way is through this tunnel."))

print("With ignore case and multi line")
print(re.findall(r"(?im)(^th[\w ]+)", """This line is first,
another line,
that line, it's the best
"""))

print("Without DOTALL")
print(re.findall(r"th.+", """
The first line
the second line
the third line
"""))

print("With DOTALL")
print(re.findall(r"(?s)th.+", """
The first line
the second line
the third line
"""))

# if you want to group some regex but don't want to save for future use, use (?:)

print("With P<>")
print(re.search(r"\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})", "(800) 555-1212").groupdict())
