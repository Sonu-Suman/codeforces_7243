def solve(s):
    area = s[0]*s[1]
    return int(area/2)


s = [i for i in map(int, input("Enter your number: ").split())]
print(solve(s))