jee=['divya','edward','mena','arun','lina','shuba','jai','ashwin','rahul','devi','john']
neet=['gayatri’,mena' ,'lina','shuba','kumar','aishu','rahul','devi','john','jack']
print('Students who passed jee: ')
print(jee)
print()
print('Students who passed neet: ')
print(neet)
print()
#both exams
both = []
for element in jee:
        if element in neet:
            both.append(element)
print('List of students who have qualified both exams: ')
print(both)
print()
#only jee
ojee=[]
for i in jee:
    if i not in both:
       ojee.append(i) 
print('List of students who have qualified only in JEE: ')
print(ojee)
print()    
#only neet
oneet=[]
for j in neet:
    if j not in both:
       oneet.append(j) 
print('List of students who have qualified only in NEET: ')
print(oneet)
print()
#atleast one exam
list4=[]
for k in ojee:
  list4.append(k)
for name in oneet:
   list4.append(name)
for s in both:
    list4.append(s)   
print('Students who attended atleast one exam: ')
print(list4)
print()



