import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

def Readings():
    line = (ser.readline().decode("utf-8"))
    #print(line)
    if "[" in line:
        string = line.replace("[", "").replace("]", "")
        list = [float(x.strip()) for x in string.split(",")]
        # if list[1] < 0:
        #     list[1] = 360 + list[1]
        return list
    return None

# while True:
#     out = Readings()
#     print(out)