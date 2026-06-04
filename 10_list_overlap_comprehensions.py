import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 12)

result = [i for i in a if i in b]
print(result)
