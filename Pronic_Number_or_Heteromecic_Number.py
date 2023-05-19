import math
n=int(input())
x=int(math.sqrt(n))
if x*(x+1)==n:
    print("YES")
else:
    print("NO")