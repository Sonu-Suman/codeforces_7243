import math

def solve(s):
    return math.ceil((s[0]*s[1])/2)


n = int(input("Enter your number: "))
for _ in range(n):
    # a = int(input("Enter your number: "))
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print(f"You give wrong input.")
    else:
        print(solve(s))