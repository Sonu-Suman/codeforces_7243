def solve(s):
    re = s[2]%s[0]

    if re==s[1]:
        return s[2]

    if re > s[1]:
        return s[2]-(re-s[1])
    else:
        return s[2]-(s[0]-(s[1]-re))


n = int(input(""))
for _ in range(n):
    s = [i for i in map(int, input("").split())]
    print(solve(s))