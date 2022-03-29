def solve(l):
    if l[0] + l[1] == l[2]:
        return "YES"

    if l[0] == l[1] == 0 and l[2] == 2:
        return "YES"

    return "NO"


s = [i for i in map(int, input("Enter your numbers: ").split())]
print(solve(s))