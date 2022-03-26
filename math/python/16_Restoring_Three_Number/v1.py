def solve(s):
    s.sort(reverse=False)
    if s[0] == s[1] == s[2]:
        a = int(s[0]/2)
        return a, a, a


s = [i for i in map(int, input("Enter your number: ").split())]
print(solve(s))