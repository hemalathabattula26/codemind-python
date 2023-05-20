n=int(input())
q=n
c=0
while(q>0):
    c+=1
    q=q//10
u=n
s=0
while(u>0):
    r=u%10
    s=s+r**c
    c-=1
    u=u//10
if n==s:
    print(True)
else:
    print(False)