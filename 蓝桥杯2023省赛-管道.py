import io
import sys
n,length=map(int,input().split())
l=[0]
s=[0]
for i in range(n):
    l1,s1=map(int,input().split())
    l.append(l1)
    s.append(s1)
idxs=[i for i in range(1,n+1)]
idxs.sort(key=lambda t:l[t]-(2000000001-s[t]))
left=1
right=length*2+1
while left<right:
    mid=(left+right)>>1
    f=1
    rb=-1
    for i in range(n):
        j=idxs[i]
        if mid>=s[j]:
            ltmp=l[j]-(mid-s[j])
            rtmp=l[j]+(mid-s[j])
            if rb==-1 and ltmp>1:
                f=0
                break
            elif rb==-1:
                rb=rtmp
            else:
                if ltmp>rb+1:
                    f=0
                    break
                else:
                    rb=max(rb,rtmp)
    if rb==-1:
        left=mid+1
        continue
    if f==1 and rb>=length:
        right=mid
    else:
        left=mid+1
print(left)