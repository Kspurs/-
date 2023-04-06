s=input()
m={}
for i in range(len(s)):
    if s[i] not in m:
        m[s[i]]=[i]
    else:
        m[s[i]].append(i)
ans=0
for i in range(26):
    if chr(i+97) in m:
        ch=chr(ord('a')+i)
        tmp=m[ch]
        for j in range(0,len(tmp)):
            left=1
            right=1
            if j!=0 and j!=len(tmp)-1:
                left+=tmp[j]-tmp[j-1]-1
                right+=tmp[j+1]-tmp[j]-1
            else:
                if j==0:
                    left+=tmp[j]
                else:
                    left+=tmp[j]-tmp[j-1]-1
                if j==len(tmp)-1:
                    right+=len(s)-tmp[j]-1
                else:
                    right+=tmp[j+1]-tmp[j]-1
            ans+=left*right
print(ans)