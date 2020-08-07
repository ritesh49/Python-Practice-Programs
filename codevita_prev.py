#Consecutive prime Sum
import math
def is_prime(a):
	if a<=1:
		return False
	max_div=math.floor(math.sqrt(a))
	for i in range(2,1+max_div):
		if a%i==0:
			return False
	return True
a=int(input())
prime=[]
for i in range(2,a):
	if is_prime(i):
		prime.append(i)
# [2, 3, 5, 7, 11, 13, 17, 19]
cou=0
sum=prime[0]
for i in range(1,len(prime)):
	sum+=prime[i]
	if sum in prime:
		cou+=1
print(cou)