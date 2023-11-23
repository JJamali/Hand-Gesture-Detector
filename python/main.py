import serial
from useful_functions import popupmsg, plot_grid, determine_sign


# connect python to arduino serial readings
ser = serial.Serial('/dev/cu.usbserial-140', 9600, timeout=1)
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
        input = 0  # this might introduce a bug, as the program will start with not seeing anything. prob ok tho
        
    # print("cleaned input = " + str(input))

    if input < 100:
        print("finger lmao")
    else:
        print("i dont see anything haha")

    # do stuff with data
    
data = [[]]

plot_grid(data)

popupmsg(determine_sign(data), "blue")


