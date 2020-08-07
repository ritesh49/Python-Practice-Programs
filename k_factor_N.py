#k largest factor of N
n,k=map(int,input().split(','))
fac=[i for i in range(1,n+1) if n%i==0]
print(fac[k] if k<len(fac) else 1)