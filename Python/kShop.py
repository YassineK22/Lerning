import math
n=int(input())
a,*shop = list(map(int,input().split()))
s=0
shop=shop[:-1]
for i in range(len(shop)-1,0,-1):
    s+=abs(shop[i]-shop[i-1])
s=s-1
print(s)

