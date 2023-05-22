n=int(input())
lst=list(map(int,input().split()))
c=1
for i in lst:
    if i!=0 and i!=1:
        c=0
if(c):
    print(True)
else:
    print(False)