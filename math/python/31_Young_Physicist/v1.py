def solve(l):
    su = []
    for i in range(3):
        for j in range(len(l)):
            su.append(l[j][i])
        if sum(su) != 0:
            return "NO"
    return "YES"




n = int(input("Enter your number: "))
l = []
for _ in range(n):
    l.append([i for i in map(int, input("Enter your list number: ").split())])

    
print(solve(l))