n,m,k,t=map(int,input().split())
times=list(map(int,input().split()))
seeds=list(map(int,input().split()))
methods=[[] for i in range(n+1)]
gettime=[-1 for i in range(n+1)]
for i in range(k):
    s1,s2,s3=map(int,input().split())
    methods[s3].append([s1,s2])
def f(seed):
    if seed in seeds:
        return 0
    if gettime[seed]!=-1:
        return gettime[seed]
    tmp=0x3f3f3f
    for m in methods[seed]:
        s1=m[0]
        s2=m[1]
        tmp=min(tmp,max(f(s1),f(s2))+max(times[s1-1],times[s2-1]))
    gettime[seed]=tmp
    return tmp
print(f(t))
