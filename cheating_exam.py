#Cheating Exam
'''
c         d         x
 a       o e       s
  n     c   c     i
   y   e     o   h
    o d       d t
     u         e
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
c d x a o e s n c c  i  y  e  o  h  o  d  d  t  u  e
'''
d=int(input())
s=input()
k=-1
lis=[['' for i in range(len(s))] for i in range(d)]
k=-1
row=1
for i in range(len(s)):
	
	# lis[k][i]="*"
	if row==d-1 or row==0:
		k=k*-1
	row=row+k
	lis[row][i]="*"
# cdxaoesncciyeohoddtue
k=0
for i in range(d):
	for j in range(len(s)):
		if lis[i][j]=="*":
			lis[i][j]=s[k]
			k=k+1
k=-1
row=1
for i in range(len(s)):
	if row==d-1 or row==0:
		k*=-1
	row=row+k
	if lis[row][i]!='x':
		print(lis[row][i],end='')
