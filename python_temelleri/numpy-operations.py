import numpy as np

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

# result = numbers1 + numbers2
# result = numbers1 + 10 
# result = numbers1 - numbers2
# result = numbers1 - 10
# result = numbers1 * numbers2
# result = numbers1 * 10
# result = numbers1 / numbers2
# result = numbers1 / 10


result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

print(result)