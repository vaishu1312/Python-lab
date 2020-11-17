M1=int(input("Enter marks obtained in English: "))
M2=int(input("Enter marks obtained in Maths: "))
M3=int(input("Enter marks obtained in Science: "))
M4=int(input("Enter marks obtained in Tamil: "))
A=((M1+M2+M3+M4)/4)
if A>=90:
  G='A'
elif  A>=80:
  G='B'  
elif  A>=70:
  G='C'
elif  A>=60:
  G='D'
else:
  G='E'
print("Grade is:", G)
