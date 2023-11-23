import matplotlib.pyplot as plt


def plot_grid(data):


    ### dummy data just to play with
    # data = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    #  [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    #  [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    #  [0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    #  [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    #  [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    #  [0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    #  [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    #  [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    #  [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]]

    plt.imshow(data)
    plt.show()