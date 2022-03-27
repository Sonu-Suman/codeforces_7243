def solve(s):
    max_t = (s[0] + s[1]) / s[2]
    c = s[:2]
    c.sort(reverse=False)
    if int(c[0] / s[2]) != (c[0] / s[2]):
        if int(c[1]/s[2]) != (c[1]/s[2]):
            d = c[1] - (s[2] * int(c[1] / s[2]))
            return int(max_t), s[2]-d
    return int(max_t), 0


s = [i for i in map(int, input("Enter your number: ").split())]
print(solve(s))