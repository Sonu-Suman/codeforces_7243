import math

def solve(a, s):
    k = [0]
    m = [s[0] % 2]
    if a == 1:
        if k == m:
            return 0
        else:
            return -1

    j = 0
    for i in range(1, len(s)):
        if k[-1] != m[-1]:
            j += 1
        k.append(i % 2)
        m.append(s[i] % 2)
    if k[-1] != m[-1]:
        j += 1
    
    if j%2==0:
        if int(len(s)/2)>=j:
            return int(j/2)
    return -1


n = int(input(""))
for _ in range(n):
    a = int(input(""))
    s = [i for i in map(int, input("").split())]
    print(solve(a, s))