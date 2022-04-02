def solve(s):
    for i in reversed(range(s[2]+1)):
        if i % s[0] == s[1]:
            return i


n = int(input(""))
for _ in range(n):
    s = [i for i in map(int, input("").split())]
    print(solve(s))