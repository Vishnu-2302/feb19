def prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True


t=int(input('enter number of series : '))
for i in range(t):
	n=input('enter the range : ').split()
	initial=int(n[0])
	final=int(n[1])
	c=0
	for i in range(initial+1,final):
		if prime(i):
			print(i,end=' ')
			c=c+1
	print(f'total count = {c}')