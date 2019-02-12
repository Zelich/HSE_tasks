sas = input()
s = input()
t = input()
b = []
for i in t:
    b.append(0)
j = 0
for letter in t:
    while True:
        if s[j] == letter:
            j += 1
            break
        j += 1
        if j == len(s):
            print("No")
            exit()
print("Yes")