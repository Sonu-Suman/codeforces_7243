def solve(s):
    if s[0] == 1:
        return 0
    elif s[0] == 2:
        return s[1]
    elif (s[0] == s[1]) and (s[0]>2):
        return 2*s[1]




n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))