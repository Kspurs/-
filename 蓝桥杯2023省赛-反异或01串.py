s=input()
s1=""
for ch in s:
    s1+='0'+ch
s1+='0'
s=s1
n=len(s)
l=[]
for i in range(n+1):
    l.append(0)
k=0
r=0
pre=[]
for i in range(n+1):
    pre.append(0)

l[0]=1
for i in range(1,n):
    if s[i]=='1':
        pre[i+1]=pre[i]+1
    else:
        pre[i+1]=pre[i]
    if i<r:
        l[i]=min(r-i,l[(k<<1)-i])
    else:
        l[i]=1
    while i-l[i]>=0 and i+l[i]<n and s[i+l[i]]==s[i-l[i]]:
        l[i]+=1
    if i+l[i]>r:
        k=i
        r=i+l[i]
res=pre[n]
for i in range(0,n):
    if s[i]=='1':
        continue
    left=i-l[i]+1
    right=i+l[i]-1
    res=min(res,((pre[right+1]-pre[left])>>1)+pre[left]+pre[n]-pre[right+1])
print(res)