string='aeiousdaeiou'
count=0
cons=0
for i in string:
    if ('a' in i) or ('e' in i) or ('i' in i) or ('o' in i) or ('u' in i):
         count = count+1
    else:
        cons=cons+1
      
print(count)   
print(cons)
