words=input().split(" ")
string=[]
for word in words:
	string.append(word[::-1])
print(*string);	
