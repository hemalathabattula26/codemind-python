def palindrome(n):
    q=n
    s=0
    while(q>0):
        r=q%10
        s=s*10+r
        q=q//10
    if s==n:
        return True
    else:
        return False
n=int(input())
q=n+1
while(q):
    if(palindrome(q)==True):
        n1=q
        break
    q+=1
t=n-1
while(t):
    if(palindrome(t)==True):
        n1=t
        break
    t-=1
if n-t>q-n:
    print(q)
elif n-t<q-n:
    print(t)
else:
    print(t,q)