""" 
I think this problem is not properly written in correct way.
Whatever I understand this problem, I want to write that for code if in case future, if this problem
would be changed in future, then i must be revisit this problem and problem solution.
"""

def game(n):
    if n%2==0:
        return "Mahmoud"
    else:
        return "Ehab"


n = int(input("Enter your choosed number: "))
print(game(n))