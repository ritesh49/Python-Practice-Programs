#Break your Head Here ;)
import math
k,q=map(int,input().split())
lst=['_' for i in range(100000)]
def prime_factor(k):
	p_k=[]
	while k%2==0:
		p_k.append(2)
		k=k/2
	for i in range(3,int(math.sqrt(k))+1,2):
		while k%i==0:
			p_k.append(i)
			k=k/i
	if k>2:
		p_k.append(int(k))
	return p_k
k_prime=prime_factor(k)
dic_prime={}
for _ in range(q):
	qu=[i for i in input().split()]
	l=int(qu[1])
	r=int(qu[2])
	if qu[0]=='!':
		if qu[3] not in dic_prime:
			dic_prime.update({int(qu[3]):prime_factor(int(qu[3]))})
		for i in range(l,r+1):
			if lst[i]=='_':
				lst[i]=int(qu[3])
	if qu[0]=='?':
		coun=0
		for i in set(lst[l:r+1]):
			if i=='_':
				continue
			else:
				for i in dic_prime[i]:
					if i in k_prime:
						coun+=1
						break
		print(coun)