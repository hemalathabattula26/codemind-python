n=int(input())
c=0
lst=list(map(int,input().split()))
for i in range(n):
    if i % 2!=0:
        c+=lst[i]
print(c)