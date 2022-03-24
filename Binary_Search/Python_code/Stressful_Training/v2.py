def finding_Charger_power(n, k, l, m):
    s = []
    for j in range(k - 1):
        for i in range(n):
            s.append(l[i] - m[i])

        # This is for when no available any positive answer
        c = s.copy()
        c.sort(reverse=False)
        if s[1] < 0:
            return -1

        r = s.index(min(s))

    return s[r]


n, k = map(int, input("Enter your number: ").split())

l = [i for i in map(int, input("Enter your numbers: ").split())]
m = [j for j in map(int, input("Enter your numbers: ").split())]
print(finding_Charger_power(n, k, l, m))
