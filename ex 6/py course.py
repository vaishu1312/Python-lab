stu=['anitha','saritha','furleen','divya','edward','rahul','ibrahim']
#new student
s1=input('Enter the name of the new student: ')
print()
stu.append(s1)
print('The list of students are: ')
print(stu)
print()
#no of students
l=len(stu)
print('The no of students registered for the course are: ',l)
print()
#first and last student
first=min(stu)
last=max(stu)
print('The first student and the last student in lexographical order are ',first,'and ',last,'respectively')
print()
#new list
n=int(input('Enter no of new students: '))
for i in range(0,n):
    e=input('Enter name of student {}: '.format(i+1))
    stu.append(e)
print()
print('The new list of students are: ',stu)
print()
#sort
stu.sort()
print('The sorted name list is: ',stu)
print()
#reg no
regno=[]
reg=101
print('The list of students with register no are: ')
for i in range(len(stu)):
   regno.append(reg)
   reg=reg+1
   print(regno[i],stu[i])
print()
#insert new student
new=input('Enter the name of the new student: ')
for i in range (len(stu)):
  if stu[i]<new<stu[i+1]:
      p=i+1
      break
stu.insert(p,new)
a=regno[-1]+1
regno.append(a)
print('The modified list is ')
print(stu)
print()
#search for a student name
name=input('Enter name of student to be searched: ')
position=stu.index(name)
print('The reg no of the student is: ',regno[position])
print()
#discontinued
rname=input('Enter name to be removed: ')
index=stu.index(rname)
stu.remove(rname)
d=regno.pop(index)
for i in range(index,len(stu)):
    regno[index]=d
    d+=1
print('The updated list is: ',stu)
print()
#name list for exam
print('The name list for the exam is: ')
for i in range(len(stu)):
  print(regno[i],stu[i])
  
