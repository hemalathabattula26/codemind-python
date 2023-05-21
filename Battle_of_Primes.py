def prime(n):
    c=0
    for i in range(2,n):
       if n%i==0:
           c+=1
    if c==0:
        return True
    else:
        return False
n1=int(input())
n2=int(input())
q=n1+n2+1
while(q):
    if(prime(q)):
        s=q
        break
    q=q+1
print(s-n1-n2)