s=input()
m={}
ans=0
i=0
while i<len(s):
    if i+1<len(s):
        if s[i+1]==s[i] or s[i+1]=='?' or s[i]=='?':
            ans+=1
            i+=2
        else:
            i+=1
    else:
        i+=1
print(ans)
