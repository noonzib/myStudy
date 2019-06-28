import re

code = open("level3.txt", 'r')

data = code.read()
info = []

p=re.compile("[a-z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]+")
result = p.findall(data)

q=re.compile("[A-Z]{3}[a-z]{1}[A-Z]{3}")
r=re.compile("[a-z]")

result = "".join(result)
result = q.findall(result)
result = "".join(result)
result = r.findall(result)

print(result)
