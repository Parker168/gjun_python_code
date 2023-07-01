import numpy as np
x = np.random.randint(1, 10)
y = np.random.randint(1, 10)

if x > y:
    print("bigger")
else:
    if x == y:
        print("equal")
    else:
        print("smaller")

print(f"x:{x}, y:{y}")