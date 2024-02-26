import re

with open("row.txt", "r") as file:
    data = file.read()

x = re.findall("[a-z]+\_{1}")
print(x)