def solve(s):
    a, b = s[0], s[1]
    if a % b == 0:
        return 0
    else:
        j = 0
        while a % b != 0:
            a += 1
            j += 1
        return j


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))