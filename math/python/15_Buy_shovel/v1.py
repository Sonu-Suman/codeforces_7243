def solve(s):
    f = []
    for i in range(1, 10):
        d = s[0]*i
        f.append(str(d))


    for j in range(len(f)):
        if int(f[j][-1]) == s[1]:
            return j+1

    for j in range(len(f)):
        if int(f[j][-1]) < s[1]:
            if j > 0:
                return j+1

    k = str(s[0])
    if int(k[-1]) == 0:
        return 9



s = [i for i in map(int, input("Enter your number: ").split())]
print(solve(s))