
def solve(l, m):
    if (4 >= l >= m) or (4 >= l > 1 and m == 3):
        return "YES"

    if m > l >= 5:
        return 'YES'

    return "NO"



n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s[0], s[1]))