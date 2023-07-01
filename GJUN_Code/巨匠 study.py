import random

# 隨機選取6個數字
numbers = random.sample(range(1, 11), 6)

print("原始數字:")
print(numbers)

# 使用氣泡排序將數字從小到大排序
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            print("排序過程:")
            print(numbers)

# 最終排序結果
print("最終排序結果:")
print(numbers)