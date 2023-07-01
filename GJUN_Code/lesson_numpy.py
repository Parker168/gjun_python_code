# pip install numpy
import numpy as np
n = np.random.randint(1, 50000) # 數字串列的長度
major_element = np.random.randint(-1* 10**9, 10**9) # 隨機一個Major element
part_2 = np.full(n//2, major_element) # 把Major element 擴展為一個長度為n/2的串列 來符合題意
part_1 = np.random.randint(-1* 10**9, 10**9, n//2) # 填滿剩下的一半
print(major_element)

