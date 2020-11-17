#simple calculator
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch=input("Enter choice: ")
if ch=='1' or ch=='2' or ch=='3' or ch=='4':
 n1=int(input("Enter first number: "))
 n2=int(input("Enter second number: ")) 
 if ch=='1':
    print(n1+n2)
 elif ch=='2':
    print(n1-n2)
 elif ch=='3':
    print(n1*n2)
 elif ch=='4':
    print(n1/n2)
else:
    print("Operation can't be performed")
    

