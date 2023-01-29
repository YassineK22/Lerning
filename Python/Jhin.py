n=int(input())
s=''
for i in range(n):
    a = int(input())
    if(a%4==0):
        s=s+"BOB "
    else:
        s=s+"ALICE "
res=list(map(str,s.split()))
print(*res)