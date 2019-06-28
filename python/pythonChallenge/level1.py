import string

before = 'abcdefghijklmnopqrstuvwxyz'
after = 'cdefghijklmnopqrstuvwxyzab'
st = "map"
b = st.maketrans(before,after)
print (st.translate(b))

# String : i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
# solve: ocr

# flag = ""
# for i in range(97,123):
#     flag += chr(i+2)
# print (flag)2