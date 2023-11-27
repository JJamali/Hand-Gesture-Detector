import serial
from useful_functions import plot_grid


# connect python to arduino serial readings
ser = serial.Serial('/dev/cu.usbserial-113240', 9600, timeout=1)

ROWS, COLS = 6, 10
data = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
x, y = 0, 0

print(data)

# run indefinitely
while True:

    try:
        input = ser.readline()
        print("input")
        print(input)
        print(input.decode("utf-8"))
    except Exception:
        # print("unable to read line")
        i = 0
    # # if we've populated all the data, exit the while loop
    if input.decode("utf-8") == "do":
        print("BREAK")
        break

    extracted_num = ""

    for c in str(input):
        if c.isdigit():
            extracted_num += c
        elif len(extracted_num) > 0:
            break
    if extracted_num != "":
        input = int(extracted_num)
    else:
        continue  # this might introduce a bug, as the program will start with not seeing anything. prob ok tho
        
    print("extracted input " + str(input))
    finger_detected = input < 100
    print(finger_detected)

    # populate grid
    print(x, y)
    data[y][x] = finger_detected
    print(data)
    if x == COLS - 1:
        x = 0
        y += 1
    else:
        x += 1


print(data)

# flip every other row
for i in range(1, ROWS - 1, 2):
    data[i] = data[i][::-1]

# do stuff with data
plot_grid(data)
