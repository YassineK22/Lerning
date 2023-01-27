# Ecrit ton programme ici ;-)
list1= ['Minecraft',10,'CallOfDuty',7.7,'Lol',7.9,'valorant',4.6]
print(list1[0:4])
print("Update")
list2 = list1
list2.append("END")
list2.insert(1,"Minecraft")
list2.insert(0,"Start")
list2[2] = 9.7
print(list2)
print("Is lol is the list")
print("Lol" in list2)
print("Remove lol and the rate from the list")

list2.remove("Lol")
list2.remove(7.9)
print(list2)
print("We have ",len(list2)," in our list")
print()
print("-----------------------")
for i in list2:
    print(i)
print("-----------------------")
