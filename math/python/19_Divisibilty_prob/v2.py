def solve(s):
    a, b = s[0], s[1]
    g = int(s[0]/s[1])
    if a % b == 0:
        return 0
    else:
        return s[1]*(g+1)-s[0]


n = int(input(""))
for _ in range(n):
    s = [i for i in map(int, input("").split())]
    print(solve(s))