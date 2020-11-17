#
k = 1
n=5
for i in range(0, n):
	for j in range(0, k):
		print("* ", end="")
	k = k + 2
	print()
print()
#
n=5
k =2*(n+3)
tim = 1
for i in range(0, n):
	for j in range(0, k):
		print(end=" ")
	k = k - 4
	for j in range(0, tim):
		print("* ", end="")
	tim = tim + 2
	print()
print()
#
n=5
k =2*(n)
tim = 1
for i in range(0, n):
	for j in range(0, k):
		print(end=" ")
	k = k - 2
	for j in range(0, tim):
		print("* ", end="")
	tim = tim + 2
	print()
print()
#
for i in range(1,6):
        for j in range(1,6):
                print('*',end='')
        print()
