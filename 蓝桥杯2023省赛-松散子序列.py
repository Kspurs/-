s=input()
d0=0
d1=ord(s[0])-97+1
for i in range(1,len(s)):
    d00=max(d0,d1)
    d11=d0+ord(s[i])-97+1
    d0=d00
    d1=d11
print(max(d0,d1))

