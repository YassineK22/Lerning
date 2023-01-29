#Advantages
for __ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    max1=max(a)
    max2=sorted(a)[-2]
    print(*(x-max1 if x!=max1 else x-max2 for x in a))
#BlockTwoer
for __ in range(int(input())):
    n=int(input())
    a,*b=map(int,input().split())
    b.sort()
    for x in b:
        if(x>a):
            a+=(x-a+1)//2
 
    print(a)    
#GDC partition
import math
for __ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    acc=0
    ans=0
    for i in range(n-1):
        acc+=a[i]
        ans=max(ans,math.gcd(acc,s-acc))
    print(ans) 
# Gardener and the Capybaras (easy version)
for __ in range(int(input())):
    s=input()
    if (s[1]=='a'):
        print(s[0],s[1],s[2:])
    else:
        print(s[0],s[1:len(s)-1],s[-1])

#HAytou
for __ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    even=[]
    odd=[]
    for i in range(0,n):
        if (a[i]%2==0):
            even.append(i+1)
        else:
            odd.append(i+1)
        
    if (len(odd)>=3):
        print("YES")
        print(odd[0],odd[1],odd[2])
    elif( len(odd)>=1 and len(even)>=2):
        print("YES")
        print(odd[0],even[0],even[1])
    else:
        print("NO")