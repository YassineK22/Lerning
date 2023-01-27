import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

nb_tree = int(input())
nb_water = int(input())
size = int(input())
water = []
tree = []
for i in range(nb_tree):
    tree.append(([int(j) for j in input().split()]))
for i in range(nb_water):
    water.append(([int(j) for j in input().split()]))
for i in range(size):
    row=[]
    for j in range(size):
        c = "."
        if [i, j] in tree:
            c = "+"
        if [i, j] in water:
            c = "#"
        row.append(c)
    print(" ".join(row))

