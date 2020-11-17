#
n=5
for i in range(0, n):
	for j in range(0, i+1):
		print("* ",end="")
	print()
print()
#
n=5
k = n+3
for i in range(0, n):
	for j in range(0, k):
		print(end=" ")
	k = k - 2
	for j in range(0, i+1):
		print("* ", end="")
	print()
print()
#
n=5
for i in range(0, n):
	for j in range(n, i, -1):
		print("* ", end="")
	print()
print()
#
n=5
k = n-5
for i in range(0, n):
	for j in range(0, k):
		print(end=" ")
	k = k + 2
	for j in range(5, i, -1):
		print("* ", end="")
	print()
print()
#
n=5
k = 2*n-(n+1) 
for i in range(0, n):
     for j in range(0, k):
            print(end=" ")
     k = k - 1
     for j in range(0, i+1):
         print("* ", end="")
     print()
print()
#
n=5
k = 0
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k + 1
    for j in range(n, i, -1):
        print("* ", end="")
    print()

