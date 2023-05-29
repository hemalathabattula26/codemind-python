n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    if i in lst1:
        pass
    else:
        lst1.append(i)
        print(i,end=' ')
        print(lst.count(i),end=' ')