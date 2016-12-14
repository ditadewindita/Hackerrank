#!/bin/python3

import sys


s = input().strip()
c = 1
for a in range(len(s)):
    if s[a].isupper():
        c += 1
print(c)