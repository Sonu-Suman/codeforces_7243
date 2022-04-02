def solve(a, s):
    s.sort(reverse=True)
    d0 = (a[1]//a[2])-1
    return s[1]*d0 + s[0]*(a[1]-d0)


a = [i for i in map(int, input("").split())]
s = [i for i in map(int, input("").split())]
print(solve(a, s))