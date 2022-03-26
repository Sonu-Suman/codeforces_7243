
def solve(s):
    f = s[0] / 2
    if f % 2 == 0:
        l = []
        for i in range(2, s[0] + 1):
            if i % 2 == 0:
                l.append(i)
        su = sum(l)
        n = 1
        for j in range(int(f)):
            if j == int(f-1):
                su2 = sum(l[int(f):])
                su1 = su - su2
                if su1 % 2 != 0:
                    l.append(su1)
                    return "YES", l
                else:
                    return "NO"
            l.append(n)
            n += 2

    elif f % 2 != 0:
        return "NO"


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    print(solve(s))