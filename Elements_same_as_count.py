n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    if i==lst.count(i):
        if i in lst1:
            pass
        else:
            lst1.append(i)
        # lst.pop(i)
if len(lst1)==0:
    print(-1)
else:
    for i in lst1:
        print(i,end=' ')