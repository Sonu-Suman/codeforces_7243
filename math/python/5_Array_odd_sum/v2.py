def solve(s):
    for i in s:
        if i % 2 != 0:
            return "YES"
    return "NO"


n = int(input(""))
for _ in range(n):
    a = int(input(""))
    s = [i for i in map(int, input("").split())]
    if a != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))