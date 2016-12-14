
s = input().strip()
i = 0
p = True

def f(s):
    for a in range(len(s)):
        if s.count(s[a]) > 1:
            return True
    return False

while i < len(s) and f(s):
    if i < len(s)-1 and s[i] == s[i+1]:
        s = s[:i] + s[i+2:]
        i = 0
    else:
        i += 1
if s == "":
    print("Empty String")
else:
    print(s)