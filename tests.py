a = "staggering"
b = a
c = a

for i in a:
    print(a)
    a = a[:-1]

for j in b:
    print(b)
    b = b[1:]

for k in c:
    print(c)
    c = c[:-1]
    c = c[1:]

