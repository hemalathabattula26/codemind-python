n=int(input())
lst=list(map(int,input().split()))
c=0
c1=0
for i in range(n//2):
    c+=lst[i]
for i in range(n//2,n):
    c1+=lst[i]
print(c1-c)