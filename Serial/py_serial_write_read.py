import os
import serial
import time
import threading

PORT = "/dev/ttyUSB1" # $ sudo chmod 666 /dev/ttyUSB1
BAUDRATE = 115200

# 시리얼 포트와 통신 준비
# ser = serial.Serial(PORT, baudrate=BAUDRATE)

ser:serial.Serial = None

def prepare():
    global ser

    ser = serial.Serial(PORT, baudrate=BAUDRATE)
    # t = threading.Thread(target=sum, args=(1,100000000)) # 스레드 객체 생성
    # t.daemon = True  # 메인 스레드가 죽으면 같이 죽음
    # t.start() # 동작 수행

    t = threading.Thread(target=readSerial) # 스레드 객체 생성
    t.daemon = True  # 메인 스레드가 죽으면 같이 죽음
    t.start() # 동작 수행

    pass

def readSerial():

    while True:
        line = ser.readline().decode().replace('\n','').replace('\r', '')
        
        if not line:
            # time.sleep(1)
            continue

        print("readline: " + line)
        pass
    pass


def writeSerial():

    while True:

        os.system('clear')
        msg = input('각도를 입력하세요 (0~180) (종료:q) : \n')
        if msg == 'q':
            break

        # 음수 표기로 '-'는 문자라 isdigit() 결과가 False
        # 미리 '-' 표기를 지우고 숫자만 남겨 isdigit()이 True라면 숫자
        if not msg.lstrip('-').isdigit():
            print('숫자가 아닙니다')
            time.sleep(2)
            continue

        # 문자형을 숫자형으로 변경
        angle = int(msg)

        # if 0 > angle > 180:
        if 0 > angle or angle > 180:
            print('범위를 벗어나 다시 입력')
            time.sleep(2)
            continue
        
        ser.write(str(angle).encode())
        print('정상적으로 전송 : ' , angle)
        time.sleep(2)

        # line = ser.readline().decode().replace('\n','').replace('\r', '')
        # print('받아온 값 : ',line)
        # time.sleep(2)
        pass
    pass

def sum(low, high):
    
    while True:
        total = 0
        for i in range(low, high):
            total += i

        print('sum: ', total)

    pass

if __name__ == '__main__':
    prepare()

    # 블럭.. 사용자 입력을 계속해서 받음
    writeSerial()

    pass