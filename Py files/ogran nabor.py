n, c, m, k = tuple(map(int, input().split()))
a = []
fail = False
def check_validity(b, l1, l2):
    if l1 in b[1]:
        return False
    else:
        return True

for i in range(n):
    a.append([1, set(), set(), set()])
for i in range(m):
    l1, l2 = tuple(map(int, input().split()))
    a[l1-1][1].add(l2)
    a[l2-1][2].add(l1)
    for j in a[l1 - 1][2]:
        a[j - 1][1].add(l2)
        a[l2 - 1][2].add(j)
    for j in a[l2 - 1][1]:
        a[j-1][2].add(l1)
        a[l1-1][1].add(j)
for i in range(k):
    k1, k2 = tuple(map(int, input().split()))
    a[k1-1][3].add(k2)
    for j in a[k1-1][2]:
        a[k2-1][2].add(j)
        a[j-1][1].add[k2]



print("Yes")
for i in a:
    print(i[0], end=' ')