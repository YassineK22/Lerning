# Ecrit ton programme ici ;-)
weight=float(input("Weight: "))
KL='O'
while (KL.upper() !='K' and KL.upper() !='L'):
    KL=input('(K)g or (L)bs: ')
if (KL.upper() =='K'):
    print('Weight in Lbs: ', weight*2.20462)
else :
    print('Weight in Kg: ', weight/2.20362)
