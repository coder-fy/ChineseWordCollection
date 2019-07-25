import re

str = "\n  test     it \n"
new_str = re.sub(r"\s+", " ", str).strip()
print(new_str)