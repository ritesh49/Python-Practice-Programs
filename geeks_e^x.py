# Break Your Head Here ;)
from math import factorial
# n=int(input("Enter Range: "))
p=1
f=1
# su=0
def e(x,n):
	global p,f
	if (n==0):
		return 1
	r=e(x,n-1)
	p*=x
	f*=n
	# return(r+p/f)
	return(r+p/f)

print(e(4,15))
# j=0
# while True:
# 	j+=1
# 	nt1*=n
# 	nt2*=j
# 	if nt1//nt2==0:
# 		break
# 	else:
# 		sum+=(nt1/nt2)
# print(sum,j)