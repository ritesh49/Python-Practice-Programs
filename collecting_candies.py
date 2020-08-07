#Collecting Candies
'''
A-1
B-2
D-3
E-4
C-1+2=3
F-1+2+3=6
G-1+2+3+4=10
total_time=3+6+10=19
(1+2)+(1+2+3)+(1+2+3+4)
a[0:1],a[0:2]
'''
import sys
for i in range(int(input())):
	n=int(input())
	no_of_candies=[int(i) for i in input().split()]
	sumi=0
	no_of_candies.sort()
	for i in range(2,len(no_of_candies)+1):
		sumi+=sum(no_of_candies[0:i])
	print(sumi)