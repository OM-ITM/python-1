#even number upto n
x=int(input("enter any number\n"))
y=1
if x==0 or x==1:
	print("invalid input")
while y<=x:
	if y%2==0:
		print(y)
	y=y+1
# another way
x=int(input("enter any number greayer than one:\t"))
for i in range(2,x+1,2):
	print(i)
	
# another one
x=int(input("enter any number\n"))
y=2
if x==0 or x==1:
	print("invalid input")
while y<=x:
	print(y)#if y%2==0:
	y=y+2
