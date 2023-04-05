s=input()
l=len(s)
def f(s):
    dp = [[0 for i in range(l + 2)] for j in range(l + 2)]
    dp[0][0]=1
    for i in range(1,l+1):
        if s[i]=='(':
            for j in range(1,l+1):
                dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][0]=(dp[i-1][0]+dp[i-1][1])%1000000007
            for j in range(1,l+1):
                dp[i][j]=(dp[i-1][j+1]+dp[i][j-1])%1000000007
    for i in range(l+1):
        if dp[l][i]:
            return dp[l][i]
    return -1
s=" "+s
num1=f(s)
s1=" "
s=s[::-1]
for ch in s:
    if ch=='(':
        s1+=')'
    else:
        s1+='('

num2=f(s1)
print(num1*num2%1000000007)
