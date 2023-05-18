def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n,1,-1):
        if prime(i)==True:
            r=i
            break
    for j in range(n,n*n):
        if prime(j)==True:
            u=j
            break
    if n-r>u-n:
        print(u)
    else:
        print(r)
        