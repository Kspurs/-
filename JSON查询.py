n,m1=map(int,input().split())
jsonstr=""
for i in range(n):
    tmpstr=input()
    j=0
    while j<len(tmpstr):
        if tmpstr[j]=="\\":
            jsonstr+=tmpstr[j+1]
            j+=1
        elif tmpstr[j]!=' ':
            jsonstr+=tmpstr[j]
        j+=1
m={}

def f(s,pre):
    i=1
    while i<len(s)-1:
        if s[i]=='"':
            key=""
            i+=1
            while s[i]!='"' or s[i+1]!=':':
                key+=s[i]
                i+=1
            i+=2
            if s[i]=='"':
                value=""
                i+=1
                while s[i] != '"' or s[i+1]!=',' and s[i+1]!='}':
                    value += s[i]
                    i += 1
                m[pre+key]=value
            else:
                tmp='{'
                left=1
                j=i+1
                while left>0:
                    if s[j]=='}':
                        left-=1
                    tmp+=s[j]
                    j+=1
                f(tmp,pre+key+'.')
                m[pre+key]=-1
                i=j
        i+=1
f(jsonstr,"")
ans=[]
for i in range(m1):
    q=input()
    if q in m and m[q]==-1:
        ans.append("OBJECT")
    elif q in m:
        ans.append("STRING"+" "+m[q])
    else:
        ans.append("NOTEXIST")
for _ in ans:
    print(_)