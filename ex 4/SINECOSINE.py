#sine and cosine function
import math
def fact(N):
        if N <=1:
                return 1
        else:
                return N*fact(N-1)
def sinfun(y,n):
                x=y*(math.pi/180)
                res = x
                sign = -1
                for i in range (3,n,2):
                        res = res +((sign*(x**i))/fact(i))
                        sign = - sign
                return res

        
def  cosfun(y,n):
                x=y*(math.pi/180)
                res=1
                sign=-1
                for j in range (2,n,2):
                        res=res+((sign*(x**j))/fact(j))
                        sign = - sign
                return res
        
            
print('Enter choice as 1 – sine function /2 – cosine function')
choice= int(input('Enter choice: ' ))
if choice == 1:
        x=int(input('Enter x in degrees: '))
        n= int(input('Enter n: '))
        if n%2!=0:
                print('sin(',x,')=1',end='')
                sign=1
                for i in range(3,n+2,2):
                          sign=-sign
                          if sign==-1:
                                  print((1*sign),'(1/',i,'!)',x,'**',i,sep='',end='')
                          else:
                                  print('+','(1/',i,'!)',x,'**',i,sep='',end='')
                result = sinfun(x,n)
                print ('=',result,sep='')
        else:
                print('Number',n,'not odd')
                    
elif choice == 2:
        x=int(input('Enter x in degrees: '))
        n= int(input('Enter n: '))
        if n%2==0:
                print('cos(',x,')=1',end='')
                sign=1
                for i in range(2,n+2,2):
                          sign=-sign
                          if sign==-1:
                                  print((1*sign),'(1/',i,'!)',x,'**',i,sep='',end='')
                          else:
                                  print('+','(1/',i,'!)',x,'**',i,sep='',end='')

                result = cosfun(x,n)
                if result == -50:
                    print ('Result not available')
                else:
                    print ('=',result,sep='')
        else:
           print('Number',n,'not even')
else:
    print('Incorrect choice')


