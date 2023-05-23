n=int(input())
lst=list(map(int,input().split()))
k=int(input())
lst1=[]
for i in lst:
    if lst.count(i)==k:
        if i in lst1:
            pass
        else:
            lst1.append(i)
if len(lst1)==0:
    print(-1)
else:
    for i in lst1:
        print(i,end=' ')