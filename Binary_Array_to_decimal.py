n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    c+=lst[i]*(2**(n-i-1))
print(c)