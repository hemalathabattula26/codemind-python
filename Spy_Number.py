n=int(input())
s=0
p=1
q=n
while(q):
    r=q%10
    s=s+r
    q=q//10
t=n
while(t):
    r1=t%10
    p=p*r1
    t=t//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")