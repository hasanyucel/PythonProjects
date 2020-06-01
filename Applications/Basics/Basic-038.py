# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def solve_problem(x,y):
    result = (x + y) * (x + y)
    return result

print(solve_problem(4,3))
