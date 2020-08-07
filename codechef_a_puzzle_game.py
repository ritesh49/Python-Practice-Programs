#Break Your Head Here ;)
for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	odd=0
	even=0
	c=0
	for i in a:
		even=even+1 if i%2==0 else even+0
	for i in range(n-1,-1,-1):
		if a[i]%2!=0:
			odd+=1
			continue
		else:
			c+=odd*even
			odd=0
			even-=1		
	print(c)	