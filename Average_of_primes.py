def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
lst=list(map(int,input().split()))
c,c1=0,0
for i in lst:
    if prime(i):
        c+=1
        c1+=i
print("%.2f"%(c1/c))