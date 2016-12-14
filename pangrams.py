# 97 - 122
s = input().strip().lower()
ret = "pangram"
for i in range(97, 123):
    if chr(i) not in s:
        ret = "not " + ret
        break
print(ret)