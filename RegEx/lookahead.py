import re

print("Without positive lookahead")
print(re.findall(r"(\w+)\svan Rossum", """
Guido van Rossum
Tim Peters
Alex Martelli
Just van Rossum
Raymond Hettinger
"""))
print("With positive lookahead")
print(re.findall(r"\w+(?= van Rossum)", """
Guido van Rossum
Tim Peters
Alex Martelli
Just van Rossum
Raymond Hettinger
"""))

print("With multi line negative lookahead")
print(re.findall(r"(?m)^\s+(?!noreply|postmaster)(\w+)",
"""
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
"""))
