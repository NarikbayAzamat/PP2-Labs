import re

with open('row.txt', 'r') as file:
    data = file.read()

x = re.search('a.*b$', data)
print(x)