def solve(s):
    su = sum(s)
    if su % 2 == 0:
        return "NO"
    else:
        return "YES"


n = int(input("Enter your number: "))
for _ in range(n):
    a = int(input("Enter your number: "))
    s = [i for i in map(int, input("Enter your number: ").split())]
    if a != len(s):
        print(f"You give wrong input.")
    else:
        print(solve(s))