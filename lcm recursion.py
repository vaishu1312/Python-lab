def lcm(a,b,i=1):
   if i%a==0 and i%b==0:
            return i
   else:
         i+=1
         return lcm(a,b,i)

a=20
b=10
print(lcm(a,b))

def gcdr(a,b):
    if a<b:
      (a,b)=(b,a)
    if(b==0):
        return a
    else:
        return gcdr(b,a%b)

lcmr=(a*b)/(gcdr(a,b))
print(lcmr)
