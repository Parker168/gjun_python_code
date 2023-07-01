import math
import numpy as np
n = 3
numbers = np.random.choice(1000, n, replace=False)
print("Numbers: ", numbers, math.gcd(*numbers))

# 1. minimum number of numbers
# 2. divisor of min number
# 3. check if divisor is common divisor
# 4. max common divisor

# 1
min_number = min(numbers)
# 2
divisors = list()
for n in range(1, min_number+1):
    if min_number % n == 0:
        divisors.append(n)
print(min_number, "'s Divisors: ", divisors)

# 3
common_divisors = list()
for divisor in divisors:
    is_common_divisor = True
    for number in numbers:
        if number % divisor == 0:
            continue
        else:
            is_common_divisor = False
            break
    if is_common_divisor == True:
        common_divisors.append(divisor)
print(common_divisors)

# 4
print(max(common_divisors))
