from queue import PriorityQueue
n=int(input())
nums=list(map(int,input().split()))
nums.sort()
i=0
m={}
q=PriorityQueue()
for num in nums:
    if num not in m:
        q.put(num)
        m[num]=0
    m[num]+=1

while not q.empty():
    tmp=q.get()
    div=tmp+1
    sum=m[tmp]
    if sum%div!=0:
        print(tmp)
        break
    while sum%div==0:
        sum=sum//div
        div+=1
    if div-1 not in m:
        q.put(div-1)
        m[div-1]=0
    m[div-1]+=sum