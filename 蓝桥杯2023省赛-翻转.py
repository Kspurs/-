n=int(input())
str1=[]
str2=[]
for i in range(n):
    str1.append(input().split()[0])
    str2.append(input().split()[0])
for i in range(n):
    s1=str1[i]
    s2=str2[i]
    if len(s1)!=len(s2) or len(s1)==0:
        print(-1)
        continue
    f=1
    ans=0
    pre=0
    for j in range(len(s1)):
        if s1[j]!=s2[j]:
            if j==0 or j==len(s1)-1:
                f=0
                break
            else:
                if s2[j-1]!=s1[j] or s2[j+1]!=s1[j] or pre==1:
                    f=0
                    break
            pre=1
            ans+=1
        else:
            pre=0
    if f:
        print(ans)
    else:
        print(-1)


