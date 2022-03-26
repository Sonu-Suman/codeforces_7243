def solve(s):
    step = [1, 2, 3, 4, 5]
    if s <= 5:
        return 1
    else:
        st = s//step[4]
        return st + 1


s = int(input("Enter your number: "))
print(solve(s))