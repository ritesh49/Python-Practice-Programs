n=int(input())
sumi,nt=0,1
for i in range(1,n+1):
	nt*=i
	sumi+=nt
print(sumi)