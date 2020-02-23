a = [10, 7, 5, 4]

while True:
    m = max(a)
    index = a.index(m)
    a = [x + 1 for x in a]
    a[index] -= 4
    print(a)

