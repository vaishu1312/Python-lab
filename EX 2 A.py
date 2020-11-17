#to add two nos
n1=int(input('enter first no '))
n2=int(input('enter second no '))
sum=n1+n2
print('the sum of ',n1 ,'and ',n2 ,'is ',sum)

#area of triangle
b=int(input('enter base '))
h=int(input('enter height '))
area=0.5*b*h
print('the area of the triangle is ',area)

#square root
n = int(input('Enter a number: '))
sqrt = n** 0.5
print('The square root of ',n ,'is ',sqrt)

#quadratic eqn solution
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = (b**2) - (4*a*c)
r1 = (-b+(d**0.5))/(2*a)
r2 = (-b-(d**0.5))/(2*a) 
print('The roots are ',r1 ,'and ',r2)

#fahrenheit to celsius
f=float(input('enter temperature in fahrenheit '))
c=(5/9)*(f-32)
print('the temperature in celsius is ',c)

#quotient and remainder
d1=int(input('enter dividend '))
d2=int(input('enter divisor '))
q=d1//d2
r=d1%d2
print('the quotient is ',q)
print('the remainder is ',r)

#swap two nos
a = int(input('Enter a number: '))
b= int(input('Enter another number: '))
temp=a
a = b
b= temp 
print('The value of a after swapping: ',a)
print('The value of b after swapping: ',b)

#average of 3 marks
m1 = float(input('Enter marksi n eng: '))
m2 = float(input('Enter marks in maths: '))
m3 = float(input('Enter marks in science: '))
avg=(m1+m2+m3)/3
print('the average of three marks is ',avg)

#simple interest
p= float(input('Enter principal: '))
n = int(input('Enter no of years: '))
r = float(input('Enter rate of interest: '))
i=(p*n*r)/100
print('the simple interest is ',i)

#net pay
basic_pay=float(input('enter basic_pay '))
hr=0.03*basic_pay
da=0.05*basic_pay
deduction=0.02*basic_pay
net_pay=basic_pay+hr+da-deduction
print('the net pay is ',net_pay)
                    
                    

