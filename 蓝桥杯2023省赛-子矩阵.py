from collections import deque
n,m,a,b=map(int,input().split())
mat=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    mat.append(tmp)
def maxrow(nums,a):
    ans=[]
    q=deque()
    if a>len(nums):
        return []
    for i in range(len(nums)):
        while len(q)>0 and nums[q[-1]]<nums[i]:
            q.pop()
        q.append(i)
        if q[0]<=i-a:
            q.popleft()
        if i>=a-1:
            ans.append(nums[q[0]])
    return ans
def minrow(nums,a):
    ans=[]
    if a>len(nums):
        return []
    q=deque()
    for i in range(len(nums)):
        while len(q)>0 and nums[q[-1]]>nums[i]:
            q.pop()
        q.append(i)
        if q[0]<=i-a:
            q.popleft()
        if i>=a-1:
            ans.append(nums[q[0]])
    return ans
maxlst=[]
minlst=[]
for i in range(n):
    maxs=maxrow(mat[i],b)
    mins=minrow(mat[i],b)
    maxlst.append(maxs)
    minlst.append(mins)
maxlst=[[maxlst[j][i] for j in range(len(maxlst))] for i in range(len(maxlst[0]))]
minlst=[[minlst[j][i] for j in range(len(minlst))] for i in range(len(minlst[0]))]
finalmax=[]
finalmin=[]
for i in range(len(maxlst)):
    maxs=maxrow(maxlst[i],a)
    mins=minrow(minlst[i],a)
    finalmax.append(maxs)
    finalmin.append(mins)
ans=0
k=998244353
for i in range(len(finalmax)):
    for j in range(len(finalmax[0])):
        tmp=(finalmax[i][j]*finalmin[i][j])%k
        ans=(ans+tmp)%k
print(ans)