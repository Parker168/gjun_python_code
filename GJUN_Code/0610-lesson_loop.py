list_a = ['a', 'b', 'c', 'd', 'e']
print(list_a)
# replace with for-loop
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[3])
# print(list_a[4])
for letter in list_a:
    for letter_upper in list_a:
        print("Letter: ", letter)
        print("Letter upper: ", letter_upper.upper())
    print("------------------------------------------")
