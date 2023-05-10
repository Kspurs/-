num=int(input())
if num<=325:
    len=2
    while (len-1)*len//2<num:
        len+=1
    ans=""
    for