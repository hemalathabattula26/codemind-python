n=int(input())
lst=list(map(int,input().split()))
c=0
c1=0
for i in lst:
    c+=i
x=c//n
for i in lst:
    if i>=x:
        c1+=1
print(c1)