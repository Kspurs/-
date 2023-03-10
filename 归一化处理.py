n=int(input())
nums=list(map(int,input().split()))
mean=sum(nums)/len(nums)
d=(sum([(nums[i]-mean)**2 for i in range(len(nums))])/len(nums))**0.5
for _ in nums:
    print((_-mean)/d)