n=int(input())
lst=list(map(int,input().split()))
se=int(input())
c=0
for i in lst:
    if i==se:
        c=lst.count(i)
        break
print(c)