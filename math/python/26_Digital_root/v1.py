import math

def solve(s):
    l = []
    for i in range(int(math.pow(10, 12))):
        k = [int(j) for j in str(i)]
        if s[1] == sum(k):
            l.append(int(i))
            if len(l) == s[0]:
                return l[(s[0]-1)]
        elif sum(k) in l:
            l.append(i)
            if len(l) == s[0]:
                return l[(s[0]-1)]



n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))
