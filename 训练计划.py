n,m=map(int,input().split())
depend=list(map(int,input().split()))
cost=list(map(int,input().split()))
early=[]
for i in range(m):
    if depend[i]!=0:
        early.append(early[depend[i]-1]+cost[depend[i]-1])
    else:
        early.append(1)
f=1
for i in range(m):
    print(early[i],end=" ")
    if(early[i]+cost[i]-1>n):
        f=0
print()
if f==1:
    last=[n-cost[i]+1 for i in range(m)]
    for i in range(m-1,-1,-1):
        if depend[i]>0:
            last[depend[i]-1]=min(last[depend[i]-1],last[i]-cost[depend[i]-1])
    for i in range(m):
        print(last[i],end=" ")
