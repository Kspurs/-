def row(s):
    underline=-1
    linkstack=[]
    res=""
    flag=0
    for i in range(len(s)):
        res+=s[i]
        cur = len(res) - 1
        if s[i]=='_':
            if flag==0:
                flag=1
                underline=cur
            else:
                for j in range(cur-1,-1,-1):
                    if res[j]=="_":
                        underline=j
                        break
                res=res[:underline]+"<em>"+res[underline+1:cur]+"</em>"
                flag=0
        elif s[i]==')':
            left=-1
            for j in range(cur, -1, -1):
                if res[j] == "(":
                    left = j
                    break
            res=res[:left]+"<a href="+"\""+res[left+1:cur]+"\">"+linkstack.pop()+"</a>"
        elif s[i]==']':
            left = -1
            for j in range(cur, -1, -1):
                if res[j] == "[":
                    left = j
                    break
            linkstack.append(res[left+1:cur])
            res=res[:left]
    return res
import sys
i=1
islist=0
ispara=0
strlst=[]
strlst.append("")
while 1:
    s = sys.stdin.readline()
    if not s:
        break
    s=s.strip()
    if len(s)>0:
        strlst.append(s)
    elif strlst[i-1]!="&":
        strlst.append("&")
for i in range(1,len(strlst)):
    s=strlst[i]
    if len(s)>0 and s!="&":
        res=""
        if s[0]=='#':
            rank=0
            while s[rank]=='#':
                rank+=1
            res+="<h"+str(rank)+">"
            j=rank
            while s[j]==' ':
                j+=1
            text=s[j:]
            res+=row(text)+"</h"+str(rank)+">"
            print(res)
        elif s[0]=='*':
            if ispara == 1:
                print("</p>")
                ispara = 0
            if islist==0:
                print("<ul>")
                islist=1
            res+="<li>"
            j=1
            while s[j]==' ':
                j+=1
            text=s[j:]
            res+=row(text)+"</li>"
            print(res)
        else:
            if islist == 1:
                print("</ul>")
                islist = 0
            if ispara==0:
                ispara=1
                res+="<p>"
                res+=row(s)
                print(res,end="")
            else:
                print()
                print(row(s),end="")
    else:
        if islist==1:
            print("</ul>")
            islist=0
        if ispara==1:
            print("</p>")
            ispara=0
if islist==1:
    print("</ul>")
    islist=0
if ispara==1:
    print("</p>")
    ispara=0


