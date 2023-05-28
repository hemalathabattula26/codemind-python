n=int(input())
lst=list(map(int,input().split()))
lst1=[]
c=0
for i in lst:
    if i in lst1:
        pass
    else:
        lst1.append(i)
for i in lst1:
    print(i,end=' ')