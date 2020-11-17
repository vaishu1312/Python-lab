#quadratic eqn solution
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = (b**2) - (4*a*c)
if d<0:
    print('Imaginary roots')
else:
    if d>=0:
      print('Roots are real and equal')
    else:
       print('Roots are real and distinct')
    r1 = (-b+(d**0.5))/(2*a)
    r2 = (-b-(d**0.5))/(2*a) 
    print('The roots are ',r1 ,'and ',r2)

    

def sqrt(n):
    return(n**(1/2))

def rootofeqn(x,y,z):
    d=b**2-4*a*c
    if d<0:
        print('the roots are imaginary')
    else:
        r1=(-b+sqrt(d))/(2*a)
        r2=(-b-sqrt(d))/(2*a)
        print(r1,r2)    

a=float(input('enter the coefficient of x^2'))
b=float(input('enter the coefficient of x'))
c=float(input('enter the constant term'))
rootofeqn(a,b,c)

