'''
f = open('output.txt', 'r')
n = int(f.readline())
a = list(map(int, f.readline().split()))
'''
n = int(input())
a = list(map(int, input().split()))
b = False
maxs = 1
for d in range(1, n):
    res = []
    j = 0
    for i in range(n-1, -1, -1):
        if j - d < 0:
            res.append(a[i])
        else:
            res.append(max(a[i] + res[j-d], a[i]))
        if b:
            maxs = max(maxs, res[-1])
        else:
            maxs = res[-1]
            b = True
        j += 1
    print(res)

print(maxs)


