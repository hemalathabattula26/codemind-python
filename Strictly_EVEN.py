n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    if lst[i]%2==0 or lst[i]==0:
        if i%2==0 or i==0:
           c+=1
if n%2!=0:
    if c==(n//2)+1:
        print(True)
    else:
        print(False)
if n%2==0:
    if c==(n//2):
        print(True)
    else:
        print(False)