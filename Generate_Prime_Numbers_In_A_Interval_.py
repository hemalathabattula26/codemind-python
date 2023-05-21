def prime(n):
    c=0
    for i in range(2,n):
       if n%i==0:
           c+=1
    if c==0:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i)==True and i!=1:
        print(i)