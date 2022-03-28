def solve(s):
    dic = {1: 15, 2: 16, 3: 17, 4: 18, 5: 19, 6: 20}

    for key, value in dic.items():
        g = s // 14
        su = 14 * (g - 1)
        if (s - su) == value:
            return "YES"
    return "NO"



a = int(input("Enter your number: "))
s = [i for i in map(int, input("Enter your list number: ").split())]
if a != len(s):
    print("You give wrong input.")
else:
    for i in s:
        print(solve(i))