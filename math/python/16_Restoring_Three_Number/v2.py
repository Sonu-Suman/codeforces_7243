def solve(s):
    s.sort(reverse=False)
    if s[0] == s[1] == s[2]:
        a = int(s[0] / 2)
        return a, a, a

    for i in range(s[0] + 1):
        a = i
        b = s[0] - 1
        for j in range(a, s[1] + 1):
            c = s[1] - a
            if ((a + b + c) == s[3]) and (b+c == s[2]):
                return a, b, c


s = [i for i in map(int, input("Enter your number: ").split())]
print(solve(s))