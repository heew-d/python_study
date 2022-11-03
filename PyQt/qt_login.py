import PySide2
import PySide2.QtCore

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
import sys # 시스템 종료 시 사용하기 위해 import

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = QWidget()

    labelId = QLabel('&Id : ')
    labelId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    labelPW = QLabel("&Password : ")

    lineEditId = QLineEdit()
    lineEditPW = QLineEdit()
    lineEditPW.setEchoMode(QLineEdit.Password)

    labelId.setBuddy(lineEditId)
    labelPW.setBuddy(lineEditPW)

    #       Id : [lineEditId]
    # Password : [lineEditPW]

    buttonOK = QPushButton("&Ok")
    # buttonOK.setIcon(QIcon(":/ok.png"))

    layout1 = QGridLayout()
    layout1.addWidget(labelId,0,0)
    layout1.addWidget(lineEditId,0,1)
    layout1.addWidget(labelPW,1,0)
    layout1.addWidget(lineEditPW,1,1)

    layout2 = QHBoxLayout()
    layout2.addStretch()
    layout2.addWidget(buttonOK)

    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layout1)
    mainLayout.addLayout(layout2)

    login.setLayout(mainLayout)
    login.setWindowTitle("Log on")
    # login.setWindowIcon(QIcon(":/images/ok.png"))

    buttonOK.clicked.connect(app.quit)

    login.show()
    app.exec_()

