import math


def solve(s):
    dic = {1: 15, 2: 16, 3: 17, 4: 18, 5: 19, 6: 20}

    # for i in s:
    d = math.ceil(s/20)
    for k in range(1, 7):
        su = 0
        for j in range(d):
            if j == 0:
                su += dic[k]
                if s == su:
                    return "YES"
            else:
                # print(su)
                # After this line code is wrong.
                va = [su]
                for n in range(1, 7):
                    for key, value in dic.items():
                        if len(va) > 1:
                            if value == (va[-1]-va[-2]):
                                su += (dic[n]-key)
                                va.append(su)
                                if s == su:
                                    return "YES"
                        else:
                            if value == va[-1]:
                                su += (dic[n]-key)
                                va.append(su)
                                if s == su:
                                    return "YES"
    return "NO"


a = int(input("Enter your number: "))
s = [i for i in map(int, input("Enter your list number: ").split())]
if a != len(s):
    print("You give wrong input.")
else:
    for i in s:
        print(solve(i))