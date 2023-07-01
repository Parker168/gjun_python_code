from matplotlib import pyplot as plt

# 1
list_y = [2, 4, 6, 8]
plt.plot(list_y)
# plt.show()
plt.savefig("./plot_image/first_plot.jpg")

# 2
list_x_y = [(1,2), (2,4), (9,6), (7,10)]
list_x_y.sort()
print(list_x_y)
plt.plot([x for x, y in list_x_y], [y for x, y in list_x_y])
# plt.show()
plt.savefig("./plot_image/second_plot.jpg")