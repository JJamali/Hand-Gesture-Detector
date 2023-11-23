from useful_functions import popupmsg, plot_grid, determine_sign

data = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
     [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
     [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
     [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
     [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
     [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]]


plot_grid(data)

print(determine_sign(data))

popupmsg(determine_sign(data), "red")