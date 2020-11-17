#Binary Search
def binary_search(sortedlist,n,x):
    start=0
    end=n
    while(start<=end):
        mid=(start+end)//2
        if (x==sortedlist[mid]):
            return mid
        elif(x < sortedlist[mid]):
               end = mid - 1
        else:
               start = mid + 1 
    return -1  
 
sorted_cubes=[1,8,27,64,125,216,343,512,729,1000]
print('The list of sorted cubes are: ')
print( sorted_cubes)
n=len(sorted_cubes)
x = int(input("Enter the number to be searched: "))
position = binary_search(sorted_cubes,n,x)
if(position != -1):
    print("Entered number",x,"is present at position: ",position)
else:
    print("Entered number",x,"is not present in the list")
print()

#linear search
def linear_search(list, key):
    for j in range(len(list)):
            if list[j] == key:
                return j
    else:
        return -1

unsorted_cubes=[8,343,1,1000,125,27,512,64,216,729]
print('The list of unsorted cubes are:')
print(unsorted_cubes)    
key=int(input('Enter the number to be searched: '))
val=linear_search(unsorted_cubes,key)
if val==-1:
    print("Entered number",key,"is not present in the list")
else:
    print("Entered number",key,"is present at position: ",val)
