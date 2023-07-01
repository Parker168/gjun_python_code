# a =   11 => 3
# b =  101 => 5
# s = 1000 => 8

# e = 12 => 18
# f = 2A => 42
# e = 3C => 60
# 0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F -> hex

a = "11"
b = "1"
print(a + b)
print(int(a), int(b), int(a) + int(b))
print(int(a, 2), int(b, 2), int(a, 2) + int(b, 2))
c = int(a, 2) + int(b, 2)

