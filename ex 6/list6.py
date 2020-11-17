#6
def rev(list):
    rev=[]
    for i in range(-1,-(len(list)+1),-1):
        rev.append(list[i])
    return rev
    
list=[1,2,3,4,5,6,7,8,9]
print('The list is ',list)
r=rev(list)
print('The reversed list is ',r)

#using slice
l=[1,2,3,4,5,6,7,8,9]
print('The reversed list is ',l[::-1])
