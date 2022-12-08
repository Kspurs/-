n,l,t=map(int,input().split())
lst=list(map(int,input().split()))
pace=[1]*n
for i in range(t):
    for j in range(n):
        lst[j]+=pace[j]
    loc={}
    for j in range(n):
        if lst[j] in loc:
            pace[j]=-pace[j]
            pace[loc[lst[j]]]*=-1
        if lst[j]==l or lst[j]==0:
            pace[j]*=-1
        loc[lst[j]]=j
for i in range(n):
    print(lst[i],end=" ")
