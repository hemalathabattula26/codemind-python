n=int(input())
lst=list(map(int,input().split()))
c=1
for i in lst:
    if i%2!=0:
        c=0
        break
if c:
    print(True)
else:
    print(False)