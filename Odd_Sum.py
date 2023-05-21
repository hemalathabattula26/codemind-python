n=int(input())
c=0
lst=list(map(int,input().split()))
for i in lst:
    if i%2!=0:
        c+=i
print(c)