import re

print(re.findall(r"car", "carry the barcardi to the car"))

g = re.finditer(r"(th\w+) and (th\w+)", "This and that", re.IGNORECASE)
i = g.next()
print(i.groups())
