def solve(s, l):
    j = 0
    if len(l) == 1:
        return 1

    k = []
    l.sort(reverse=False)
    print(l)
    for i in min(l):
        k.append(i)
        l.remove(i)
        if sum(k) > l[-1]:
            k.remove(i)
            if l[0] > i:
                pass
            elif sum(k) == s:
                return len(k)


n = int(input("Enter your number: "))
l = []
for _ in range(n):
    # a = int(input("Enter your number: "))
    s = [i for i in map(int, input("Enter your list number: ").split())]
    l.append(s[0])
    # if 2 != len(s):
    #     print("You give wrong input.")
    # else:
    #     print(solve(s))
    print(solve(s, l))