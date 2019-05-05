a=int(input())
b=list(map(int,input().split()))
ps=[]
pr=1
for i in b:
  pr*=i
ps.append(pr)
for i in range(0,a-1):
  n,n1=b[:i+1],b[i+1:]
  pr1,pr2=1,1
  for i in n:
    pr1*=i
  for i in n1:
    pr2*=i
  if pr1>pr2:
    ps.append(pr1)
  else:
    ps.append(pr2)
print(max(ps))
