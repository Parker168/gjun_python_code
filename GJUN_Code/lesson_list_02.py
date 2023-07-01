# Create
list_1 = list()
list_2 = []

string_for_list = "I want to play a game!".replace(" ", "**")
print(string_for_list)
list_from_string = string_for_list.split('**')
print(list_from_string)
list_from_string_2 = "Eat an apple a day, keep doctor away.".split(" ")
print(list_from_string_2)

# Get
list_3 = [1, 2, 3, 4, 5, 6, 7]
x = list_3[0]
y = list_3[5]
z = list_3[-1]
w = list_3[1:3]
v = list_3[1:-1]
print(x, y, z, w, v)

list_3[-1] = [55, 66]
list_3[1:3] = [10, 11]
print(list_3)
