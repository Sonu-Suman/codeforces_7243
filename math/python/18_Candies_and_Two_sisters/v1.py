def solve(s):
    if s[0] <= 2:
        return 0

    d = int(s[0]/2)+1
    return s[0]-d


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    print(solve(s))