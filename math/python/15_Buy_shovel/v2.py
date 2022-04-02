def solve(s):
    k = []

    l = [str(s[0]*i) for i in range(1, 10)]

    for i in range(len(l)):
        if i==(len(l)-1):
            if s[1]>=int(l[i][-1]):
                k.append(i+1)
        else:
            if int(l[i][-1])<s[1]: # and int(l[i+1][-1])>s[1]:
                k.append(i+1)

        if int(l[i][-1])==s[1]:
            return i+1


    return min(k)



s = [i for i in map(int, input("").split())]
print(solve(s))
