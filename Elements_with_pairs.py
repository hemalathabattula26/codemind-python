n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    print(lst[i],end=' ')
if n%2==0:
    pass
else:
    print(0)