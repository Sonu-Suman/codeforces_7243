def solve(s):
    if s[0] == s[1] == s[2]:
        s4 = s[3] / 3
        if int(s4) == s4:
            return "YES"
        else:
            return "NO"

    n = s[3]
    c = s[:3]
    c.sort(reverse=False)

    if c[0] < c[2]:
        c1 = c[2] - c[0]
        if c[1] < c[2]:
            c2 = c[2] - c[1]

            c[0] = c[0] + c1
            c[1] = c[1] + c2
            su = c1 + c2
            n -= su
            check = n / 3
            if int(check) == check:
                return "YES"
        elif c[1] == c[2]:
            c[0] = c[0] + c1
            n -= c1
            check = n/3
            if int(check) == check:
                return "YES"

    return "NO"


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 4 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))