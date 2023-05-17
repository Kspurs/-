t=int(input())
def matpow(mat,n):
    if n==1:
        return mat
    if n%2==0:
        return matpow(mat,n//2)

while t:
    t-=1
    n=int(input())