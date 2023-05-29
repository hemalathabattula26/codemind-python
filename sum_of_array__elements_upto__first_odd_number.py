n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i % 2 !=0:
        break
    c+=i
print(c)