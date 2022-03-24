def finding_Charger_power(n, k, l, m):
    s = []
    for j in range(k - 1):
        for i in range(n):
            s.append(l[i] - m[i])

        # This is for when no available any positive answer
        s.sort(reverse=False)
        s = s[:2]
        j = 0
        for i in s:
            if i < 0:
                j += 1
                if j > 1:
                    return -1

        r = s.index(min(s))

    return s[r]


n, k = map(int, input("Enter your number: ").split())

l = [i for i in map(int, input("Enter your numbers: ").split())]
m = [j for j in map(int, input("Enter your numbers: ").split())]
print(finding_Charger_power(n, k, l, m))
"""
l = []
for _ in range(n):
    l.append(int(input("Enter your number: ")))

m = []
for _ in range(n):
    m.append((int(input("Enter your number: "))))

"""
