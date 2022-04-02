n, k = map(int, input("").split())

C = [0]*(k+1)

for _ in range(n):
	C[int(input())] += 1


odd = 0
for c in C:
	if c%2 == 1:
		odd += 1

print(((n+1)//2)*2- (odd+1)//2)