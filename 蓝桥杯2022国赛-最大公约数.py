import math


class node:
    def __init__(self,gcd,l,r):
        self.gcd=gcd
        self.l=l
        self.r=r
class tree:
    def __init__(self,n,nums):
        self.n=n
        self.lst=[0 for i in range(n*4)]
        self.nums=nums
        self.one=0
    def pushup(self,x):
        self.lst[x].gcd=math.gcd(self.lst[x*2].gcd,self.lst[x*2+1].gcd)
    def build(self,x,l,r):
        if l==r:
            self.lst[x]=node(self.nums[l],l,r)
            if self.lst[x].gcd==1:
                self.one+=1
        else:
            self.lst[x]=node(0,l,r)
            mid=(l+r)//2
            self.build(x*2,l,mid)
            self.build(x*2+1,mid+1,r)
            self.pushup(x)
    def query(self,x,l,r):
        l1=self.lst[x].l
        r1=self.lst[x].r
        if l1>=l and r1<=r:
            return self.lst[x].gcd
        else:
            mid=(l1+r1)//2
            if r<=mid:
                return self.query(x*2,l,r)
            elif l>mid:
                return self.query(x*2+1,l,r)
            else:
                gcd1=self.query(x*2,l,r)
                gcd2=self.query(x*2+1,l,r)
                return math.gcd(gcd1,gcd2)
n=int(input())
nums=list(map(int,input().split()))
t=tree(n,nums)
t.build(1,0,n-1)
min1=n
j=0
for i in range(n):
    while j<i and t.query(1,j+1,i)==1:
        j+=1
    if t.query(1,j,i)==1:
        min1=min(min1,i-j)
if t.one>0:
    print(n-t.one)
elif min1==n:
    print(-1)
else:
    print(min1+n-1)
