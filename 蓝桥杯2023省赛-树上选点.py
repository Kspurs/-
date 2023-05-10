# Created on iPad.
n=int(input())
p=[-1,0]
p+=list(map(int,input().split()))
v=[0]
v+=list(map(int,input().split()))
childs=[[] for i in range(n+1)]
for i in range(2,n+1):
    parent=p[i]
    childs[parent].append(i)
layers=[[1]]
queue=[]
maxlayer=0
queue.append([1,1])
while len(queue)>0:
    node,layer=queue[0]
    queue.pop(0)
    layer+=1
    if len(layers)<layer:
        layers.append([])
    for child in childs[node]:
        maxlayer=max(maxlayer,layer)
        layers[layer-1].append(child)
        queue.append([child,layer])
dp=[v[1],0,0,1]
for i in range(2,maxlayer+1):
    max1=0
    second=0
    idx=-1
    for node in layers[i-1]:
        if p[node]==dp[3]:
            if  max(dp[2],dp[1])+v[node]>max1:
                idx=node
                second = max1
                max1=max(max1,max(dp[2],dp[1])+v[node])
            elif max(dp[2],dp[1])+v[node]>second:
                second=max(second,max(dp[2],dp[1])+v[node])
        else:
            if max(dp[2],dp[0])+v[node]>max1:
                idx=node
                second = max1
                max1=max(max1,max(dp[2],dp[0])+v[node])
            elif max(dp[2],dp[0])+v[node]>second:
                second=max(second,max(dp[2],dp[0])+v[node])
    dp[2]=max(dp[1],dp[0])
    dp[0]=max1
    dp[1]=second
    dp[3]=idx
ans=max(dp[0],dp[2])
print(ans)
