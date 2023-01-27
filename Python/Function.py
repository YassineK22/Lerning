# Ecrit ton programme ici ;-)
# Ecrit ton programme ici ;-)
from pickle import*
from numpy import*
def convb_10(b1,ch):
    s=0
    p=1
    for i in range(len(ch)-1,-1,-1):
        if(ch[i]>="0" and ch[i]<="9" ):
            s+=int(ch[i])*p
        else:
            s+=(ord(ch[i])-55)*p
        p=p*b1
    return s
def conv10_b(n,b1):
    ch=""
    while not n==0:
        r=n%b1
        if r<10:
            ch=str(r)+ch
        else:
            ch=chr(r+55)+ch
        n=n//b1
    return ch
def trie():
    n=len(t)
    for i in range(n):
        for j in range(n-1-i):
            if t[j]>t[j+1]:
                t[j],t[j+1]=t[j+1],t[j]
def trie():
    test=True
    while not test==False:
        test=False
        for i in range(n-1):
            if t[i]>t[i+1]:
                t[i],t[i+1]=t[i+1],t[i]
                test=False
def f(x):
    return x*x
def retangle(a,b,n):
    h=(b-a)/n
    x=a+h/2
    s=0
    for i in range(n):
        s+=f(x)
        x=x+h
    return s*h
def trapeze(a,b,n):
    h=(b-a)/n
    x=a
    s=0
    for i in range(n):
        s+=(f(x)+f(x+h))/2
        x+=h
    return s*h
def premier(x):
    test=True
    for i in range(2,x//2+1):
        if x%i==0:
            test=False
    return test
def factorile(x):
    p=2
    ch=""
    while not x==1:
        if (x%p==0):
            ch+=str(p)+"*"
            x=x//p
        else:
            p+=1
    ch=ch[:-1]
    return ch
print(factorile(12))

