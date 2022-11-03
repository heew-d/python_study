import PySide2
import PySide2.QtCore
# print("PySide2 version",PySide2.__version__) # 버전 확인
# print("QtCore version",PySide2.QtCore.qVersion())

from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys # 시스템 종료 시 사용하기 위해 import

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    # window.resize(289, 170)
    window.resize(400, 500)
    window.setWindowTitle("my first QTApplication")

    label = QLabel("안녕하세요",window)
    label.move(100, 250)

    window.show()
    app.exec_()

