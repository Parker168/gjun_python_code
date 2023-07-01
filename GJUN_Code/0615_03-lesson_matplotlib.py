from matplotlib import pyplot as plt

# 1
list_y = [2, 4, 6, 8]
plt.plot(list_y)
# plt.show()
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend(["First Line"])
plt.title("First Plot")
plt.savefig("./plot_image/first_plot.jpg")

plt.cla()

# 2
list_x_y = [(1,2), (2,4), (9,6), (7,10)]
list_x_y.sort()
plt.plot([x for x, y in list_x_y], [y for x, y in list_x_y])
# plt.show()
plt.savefig("./plot_image/second_plot.jpg")
plt.cla()

# 3
n = range(1,30)
plt.plot(n, n, "y--")   # Yellow Dash
plt.plot(n, [i*i for i in n], "rs") # Red Square
plt.plot(n, [i**3 for i in n], "g^") # Green Triangle
# plt.plot(n, n, "y--", n, n**2, "rs", n, n**3, "g^")
plt.legend(["n","n*n","n*n*n"])
plt.savefig("./plot_image/third_plot.jpg")
plt.cla()

# 4
n = range(1,30)
plt.scatter(n, n, c='y') 
plt.scatter(n, [i*i for i in n], c="r")
plt.scatter(n, [i**3 for i in n], c="g")
plt.legend(["n","n*n","n*n*n"])
plt.savefig("./plot_image/forth_plot.jpg")
plt.cla()