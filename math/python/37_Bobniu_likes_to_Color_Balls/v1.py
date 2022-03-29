
def solve(l):
    if sum(l) in [0, 1]:
        return "YES"

    odd = 0
    k = []
    for i in l:
        if i % 2 == 1:
            k.append(i)
            odd += 1
            
    k.sort()
    if (odd > 1 and min(k) != sum(k)/len(k)) or (odd <= 1):
        return "YES"
    return "NO"



n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 4 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))