def toformat(q):
    if q < 10:
        return "0" + str(q)
    else:
        return str(q)

m0 = int(60)
h0 = 60 * m0
d = h0 * 24
n = int(input()) % d
h = n // h0
n = n % h0
m = n // m0
s = n % m0
print(str(h)+":"+toformat(m)+":"+toformat(s))
