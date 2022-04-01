def solve(l, s):
    g = [l, s]
    st0 = g[0].count(g[0][0])
    st1 = g[1].count(g[1][0])
    st = st1+st0
    s = [len(l), len(s)]
    su = sum(s)

    ma = max(s)
    mi = min(s)
    ind = s.index(mi)

    if su == st:
        return g[s.index(ma)]*mi

    if ma % mi == 0:
        d = int(ma / mi)
        j = 0
        for i in range(1, d + 1):
            if l[j:i * mi] != g[ind]:
                return -1
            j = i * mi
        return g[s.index(ma)]
    return -1


for i in range(int(input("Enter your number: "))):
    l = input("Enter your string: ")
    s = input("Enter your second string: ")
    print(solve(l, s))