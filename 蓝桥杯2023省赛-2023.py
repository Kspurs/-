ans=0
for i in range(12345678,98765433):
    break
    s=str(i)
    s1="2023"
    idx=0
    for j in range(len(s)):
        if idx<4 and s[j]==s1[idx]:
            idx+=1
    if idx==4:
        ans+=1
print(98765433-12345678-460725)