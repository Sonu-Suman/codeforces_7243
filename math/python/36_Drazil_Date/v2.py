def solve(l):
    if l[0]!=l[1]:
        if l[0] + l[1] == l[2]:
            return "YES"

    if l[0] == l[1]:
        if (l[0]+l[1]+2)==l[2]:
            return "YES"

    return "NO"


s = [i for i in map(int, input("").split())]
print(solve(s))