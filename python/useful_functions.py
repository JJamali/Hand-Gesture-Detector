import matplotlib.pyplot as plt


def plot_grid(data):
    plt.title("I believe that this is " + determine_sign(data))
    plt.imshow(data)
    plt.show()


def determine_sign(data):

    left_found = False
    right_found = False

    # if we detect nothing on the 5th row, just return rock
    if not max(data[5]):
        return "rock"

    for i in data[5]:
        if i and not left_found:
            left_found = True

        elif not i and left_found:
            right_found = True

        elif i and right_found:
            # found changing from air to finger after finding a full solid body (1 finger)
            return "scissors"

        # if right found and not i, do nothing.

    if right_found:
        return "paper"

    else:
        return "inconclusive"
