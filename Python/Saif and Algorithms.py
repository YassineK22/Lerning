n=int(input())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
r=set(a)
d=dict()
for i in r:
    d[i]= []
for i in range(len(a)):
    d[a[i]].append((c[i]))
s=0
for i in r:
    s+=min(d[i])
print(len(r))
print(s)