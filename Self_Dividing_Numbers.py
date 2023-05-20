a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    t=0
    q=i
    while(q!=0):
       c+=1
       r=q%10
       q=q//10
       if r!=0 and i%r==0:
           t=t+1
    if c==t:
        print(i,end=' ')