def maxi(alist,n):
        for i in range(1,n+1):
                max=alist[i-1]
                for j in range(i-1,len(alist)):
                    if alist[j]>max:
                        max=alist[j]
                ind=alist.index(max)
                alist[i-1],alist[ind]=alist[ind],alist[i-1]
        
        return max
l=[55,71,123,5,82,90,6]
n=int(input('enter the no '))
print(maxi(l,n))


def mini(alist,n):
        for i in range(1,n+1):
                min=alist[i-1]
                for j in range(i-1,len(alist)):
                    if alist[j]<min:
                        min=alist[j]
                ind=alist.index(min)
                alist[i-1],alist[ind]=alist[ind],alist[i-1]
        
        return min
l=[55,71,123,5,82,90,6]
n=int(input('enter the no '))
print(mini(l,n))

#recursion
def find_max (L):
    if len(L) == 1:
        return L[0]
    else:
      v1 = L[0]
      v2 = find_max(L[1:])
      if v1 > v2:
        return v1
      else:
        return v2
L=[588,867,2,6]
print(find_max(L))
