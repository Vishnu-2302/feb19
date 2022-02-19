def prime(n):
	for i in range (2,n):
		if n%i==0:
			return False
	return True

t=int(input('enter number series : '))
for i in range(t):
	n=int(input('enter the number : '))
	c=0
	for i in range(2,n+1):
		if prime(i):
			print(i,end=' ')
			c=c+1
	print(f'total count = {c}')