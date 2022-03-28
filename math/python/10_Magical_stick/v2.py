def solve(s, li):
    l = li.copy()
    if len(l) <= 2:
        return 1

    k = []
    l.sort(reverse=False)
    for i in range(len(l)):
        k.append(l[0])
        l.remove(l[0])
        if sum(k) == s:
            return len(k), k
        if sum(k) > s:
            for _ in range(1, len(k)+1):
                di = k[-1]
                k.remove(di)
                l.append(di)
                num = s - sum(k)
                if num in l:
                    return len(k), k
    return 1


n = int(input("Enter your number: "))
l = []
for _ in range(n):
    a = int(input("Enter your number: "))
    l.append(a)
    print(solve(a, l))


"""
This is not perform right on this data.py

l = [2, 65, 4, 3, 9, 48, 23, 7]
print(solve(29, l))
"""
