y=int(input("Enter year: "))
if y%4==0:
    if y%100:
        if y%400:
           print("Leap year')
        else:
           print("Not a leap year")
    else:
        print("Leap year')
else:
    print("Not a leap year")
                 
