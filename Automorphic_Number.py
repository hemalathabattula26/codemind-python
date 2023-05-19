n=int(input())
s=n**2
l=0
l1=0
q=n
while(q>9):
    l+=1
    q=q//10
sq=s
while(sq>9):
    l1+=1
    sq=sq//10
t=1
u=1
for i in range(l+2):
    t*=10
for i in range(l1+2):
    u*=10
x=u/t
r=s%x
if n==r:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")