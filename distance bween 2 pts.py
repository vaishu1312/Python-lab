#distance between two points
def sqrt(n):
    return(n**(1/2))

def dist(a,b,c,d):
        distance=sqrt((c-a)**2+(d-b)**2)
        return(distance)
    
x1=int(input('enter x1 '))
x2=int(input('enter x2 '))
y1=int(input('enter y1 '))
y2=int(input('enter y2 '))
print('the distance between (',x1,',',y1,') and (',x2,',',y2,') is ',\
      dist(x1,y1,x2,y2),sep='')
