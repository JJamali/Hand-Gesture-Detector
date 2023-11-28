import serial
from useful_functions import plot_grid


# connect python to arduino serial readings
ser = serial.Serial('/dev/cu.usbserial-1110', 9600, timeout=1)

ROWS, COLS = 12, 14
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
        print("unable to read line")
        # i = 0
    # if we've populated all the data, exit the while loop
    if input.decode("utf-8") == "do":
        print("BREAK")
        break
    if input.decode("utf-8") == "nr\r\n":
        print("new row")
        print(x, y)
        x = 0
        y += 1

    extracted_num = ""

    for c in str(input):
        if c.isdigit():
            extracted_num += c
        elif len(extracted_num) > 0:
            break
    if extracted_num != "":
        input = int(extracted_num)
    else:
        continue
        
    print("extracted input " + str(input))
    finger_detected = input < 100
    print(finger_detected)

    # populate grid
    print(x, y)
    if not (y == ROWS or x == COLS):
        data[y][x] = finger_detected

    print(data)
    x += 1

print(data)

# flip every other row
for i in range(1, ROWS - 1, 2):
    data[i] = data[i][::-1]

# plot grid
plot_grid(data)
