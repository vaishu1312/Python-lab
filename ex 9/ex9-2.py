#no of occurences of a word,frequently used word
d={}
file=open('data.txt','w')
file.write('Good morning \n')
file.write('How are you? \n')
file.write('Good bye \n')
file.close()
file=open('data.txt','r')
print(file.read())
file=open('data.txt','r')
for i in file:
  #w=f.read().split()
  w=i.split()
  for word in w:
    #d[word]=w.count(word)
      if word not in d.keys():
         d[word]=1
      else:
         d[word]+=1
for j in d:
    print('No of occurences of ',"'",j ,"'",': ',d[j],sep='')
freq=max(d.values())
for k in d:
        if d[k]==freq:
            print('The most frequently used word is ',"'",k,"'")


