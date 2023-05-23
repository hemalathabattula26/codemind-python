n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in range(n):
    if lst[i]==lst.count(lst[i]):
        lst1.append(lst[i])
if len(lst1)==0:
    print(-1)
else:
    print(min(lst1),max(lst1),end=' ')