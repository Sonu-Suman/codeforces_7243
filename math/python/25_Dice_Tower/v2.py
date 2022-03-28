import math


def solve(s):
    dic = {1: 15, 2: 16, 3: 17, 4: 18, 5: 19, 6: 20}

    d = math.ceil(s/20)
    for k in range(1, 7):
        va = [dic[k]]
        # print(va)
        if va[0] == s:
            return "YES"
        if d > 1:
            for j in range(d-1):
                for key, value in dic.items():
                    su = 0
                    if len(va)>1:
                        if (va[-1]-va[-2]) == value:
                            su += (va[-1]-key)
                    else:
                        if va[-1] == value:
                            su += (va[-1]-key)
                    for values1 in dic.values():
                        fu = su + values1
                        if fu == s:
                            return "YES"
                        va.append(fu)
            if s in va:
                return "YES"
            else:
                return "NO"



a = int(input("Enter your number: "))
s = [i for i in map(int, input("Enter your list number: ").split())]
if a != len(s):
    print("You give wrong input.")
else:
    for i in s:
        print(solve(i))