def prime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
    if(c==0):
        return True
    else:
        return False
n=int(input())
if prime(n)==True:
    print(0)
else:
    q=n-1
    while(q>0):
        if(prime(q)==True):
            s=q
            break
        q=q-1
    t=n+1
    while(t>0):
        if(prime(t)==True):
            u=t
            break
        t=t+1
    if n-s > u-n:
        p=u
    else:
        p=s
    print(abs(n-p))