list=['mena','arun','lina','shuba','jai','ashwin','rahul','devi','john','jack']
n=input('Enter the name of a student ')
list.append(n)
print('The new list is ',list)
index=0
name=input('enter name of student to be searched ')
for i in list:
  if name in i:
    print('Found at index ',index)
  else:
    index=index+1
