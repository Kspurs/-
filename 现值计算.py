n,rate=map(float,input().split())
nums=list(map(int,input().split()))
ans=0
for i in range(int(n)+1):
    ans+=nums[i]*(1+rate)**(-i)
print(ans)