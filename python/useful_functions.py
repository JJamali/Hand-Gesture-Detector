import matplotlib.pyplot as plt
import tkinter as tk

# takes in string msg, returns pop up window when called with msg
# color dictates background color
def popupmsg(msg, color): #TODO FIX THIS
    # set up fonts for pop up window stuff
    LARGE_FONT = ("Verdana", 12)
    NORM_FONT = ("Helvetica", 80)
    SMALL_FONT = ("Helvetica", 8)

    popup = tk.Tk()
    popup.configure(bg=color)
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Ok", command=popup.destroy)
    B1.pack()
    popup.mainloop()

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


def determine_sign(data):

    left_found = False
    right_found = True

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
