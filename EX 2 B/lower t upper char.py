ch=input("Enter character: ")
c=ord(ch)
if 65<=c<=90:
    print("Uppercase to lowercase")
    c=c+32
    char=chr(c)
    print("Character is now:",char)
elif 97<=c<=122:
    print("Lower case to uppercase")
    c=c-32
    char=chr(c)
    print("Character is now:",char)
else:
    print("Not an alphabet")
    
