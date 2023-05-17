a,b=map(int,input().split())
k=998244353
def sqr(a,b):
    if b==0:
        return 1
    if b==1:
        return a%k
    if b%2==0:
        return (sqr(a,b//2)**2)%k
    else:
        return (sqr(a,b-1)*(a%k))%k
num1=sqr(a,b)
num2=sqr(a,b-1)
print((num1-num2)%k)

