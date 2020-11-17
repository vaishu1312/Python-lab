ch=input("Enter character: ")
c=ord(ch)
if 65<=c<=90:
    print("The character is in uppercase")
elif 97<=c<=122:
    print("The character is in lowercase")
elif 48<=c<=57:
    print("The character is a digit")
