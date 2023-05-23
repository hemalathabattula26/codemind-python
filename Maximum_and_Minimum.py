n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    if i==lst.count(i):
        lst1.append(i)
if len(lst1)==0:
    print(-1)
else:
    print(min(lst1),max(lst1),end=' ')