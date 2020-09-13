from itertools import permutations
from itertools import product

data = ['A', 'B', 'C']
result = list(permutations(data,2))
print(result)
result2 = list(product(data,repeat=2))
print(result2)