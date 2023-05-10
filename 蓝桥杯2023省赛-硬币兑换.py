lst=[i for i in range(1,2024)]
ans=0
for i in range(4046):
    tmp=0
    for j in range(1,i):
        if j>i-j:
            break
        if i-j<=2023:
            if i-j>j:
                tmp+=j
            else:
                tmp+=j//2
    if i<=2023:
        tmp+=i
    ans=max(ans,tmp)
print(ans)