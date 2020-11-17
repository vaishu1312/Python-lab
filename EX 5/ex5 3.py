str1=input('enter a message ')
str2=''
key=int(input('enter key '))
for i in str1:
    code=ord(i)
    str2=str2+chr(code+key)
print(str2)
