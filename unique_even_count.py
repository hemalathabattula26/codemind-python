n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    if i%2==0:
        if i in lst1:
            pass
        else:
            lst1.append(i)
print(len(lst1))