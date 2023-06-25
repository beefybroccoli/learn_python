import random

# print(random.uniform(0, 1))

def return_matrix(n,m):
    matrix = [[0 if random.uniform(0,1) < (1/2) else 1 for col in range(m)] for row in range(n)]
    return matrix

print(return_matrix(5,4))


