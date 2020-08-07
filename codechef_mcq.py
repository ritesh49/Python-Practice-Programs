for i in range(int(input())):
	n=int(input())
	s=input()
	u=input()
	coun=0
	i=0
	while i<n:
		if u[i]==s[i]:
			coun+=1
		elif u[i]=='N':
			coun+=0
			i+=1
			continue
		elif u[i]!=s[i]:
			i+=2
			continue			
		i+=1
	print(coun)