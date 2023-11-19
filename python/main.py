import serial
import tkinter as tk
# import numpy as np
# import matplotlib.pyplot as plt


# set up fonts for pop up window stuff
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 80)
SMALL_FONT = ("Helvetica", 8)

# takes in string msg, returns pop up window when called with msg
# color dictates background color
def popupmsg(msg, color):
    popup = tk.Tk()
    popup.configure(bg=color)
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="hhh", command = popup.destroy)
    B1.pack()
    popup.mainloop()

# connect python to arduino serial readings
ser = serial.Serial('/dev/cu.usbserial-140', 9600, timeout=1)
#ser.baudrate = 9600
#ser.port = 'COM3' # note: this changes with different environments
#ser.open()
print(ser.name)

# run indefinitely
while True:

    try:
        input = ser.readline()
    except Exception:
        print("unable to read line")
    
    # code to extract number from input data
    extracted_num = ""

    for c in str(input):
        if c.isdigit():
            extracted_num += c
        elif len(extracted_num) > 0:
            break
    if extracted_num != "":
        input = int(extracted_num)
    else:
        input = 0
        
    # print("cleaned input = " + str(input))

    if input < 100:
        print("finger lmao")
    else:
        print("i dont see anything haha")

    # do stuff with data
    
out = [[]]


def print_data(grid):

    width, height = len(grid), len(grid[0])
    for y in range(height):
        print()
        for x in range(width):
            print(out[x][y], end="")
