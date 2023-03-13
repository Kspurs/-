n,k=map(int,input().split())
lst=[i for i in range(1,n+1)]
num=1
while len(lst)>1:
    kid=lst.pop(0)
    if num%k!=0 and num%10!=k:
        lst.append(kid)
    num+=1
print(lst[0])