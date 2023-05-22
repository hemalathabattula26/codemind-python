n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    if i!=0 and i!=n-1:
        if (lst[i-1]%2!=0 and lst[i+1]%2==0) or lst[i-1]%2==0 and (lst[i+1]%2!=0):
            c+=1
    if i==0:
         if (lst[1]%2!=0 and lst[n-1]%2==0) or (lst[1]%2==0 and lst[n-1]%2!=0):
            c+=1
    if i==n-1:
         if (lst[n-2]%2!=0 and lst[0]%2==0) or (lst[n-2]%2==0 and lst[0]%2!=0):
             c+=1
print(c)