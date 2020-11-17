#eligiblitity to vote
date=int(input("Enter date of birth : "))
month=int(input("Enter month of birth: "))
year=int(input("Enter year of birth: "))
d=4
m=12
y=2017
if (m>month)or (m==month and d>date):
  age=y-year
elif (m<month) or (m==month and d<date) :
    age=y-year-1

if age>=18:
     print("Eligible to vote")
else:
     print("Not eligible to vote")
