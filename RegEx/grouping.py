import re

m = re.match(r"(\w+)\.\w+@\w+\.com", "kaushik.sekar@wipro.com")
if m:
    print(m.group(1))
