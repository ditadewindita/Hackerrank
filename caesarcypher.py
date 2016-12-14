#!/bin/python3

import sys

def f(c, k):
    a = ord('A')
    if s[i].islower():
        a = ord('a')
    return str(chr(a + (ord(s[i]) - a + k) % 26))

n = int(input().strip())
s = input().strip()
k = int(input().strip())

for i in range(n):
    if s[i].isalpha():
        s = s[:i] + f(s[i], k) + s[i+1:]
print(s)