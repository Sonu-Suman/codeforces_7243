def solve(s):
    a, b = s[0], s[1]
    if a == b:
        return 0
    if (a > b) or (b > a):
        dif = abs(a - b)
        if dif <= 9:
            return 1
        if dif > 9:
            if dif % 10 == 0:
                return int(dif/10)
            else:
                return (dif//10)+1






n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))