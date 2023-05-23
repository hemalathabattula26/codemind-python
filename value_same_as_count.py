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
print(len(lst1))