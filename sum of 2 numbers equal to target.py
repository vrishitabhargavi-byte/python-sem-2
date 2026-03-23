def sum(S,T):
  L=len(S)
  for i in range(L):
    for j in range(i+1,L):
      if S[i] + S[j]==T:
        return [i,j]
S=[2,7,8,4]
T=12
r=sum(S,T)
print(r)