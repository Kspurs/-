t=int(input())
for i in range(t):
    f=0
    n,m=map(int,input().split())
    for j in range(2,m+1):
        if f:
            break
        for k in range(1,j):
            if n%j==n%k:
                f=1
                break
    if f:
        print("Yes")
    else:
        print("No")