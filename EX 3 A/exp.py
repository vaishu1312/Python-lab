#exp-recursion
def power(base,exp):
    if exp==0:
        return 1
    else:
        return base*(power(base,exp-1))
    
base=int(input('enter base '))
exp=int(input('enter exponent '))
print('The result is',power(base,exp))
        


base=int(input('enter base '))
exp=int(input('enter exponent '))
result=1
while(exp>0):
    result*=base
    exp=exp-1
print('The result is',result)
