n=int(input())
s=''
for i in range(n):
    a = int(input())
    print("BOB" if a%4==0 else "ALICE")
