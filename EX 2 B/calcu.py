def calc():    
    ch=int(input("Enter choice: "))
    if ch==1 or ch==2 or ch==3 or ch==4:
     n1=int(input("Enter first number: "))
     n2=int(input("Enter second number: ")) 
     if ch==1:
        print(n1+n2)
     elif ch==2:
        print(n1-n2)
     elif ch==3:
        print(n1*n2)
     elif ch==4:
        print(n1/n2)
     print('1.Perform calculations')
     print('2.exit')
     ch=int(input("Enter choice: "))
     if ch==1:
        calc()    
     elif ch==2:
         pass
     else:
        print("Incorrect choice")
    else:
        print("Incorrect choice")
        calc()
        

print('1.Perform calculations')
print('2.exit')
ch=int(input("Enter choice: "))
if ch==1:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    calc()    
elif ch==2:
    pass
else:
    print("Incorrect choice")

