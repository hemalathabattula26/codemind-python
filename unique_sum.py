n=int(input())
lst=list(map(int,input().split()))
dict={}
sum=0
for i in lst:
    if i not in dict:
        sum+=i
        dict[i]=1
print(sum)
        