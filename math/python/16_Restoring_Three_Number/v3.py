def solve(s):
    s.sort(reverse=False)
    if s[0] == s[1] == s[2]:
        a = int(s[0] / 2)
        g = [str(a), str(a), str(a)]
        return ' '.join(g)

    for i in range(s[0] + 1):
        a = i
        b = s[0] - 1
        for j in range(a, s[1] + 1):
            c = s[1] - a
            if ((a + b + c) == s[3]) and (b+c == s[2]):
                l = [str(a), str(b), str(c)]
                return ' '.join(l)


s = [i for i in map(int, input("").split())]
print(solve(s))