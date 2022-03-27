def solve(a, s):
    s.sort(reverse=True)
    d0 = int(a[1]/a[2])-1
    return s[1]*d0 + s[0]*(a[1]-d0)


a = [i for i in map(int, input("Enter your numbers: ").split())]
s = [i for i in map(int, input("Enter your list number: ").split())]
if a[0] != len(s):
    print("You give wrong input.")
else:
    print(solve(a, s))