#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a = [a0, a1, a2]
b = [b0, b1, b2]

ac = 0
bc = 0

for i in range(0, 3):
    if a[i] > b[i]:
        ac += 1
    elif a[i] < b[i]:
        bc += 1
print(ac, bc)