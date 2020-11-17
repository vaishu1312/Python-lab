def  freq ( n, i):
        count  = 0
        while  n> 0:
                    r  = n% 10
                    n = n//10
                    if  r == i:
                          count+=1
        return  count
n = int ( input ( 'Enter the integer: ' ))
for i in  range ( 0, 10 ) :
            x = freq ( n, i )
            if x != 0 :
               print ( 'no of ' , i, " s", ' are: ' , x )


n = int ( input ( 'Enter the integer: ' ))
a=[0]*10
while n>0:
    d=n%10
    a[d]+=1
    n=n//10
for i in range(len(a)):
    if a[i]!=0:
        print('no of ' , i, " s", ' are: ' ,a[i])
