n=int(input())
q=n
l=1
lst=[]
while(q>9):
    l+=1
    q=q//10
while(n):
    r=n%10
    lst.append(r)
    n=n//10
s=set(lst)
if l==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")