def firstmins(b, m):
    i = 0
    while i < len(b):
        if b[i] != m:
            break
        i += 1
    return i

def lastmins(b, m):
    i = len(b)-1
    while i >= 0:
        if b[i] != m:
            break
        i -= 1
    return i

n = int(input())
a = list(map(int, input().split()))
h = 0

while len(a) > 0:
    if len(a) == 1:
        h += 1
        break
    m = min(a)
    if a[-1] != m:
        a = a[:-1]
    elif a[0] != m:
        a = a[1:]
    else:
        fm = firstmins(a, m)
        lm = lastmins(a, m)
        if fm > lm:
            h += 1
            break
        if fm <= len(a) - lm - 1:
            a = a[fm+1:]
        else:
            a = a[:lm-1]
    h += 1
print(h)