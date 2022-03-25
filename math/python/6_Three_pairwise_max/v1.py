def solve(s):
    if s[0] == s[1] == s[2]:
        return "YES", s[0], s[0], s[0]

    if s[0] == s[1]:
        a = s[0]
        if s[1] < s[2]:
            return "NO"
        elif s[1] > s[2]:
            b = s[1]
            c = s[2] - 1
            return "YES", a, b, c

    elif s[0] == s[2]:
        b = s[0]
        if s[1] < s[2]:
            a = s[1]
            c = s[1] - 1
            return "YES", a, b, c
        elif s[1] > s[2]:
            return "NO"

    elif s[1] == s[2]:
        c = s[1]
        if s[0] < s[2]:
            a = s[0]
            b = s[0] - 1
            l = [a, b, c]
            if l.count(0) > 0:
                l.remove(0)
                l.append(1)

            return "YES", l
        elif s[0] > s[2]:
            return "NO"

    return "NO"


n = int(input("Enter your number: "))
for _ in range(n):
    # a = int(input("Enter your number: "))
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 3 != len(s):
        print("You give wrong input number.")
    else:
        print(solve(s))