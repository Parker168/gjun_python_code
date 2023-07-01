# enumerate
list_a = ['a', 'b', 'c', 'd', 'e']
print(list_a)
for index, letter in enumerate(list_a):
    index = index + 1
    print(index, ":", letter * index)
