n,l,s=map(int,input().split())
trees=[]
treemap={}
for i in range(n):
    coor=list(map(int,input().split()))
    trees.append(coor)
    treemap[coor[0]*l+coor[1]]=1
mat=[]
for i in range(s+1):
    row=list(map(int,input().split()))
    mat.append(row)
mat.reverse()
mattreenum=0
for i in range(s + 1):
    for j in range(s + 1):
        if mat[i][j] == 1:
            mattreenum+=1
ans=0
for t in trees:
    if t[0]+s>l or t[1]+s>l:
        continue
    f=1
    num=0
    for tt in trees:
        if tt[0]-t[0]<=s and tt[0]-t[0]>=0 and tt[1]-t[1]>=0 and tt[1]-t[1]<=s:
            if mat[tt[0]-t[0]][tt[1]-t[1]]!=1:
                f=0
                break
            else:
                num+=1
    if f and num==mattreenum:
        ans+=1
print(ans)