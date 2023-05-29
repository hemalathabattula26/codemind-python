n=int(input())
lst=list(map(int,input().split()))
t=int(input())
for i in range(n):
    if lst[i]==t:
        u=i
c=0
for i in range(u+1):
    c+=lst[i]
print(c)