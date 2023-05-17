n=int(input())
cnt=[]
for i in range(100001):
    cnt.append(0)
nums=[]
for i in range(n):
    a,b=map(int,input().split())
    nums.append(b*10+a)
    cnt[a]+=1
nums.sort()
ans=0
for i in range(n):
    num=nums[i]%10
    cost=nums[i]//10
    if cnt[num]>n//10:
        cnt[num]-=1
        ans+=cost
print(ans)