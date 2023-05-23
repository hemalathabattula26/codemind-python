n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    if lst[i]%2!=0:
        if i%2!=0:
           c=c+1
if c==n//2:
    print(True)
else:
    print(False)