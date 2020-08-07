from collections import Counter as c
n=[i for i in input().split()]
td=[i for i in n[1:] if len(i)==3]
n=n[0]
lis=[]
for i in td:
	sum=0
	sum=str(int(max(i))*11+int(min(i))*7)
	if len(sum)==3:
		sum=sum[1:]	
	lis.append(sum[0])
coun=0
b=dict(c(lis[1::2]))
for i in b:
	coun=coun+2 if b[i]>2 else coun+1
b=dict(c(lis[0::2]))
for i in b:
	coun=coun+2 if b[i]>2 else coun+1
print(coun)