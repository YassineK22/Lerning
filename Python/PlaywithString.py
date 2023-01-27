s = 'H!e ldllor oW'
#Dedcode
a = s[::2]
if len(s)%2: s=s[:-1]
b= s[::-2]
print(a+b)

#The same
"""s = input()
c=''
test = True
for i in s:
    if test:
        c+=i
        test = False
    else:
        test = True

for i in range(len(s)-1,0,-1):
    if test:
        c+=s[i]
        test = False
    else:
        test = True
print(c)"""