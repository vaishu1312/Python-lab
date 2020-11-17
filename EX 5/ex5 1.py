def substring(s1,s2):
  print('The no of occurences are ',s1.count(s2))
  for i in range(len(s1)):
        if s1[i:i+len(s2)]==s2:
           print('Found at index ',i)   

p='vhas hello vc hello'
print('The string is ',p)
q="hello"
print('The substring is ',q)
substring(p,q)
#
def substring(s1,s2):
  count=0
  for i in range(len(s1)):
    if s1[i:i+len(s2)]==s2:
        count = count+1
  print('The no of occurences are ',count)
  for i in range(len(s1)):
        if s1[i:i+len(s2)]==s2:
           print('Found at index ',i)   

p='vhas hello vc hello'
print('The string is ',p)
q="hello"
print('The substring is ',q)
substring(p,q)
#
def substring(s1,s2):
  print('The no of occurences of', s2, 'are ',s1.count(s2))
  for i in range(len(s1)):
        if s1[i:i+len(s2)]==s2:
           print(s2,'is found at index ',i)   

print()
p='vhas hello vc hello'
print('The string is ',p)
s=p.split()
for i in s:
  substring(p,i)
