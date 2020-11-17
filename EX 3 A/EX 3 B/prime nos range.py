#list
l=int(input('Enter lower range '))
u=int(input('Enter upper range '))
list=[]
prime=[]
comp=[]
for k in range(l,u+1):
    list.append(k)
print('the list of nos is',list)
for num in list:
    for j in range(2,num):
        if(num%j==0):
          comp.append(num)
          break        
    else:
         prime.append(num)
print('The prime nos in the range are',prime)
print('The composite nos in the range are',comp)


l=int(input('enter lower range '))
u=int(input('enter upper range '))
print('Prime nos between',l,'and',u,'are: ')
for i in range(l,u+1):
    if i>1:
      for j in range(2,i):
        if(i%j==0):
          break        
      else:
         print(i)
    elif i==1:
        print('1 is neither prime nor composite')

