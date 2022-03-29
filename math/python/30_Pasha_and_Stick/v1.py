def solve(l):
    no_of_way = 0
    if l > 5:
        for i in range(1, int(l / 4) + 1):
            width = (l - (i * 2)) / 2
            if width == int(width):
                if i != width:
                    no_of_way += 1

    return no_of_way


print(solve(int(input("Enter your number: "))))