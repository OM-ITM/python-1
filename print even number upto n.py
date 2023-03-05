#even number upto n
x=int(input("enter any number\n"))
y=1
if x==0:
	print("invalid input")
while y<=x:
	if y%2==0:
		print(y)
	y=y+1
