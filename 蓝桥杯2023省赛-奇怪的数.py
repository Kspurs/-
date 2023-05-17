n,m=map(int,input().split())
dp=[[0 for i in range(626)] for j in range(n+1)]
mod=998244353
m1={}
m2={}
vis=set()
idx=0
for i in range(5):
    for j in range(5):
        for p in range(5):
            for q in range(5):
                idx+=1
                num=i*2*1000+j*2*100+(1+p*2)*10+(1+q*2)
                if i*2+j*2+(1+p*2)+(1+q*2)<=m:
                    dp[4][idx]=1
                    vis.add(idx)
                m1[num]=idx
                m2[idx]=num
def sqr(a,b):

    if b==0:
        return 1
    if b==1:
        return a%mod
    if b%2==0:
        return (sqr(a,b//2)**2)%mod
    else:
        return (sqr(a,b-1)*(a%mod))%mod
nums=[[0,2,4,6,8],[1,3,5,7,9]]
if m>=43:
    ans=sqr(5,n)
    print(ans)
elif m<2:
    print(0)
else:
    for i in range(5,n+1):
        newvis=set()
        for j in vis:
            if dp[i-1][j]>0:
                tmp=m2[j]
                even1=tmp//1000
                even2=(tmp%1000)//100
                odd1=(tmp%100)//10
                odd2=tmp%10
                for num in nums[i%2]:
                    if num+even1+even2+odd1+odd2<=m:
                        if i%2==0:
                            neweven2=num
                            neweven1=even2
                            newtmp=tmp%100+neweven1*1000+neweven2*100
                            dp[i][m1[newtmp]]+=dp[i-1][j]%mod
                            dp[i][m1[newtmp]]%=mod
                            newvis.add(m1[newtmp])
                        else:
                            newodd2 = num
                            newodd1 = odd2
                            newtmp = tmp-tmp%100 + newodd1*10+newodd2
                            dp[i][m1[newtmp]] += dp[i-1][j] % mod
                            dp[i][m1[newtmp]] %= mod
                            newvis.add(m1[newtmp])
                    else:
                        break
        vis=newvis
    print(sum(dp[-1])%mod)