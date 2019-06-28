txt = open('level2.txt', 'r')
data = txt.read()

flag = ""
for i in data:
    if i.isalpha():
        flag += i
print (flag)