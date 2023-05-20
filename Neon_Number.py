n=int(input())
s=n*n
sq=s
t=0
while(sq):
    r=sq%10
    t=t+r
    sq=sq//10
if n==t:
    print("Neon Number")
else:
    print("Not Neon Number")