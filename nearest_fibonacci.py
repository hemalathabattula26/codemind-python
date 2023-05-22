def fibonacci(n):
    a=0
    b=1
    cnt=0
    for i in range(1,n+1):
        c=a+b
        if c==n:
            cnt+=1
        a=b
        b=c
    if cnt!=0:
        return True
    else:
        return False
n=int(input())
q=n-1
r=n+1
while(q):
    if fibonacci(q):
        a=q
        break
    q=q-1
while(r):
    if fibonacci(r):
        u=r
        break
    r=r+1
if(n-q<r-n):
    print(q)
elif(n-q>r-n):
    print(r)
else:
    print(q,r)