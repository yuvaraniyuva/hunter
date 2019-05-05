ai=input()
s=''
for i in range(0,len(ai)-1,2):
  if int(ai[i+1])%2==0:
    s+=ai[i]*int(ai[i+1])
  else:
    s+=ai[i]+ai[i+1]
print(s)
