from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit,QTextEdit, QComboBox, 
                                QSpinBox, QSlider, QProgressBar, QHBoxLayout,
                                QGroupBox, QCheckBox)

from PySide2.QtGui import (QPixmap, QImage, QColorSpace, 
                            QIntValidator, QDoubleValidator, QRegExpValidator)

from PySide2.QtCore import QRegExp, Qt, QThread, Signal, Slot
import sys
import serial
import time
from serial.tools import list_ports

BAUDRATES = [
    300,
    1200,
    2400,
    4800,
    9600,
    19200,
    38400,
    57600,
    74880,
    115200,
    230400,
    250000,
    500000,
    1000000,
    2000000,
]

ports = []
PORT = "/dev/ttyUSB0" # $ sudo chmod 666 /dev/ttyUSB1
BAUDRATE = 115200

# 시리얼 포트와 통신 준비
# ser = serial.Serial(PORT, baudrate=BAUDRATE)

ser:serial.Serial = None
class WorkerSumP1(QThread):

    def __init__(self, low, high, widget):
        super().__init__()
        self.low = low
        self.high = high
        self.widget:QTextEdit = widget # 결과가 출력될 위젯

        # print("widget id2: ", id(self.widget))

    def run(self) -> None:
        while True:
            print(f'스레드시작 {self.low}부터 {self.high}까지 더할거임')

            now = time.time()

            total = 0
            for i in range(self.low, self.high):
                total += i

            # print('sum: ', total)
            delta = time.time() - now

            resultMSG = f'스레드 끝: 결과는 {total}, 걸린시간: {delta} sec'
            print(resultMSG)

            self.widget.append(resultMSG)
            pass

    pass

class CallbackHandler():

    def __init__(self):
        self.functions = []
        pass

    # func에 전달된 함수를 보관
    def connect(self, func):
        self.functions.append(func)

    def disconnect(self, func=None):
        if not func:
            self.functions.clear()
            return
        # self.functions.remove(func)

        funcs = self.functions[:]

        for f in self.functions:
            if f == func:
                funcs.pop(funcs.index(f))

        self.functions = funcs

        # for i in range(len(self.functions)):
        #     f = self.functions[i]
        #     if f is func:
        #     # if id(f) is id(func):
        #         self.functions.pop(i)

        # for f in self.functions:
        #     # f와 func이 같다면 functions 안에서 제거  # is 메모리 비교!!
        #     if f is func:
        #         self.functions.remove(f)
        pass

    def emit(self, *args):
        for func in self.functions:
            func(args)
            pass
        pass
    pass

class WorkerSumP2(QThread):

    # callbackSignal = pyqtSignal(str) # pyqt5
    callbackSignal = Signal(str) # pyside2   # 시그널로 사용할 수 있는 구성

    handler = CallbackHandler()

    def __init__(self, low, high, callback):
        super().__init__()
        self.low = low
        self.high = high
        # self.callback = callback
        
        self.callbackSignal.connect(callback)

    def run(self) -> None:
        print(f'스레드시작 {self.low}부터 {self.high}까지 더할거임')
        now = time.time()

        total = 0
        for i in range(self.low, self.high):
            total += i

        # print('sum: ', total)
        delta = time.time() - now

        resultMSG = f'스레드 끝: 결과는 {total}, 걸린시간: {delta} sec'
        print(resultMSG)

        # self.callback(resultMSG) # 권장되지 않는 방법

        # 시그널을 통해 Signal.connect(함수명) 된 함수를 호출 할땐 Signal.emit(매개변수)
        # *시그널 사용 권장
        self.callbackSignal.emit(resultMSG)

        # complete3, complete4, complete5 전달
        self.handler.emit(resultMSG)

        pass
    pass

class WorkerSerialRead(QThread):

    onRead = Signal(str)

    def __init__(self):
        super().__init__()
        pass

    def run(self):
        # 시리얼통신을 통해 데이터를 읽어옴
        while True:

            if not ser or ser.closed:
                continue

            line = ser.readline().decode().replace('\n','').replace('\r', '')
            
            if not line:
                # time.sleep(1)
                continue

            # print("readline: " + line)
            self.onRead.emit(line)
            pass
        pass
    pass



class MainWindow(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)

        # 현재 사용가능한 시리얼포트를 조회
        comports = list_ports.comports()
        for comport in comports:
            device = comport.device

            if 'ttyS' in device:
                continue

            ports.append(device)
            pass

        self.inputLineEdit = QLineEdit()
        self.printTextEdit = QTextEdit()
        self.printTextEdit.setReadOnly(True)

        self.inputLineEdit.returnPressed.connect(self.sendMessage)

        # 두개의 콤보박스(보드레이트, 포트)
        self.baudratecomboBox = QComboBox()
        self.baudratecomboBox.currentIndexChanged.connect(self.onChangedBaudrateAndPort)
        self.portcomboBox = QComboBox()
        self.portcomboBox.currentIndexChanged.connect(self.onChangedBaudrateAndPort)
        
        # 가로로 정렬된 모습으로 두개의 콤보박스를 추가
        serialSettingLayout = QHBoxLayout()
        serialSettingLayout.addWidget(self.portcomboBox)
        serialSettingLayout.addWidget(self.baudratecomboBox)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.inputLineEdit)
        mainLayout.addWidget(self.printTextEdit)
        mainLayout.addLayout(serialSettingLayout)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("시리얼 통신")
        self.setMinimumSize(500,500)
        # self.resize(400,400)

        self.workerSerialRead = WorkerSerialRead()
        self.workerSerialRead.onRead.connect(self.complete)
        self.workerSerialRead.start()

        # 보드레이트 목록을 보드레이트 콤보의 선택가능한 항목(item)으로 추가
        for b in BAUDRATES:
            bardrateName = f'{b} 보드레이트'
            self.baudratecomboBox.addItem(bardrateName)       

        # print('ports: ', ports)
        # 조회된 시리얼포트를 포트 콤보박스에 추가
        self.portcomboBox.addItems(ports)

        # 시리얼세팅 관련 정보를 갱신
        # self.updateSerialSetting()
        pass

    def updateSerialSetting(self):
        
        # 사용가능한 포트를 조회
        ports.clear()

        list = list_ports.comports()
        # print("updateSerialSetting:: list: ", list)

        for comport in list:
            device = comport.device
            print("updateSerialSetting:: device: ", device)
            ports.append(device)

        # 포트 목록과 보드레이트 목록을 구성
        for baudrate in BAUDRATES:
            self.baudratecomboBox.addItem(f'{baudrate} 보드레이트')
            pass

        for port in ports:
            self.portcomboBox.addItem(port)

    def onChangedBaudrateAndPort(self):
        # 현재 선택된 보드레이트 인덱스를 읽어와서 사용할 보드레이트 값을 준비
        currentIndex = self.baudratecomboBox.currentIndex()
        print("onChangedBaudrate: currentIndex: ", currentIndex)

        if currentIndex < 0:
            return
        
        baudrate = BAUDRATES[currentIndex]

        # 현재 선택된 포트 인덱스를 읽어와서 사용할 포트 값을 준비
        currentIndex = self.portcomboBox.currentIndex()
        print("onChangedPort: currentIndex: ", currentIndex)

        if currentIndex < 0:
            return

        port = ports[currentIndex]

        global ser
        if ser:
            ser.baudrate = baudrate
            if ser.port != port:
                ser.port = port
            # ser.open()
        else:
            ser = serial.Serial(port, baudrate=baudrate)

        # if ser:
        #     ser.close()
            
        # ser = serial.Serial(port, baudrate=baudrate)

        print("onChangePort: ready serial: ", ser)

        pass

    def sendMessage(self):

        # inputText = self.inputLineEdit.text()

        # 스레드 없이 메인스레드에서 더하기 함수 실행 테스트
        # self.sum(1, 100000000)

        # print("widget id1: ", id(self.printTextEdit))

        # 스레드생성 및 시작
        # self.WorkerSumP1 = WorkerSumP1(1, 100000000, self.printTextEdit)
        # self.WorkerSumP1.start()

        # self.WorkerSumP2 = WorkerSumP2(1, 100000000, self.complete)
        # self.WorkerSumP2.callbackSignal.connect(self.complete2) # 외부에서 시그널 연결
        # self.WorkerSumP2.callbackSignal.disconnect(self.complete2) # 시그널 연결 해제
        # self.WorkerSumP2.callbackSignal.disconnect() # 전체 시그널 연결 해제

        # self.WorkerSumP2.handler.connect(self.complete3)
        # self.WorkerSumP2.handler.connect(self.complete4)
        # self.WorkerSumP2.handler.connect(self.complete5)
        # self.WorkerSumP2.handler.disconnect(self.complete3)
        # self.WorkerSumP2.handler.disconnect(self.complete4)

        # self.WorkerSumP2.start()

        # 출력공간에 문구 추가 테스트
        # # self.printTextEdit.setText(self.printTextEdit.toPlainText() + inputText)
        # self.printTextEdit.append(inputText)

        # 시리얼통신을 통해 값을 전송
        inputText = self.inputLineEdit.text()

            # 입력된 문구가 숫자인지 파악
        # if inputText.isnumeric(): # 숫자표현식도 포함
        # is inputText.isdecimal(): # 정수만

        if not inputText.isdigit(): # 숫자
            return
        # if not inputText.lstrip('-').isdigit():
        #     print('숫자가 아닙니다')
        #     time.sleep(2)

            # 입력된 문구를 숫자형으로 변경
        inputNum = int(inputText)

            # 입력된 문구가 일정 범위 안에 있는지 파악
        if inputNum < 0  or inputNum > 180:
            # print('범위를 벗어나 다시 입력')
            # time.sleep(2)
            return

            # 숫자를 문자로 변경

            # 시리얼 통신을 통해 문자를 전달
        ser.write(str(inputNum).encode())
        print('정상적으로 전송 : ' , inputNum)
        # time.sleep(2)

            # 입력된 문구를 초기화 (지우기)
            # print("find: ", inputText.find('\n'))
        self.inputLineEdit.setText('')

            # 출력공간에 문구 추가 테스트
        # self.printTextEdit.append("각도: "+ inputText)
        
        pass

    def complete(self, text):
        print("complete:: text: ", text)
        self.printTextEdit.append(text)
        pass
    def complete2(self, text):
        print("complete2:: text: ", text)
        pass

    def complete3(self, text):
        print("complete3:: text: ", text)
        pass
    def complete4(self, text):
        print("complete4:: text: ", text)
        pass
    def complete5(self, text):
        print("complete5:: text: ", text)
        pass



def prepare():
    global ser

    ser = serial.Serial(PORT, baudrate=BAUDRATE)

    pass

if __name__ == '__main__':
    # prepare()

    app = QApplication(sys.argv)
    
    # 실제 화면에 그려줌
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()