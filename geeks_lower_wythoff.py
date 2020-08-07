# Break Your Head Here ;)
n=int(input())
ls=[2,1,2,2,1]
nt=1
for i in range(n):
	print(nt,end=', ')
	nt+=ls[i%5]

