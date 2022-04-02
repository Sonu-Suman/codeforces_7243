def solve(l):
    su = []
    for i in range(3):
        for j in range(len(l)):
            su.append(l[j][i])
        if sum(su) != 0:
            return "NO"
    return "YES"



n = int(input(""))
l = []
for _ in range(n):
    l.append([i for i in map(int, input("").split())])

    
print(solve(l))