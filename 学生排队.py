n=int(input())
m=int(input())
lst=[i for i in range(1,n+1)]
m1={}
for i in range(1,n+1):
    m1[i]=i-1
for i in range(m):
    no,pos=map(int,input().split())
    curpos=m1[no]
    if pos<0:
        for j in range(curpos-1,curpos+pos-1,-1):
            m1[lst[j]]+=1
            lst[j+1]=lst[j]
        lst[curpos+pos]=no
        m1[no]=curpos+pos
    else:
        for j in range(curpos+1,curpos+pos+1):
            m1[lst[j]]-=1
            lst[j-1]=lst[j]
        lst[curpos+pos]=no
        m1[no]=curpos+pos
for num in lst:
    print(num,end=" ")
