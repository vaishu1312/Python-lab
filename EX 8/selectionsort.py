#swaps the element-without min fn
A= [54,2,39,17,77,31,44,55,20]
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
    print('At the end of iteration',i,'the list is ',A)
print(A)

#swaps the element-uses min fn
a=[64, 25, 12, 22]
for i in range(len(a)):
    smallest=min(a[i:])
    smallestindex=a.index(smallest)
    a[i],a[smallestindex]=a[smallestindex],a[i]
    print('At the end of iteration',i,'the list is ',a)
print(a)

#selection sort(pushes the element)
def selectionsort(a):
    for j in range(0,len(a)):
      smallest=a[j]
      for i in range(j+1,len(a)):
         if smallest>a[i]:
           (smallest,a[i])=(a[i],smallest)
      a[j]=smallest
      print('At the end of iteration',j+1,'the list is ',a)
    return(a)

n=int(input('Enter no of elements: '))
list=[]
for i in range (0,n):
    e=int(input('Enter element{}: '.format(i+1)))
    list.append(e)
print('The list is ',list)
print('The sorted list is ',selectionsort(list))

