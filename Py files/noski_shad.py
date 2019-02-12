n = int(input())
l = list(map(int, input().split()))
m = int(input())
r = list(map(int, input().split()))
diff = []
for i in range(len(l)):
    diff.append((10000001, 0, 0))
i = 0
j = 0

while True:
    if l[i] < r[j]:
        if r[j]-l[i] < diff[i][0]:
            diff[i] = r[j]-l[i], i, j
        i += 1
    # учесть предыдущую разницу
    elif l[i] > r[j]:
        if l[i]-r[j] < diff[i][0]:
            diff[i] = l[i]-r[j], i, j
        j += 1
    else:
        print(l[i], r[j])
        exit()
    if i == len(l) or j == len(r):
        break
minv = 10000001
ind = 0
for i in range(len(diff)):
    if diff[i][0] < minv:
        ind = i
        minv = diff[i][0]
print(l[diff[ind][1]], r[diff[ind][2]])
