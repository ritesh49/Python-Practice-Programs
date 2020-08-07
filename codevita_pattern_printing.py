n=int(input())
a=n
b=1
c=n*n+1
for i in range(n,0,-1):
	for j in range((n-i)*2):
		print('*',end='')
	for j in range(i):
		print(str(b),end='0')		
		b+=1
	for j in range(i):
		if j==i-1:
			print(c,end='')
		else:
			print(c,end='0')
		c+=1
	c=(c-1)-((i-1)*2)
	print()