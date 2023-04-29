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
        return list
    return None
