def solve(l):
    su = 0
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            su += 1
        else:
            return su


n = int(input("Enter your number: "))
l = []
for _ in range(n):
    l.append(int(input("Enter number:")))

print(solve(l))