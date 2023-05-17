t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    l=k
    r=k
    tmp=1
    res=0
    while(1):
        res+=tmp
        if r*m+1>n:
            if (l-1)*m+2<=n:
                res+=n-((l-1)*m+2)+1
            break
        tmp*=m
        l=(l-1)*m+2
        r=r*m+1
    print(res)
