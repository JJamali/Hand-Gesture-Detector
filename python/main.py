import serial
from useful_functions import plot_grid, determine_sign


# connect python to arduino serial readings
ser = serial.Serial('/dev/cu.usbserial-140', 9600, timeout=1)
print(ser.name)

ROWS, COLS = 6, 10
data = [[-1] * COLS] * ROWS
x, y = 0, 0

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

    finger_detected = input < 100
    print(finger_detected)

    # populate grid
    data[x][y] = finger_detected
    if x == COLS:
        x = 0
        y += 1
    else:
        x += 1

    if y == ROWS:
        break

# flip every other row
for i in range(1, ROWS, 2):
    data[i] = data[i][::-1]

# do stuff with data
plot_grid(data)
