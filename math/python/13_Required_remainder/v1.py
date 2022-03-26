def solve(s):
    for i in range(s[2]+1):
        if (s[2] - i) % s[0] == s[1]:
            return s[2]-i


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 3 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))