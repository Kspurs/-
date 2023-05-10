n=int(input())
lst=list(map(int,input().split()))
lst.sort()
ans=0
m={}
cost=0
idx=len(lst)-1
last=len(lst)-1
for i in range(len(lst)-1,-1,-1):
    if i not in m:
        ans+=lst[i]
        cost+=1
        if cost%2==0:
            tmp=min(lst[i],lst[last])//2
            while idx>=0 and (lst[idx]>tmp or idx in m):
                idx-=1
            if idx>=0:
                m[idx]=1
        last=i
print(ans)
