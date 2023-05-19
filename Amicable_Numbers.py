n=int(input())
m=int(input())
t=0
a=0
for j in range(1,n):
    if n%j==0:
        t+=j
for j in range(1,m):
    if m%j==0:
        a+=j
if m==t and n==a:
    print("Amicable")
else:
    print("Not Amicable")