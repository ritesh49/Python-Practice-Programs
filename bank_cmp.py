#counting rock samples
'''
	ppm
'''
import sys
s,r=map(int,input().split())
samples=[int(i) for i in input().split()]
ranges=[]
for i in range(r):
	a=[int(i) for i in input().split()]
	if len(a)==2 and len(samples)==s:
		ranges.append(a)
	else:
		sys.exit(0)
out=[]
for i in ranges:
	cou=0
	for j in samples:
		if j in range(i[0],i[1]):
			cou+=1
	out.append(cou)
for i in out:
	print(i,end=' ')