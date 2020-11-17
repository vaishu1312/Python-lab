n=int(input('enter number '))
if n>1:
        for j in range(2,n):
                if(n%j==0):
                  print(n,'is composite')
                  break        
        else:
          print(n,'is prime')
elif n==1:
        print('1 is neither prime nor composite')

