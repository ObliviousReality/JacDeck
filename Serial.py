import serial


if __name__ == "__main__":
    port = serial.Serial()
    port.port = "COM3"
    port.baudrate = 115200
    port.open()
    while True:
        data = port.readline()
        print(data)
        if ("There" in data.decode("ascii")):
            break
        data = bytes("Hello\r\n", "ascii")
        port.write(data)
    port.close()
