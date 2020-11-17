#celsius to fahrenheit
c=float(input('enter temp in celsius '))
f=((c*(9/5))+32)
print('the temp in fah is ',f)

#fahrenheit to celsius
f=float(input('enter temp in fahrenheit '))
c=((f-32)*(5/9))
print('the temp in cel is ',c)

#lc
c=[23.4,56,10,178]
f=[((i*(9/5))+32) for i in c]
print(f)
f=[23.4,56,10,178]
c=[((i-32)*(5/9)) for i in f]
print(c)

#map
print(list(map(lambda c: ((c*(9/5))+32),[23.4,56,10,178])))
print(list(map(lambda f: ((f-32)*(5/9)),[23.4,56,10,178])))



