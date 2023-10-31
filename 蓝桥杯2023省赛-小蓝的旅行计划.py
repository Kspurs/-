from queue import PriorityQueue
class gas:
    def __init__(self,idx,cost):
        self.i=idx
        self.c=cost
class tree:
    def __init__(self,n):
        self.rest=[0 for i in range(n*4+1)]
        self.k=[0 for i in range(n*4+1)]
    def build(self,i,l,r):
        if l==r:
            self.rest[i]=0
            return
        self.build(i*2,l,(l+r)>>1)
        self.build(i*2+1,(l+r)//2+1,r)
    def pushup(self,i):
        self.rest[i]=max(self.rest[i*2],self.rest[i*2+1])
    def pushdown(self,i):
        if self.k[i]>0:
            self.rest[i*2]+=self.k[i]
            self.rest[i * 2+1] += self.k[i]
            self.k[i*2]+=self.k[i]
            self.k[i*2+1]+=self.k[i]
        self.k[i]=0
    def update(self,i,l,r,l1,r1,val):
        if (l>=l1 and r<=r1):
            self.rest[i]+=val
            self.k[i]+=val
            return
        mid=(l+r)//2
        self.pushdown(i)
        if mid>=l1:
            self.update(i*2,l,mid,l1,r1,val)
        if mid<r1:
            self.update(i*2+1,mid+1,r,l1,r1,val)
        self.pushup(i)
    def query(self,i,l,r,l1,r1):
        if l>=l1 and r<=r1:
            return self.rest[i]
        mid=(l+r)//2
        self.pushdown(i)
        res=0
        if mid<r1:
            res=max(res,self.query(i*2+1,mid+1,r,l1,r1))
        if mid>=l1:
            res=max(res,self.query(i*2,l,mid,l1,r1))
        self.pushup(i)
        return res
def solve():
    n,m=map(int,input().split())
    t=tree(n)
    vol=m
    q=PriorityQueue()
    ans=0
    dis=[0]
    cost=[0]
    lim=[0]
    for i in range(1,n+1):
        num1,num2,num3=map(int,input().split())
        dis.append(num1)
        cost.append(num2)
        lim.append(num3)
    t.build(1,1,n)
    for i in range(1,n+1):
        vol-=dis[i]
        while vol<0:
            if q.empty():
                print(-1)
                return
            a=q.get()
            cnt=min(lim[a[1]],m-t.query(1,1,n,a[1],i-1))
            if cnt<=0:
                continue
            if cnt+vol<=0:
                ans+=a[0]*cnt
                lim[a[1]]=0
                vol+=cnt
                t.update(1,1,n,a[1],i-1,cnt)
            else:
                ans+=(-vol)*a[0]
                lim[a[1]]=cnt+vol
                t.update(1,1,n,a[1],i-1,-vol)
                vol=0
                q.put((a[0],a[1]))
        if(vol>0):
            t.update(1,1,n,i,i,vol)
        lim[i]=min(lim[i],m-vol)
        q.put((cost[i],i))
    print(ans)
solve()