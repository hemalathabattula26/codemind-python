def primes(n):
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
k=int(input())
t=0
for i in lst:
    if primes(i)==True and i<=k:
        t+=1
print(t)