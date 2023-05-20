def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
if(prime(n) == True):
    c=0
    q=n
    c1=0
    while(q>0):
        c+=1
        r=q%10
        if prime(r)==True and r!=1:
            c1+=1
        q=q//10
    if c==c1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")