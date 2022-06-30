a = [3,3,4,2,4,4,2,4,4]
b = []
x = []
for i in range(len(a)-1):
    c = 1
    if a[i] in b:
        continue
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            c += 1
    b.append(a[i])
    x.append(c)

maximum = max(x)
i = x.index(maximum)
print(b[i])
