n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    if lst[i]%2==0:
        print(lst[i],end=' ')
for i in range(n):
    if lst[i]%2!=0:
        print(lst[i],end=' ')