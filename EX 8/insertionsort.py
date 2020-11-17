#Insertion sort
def insertionSort(list):
  for i in range(1,len(list)):
    key = list[i]
    j = i-1
    #while list i-1 >list [i]
    while j>=0 and list[j]>key:
        #list i=list[i-1]
        list[j+1]=list[j]
        j = j-1
    list[j+1]=key
    print("at the end of iteration ",i-1, list) 
  return(list)

list = [54,2,39,17,77,31,44,55,20]
print('The list is ',list)
print('The sorted list is ',insertionSort(list))
