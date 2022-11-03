import serial

PORT = "/dev/ttyUSB0"
BAUDRATE = 115200

# ser = serial.serial_for_url(PORT, baudrate=BAUDRATE, timeout=1)
# print("ser: ",ser)

# 시리얼 포트와 통신 준비
ser = serial.Serial(PORT, baudrate=BAUDRATE)
# print("ser: ",ser)

while True:
    # msg = 'q'
    msg = input()

    if (msg=='0'):
        break

    # print(f'input: {msg}', end='')

    # 데이터를 전송
    ser.write(msg.encode())
    # for c in msg:
    #     ser.write(msg.encode())
    #     # ser.write(c.encode(encoding='utf-8'))

ser.close()