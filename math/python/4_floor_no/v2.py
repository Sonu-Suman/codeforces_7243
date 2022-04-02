import math


for i in range(int(input(""))):
    s = [i for i in map(int, input("").split())]
    print(math.ceil((s[0]-2)/s[1])+1 if s[0]>2 else 1)