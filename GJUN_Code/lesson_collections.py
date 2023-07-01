from collections import deque

deque_1 = deque([1, 2, 3])
deque_1.append(4)
deque_1.extend([5, 6 ,7])
# print(deque_1)

# 正常的list要加東西到左邊, 可能要用以下形式
# list_a = ['a'] + ['b', 'c', 'd']
deque_1.appendleft(0)
deque_1.extendleft([10, 9, 8])
deque_1 = [11, 12, 13] + list(deque_1) # not list anymore
# print(deque_1)

deque_2 =  deque(['a', 'b', 'c', 'd', 'e'])
# deque_2.rotate()
# print(deque_2)
# deque_2.rotate()
# print(deque_2)
# deque_2.rotate()
# print(deque_2)
deque_2.rotate(3)
print(deque_2)