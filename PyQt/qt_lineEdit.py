from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QComboBox)

from PySide2.QtGui import (QPixmap, QImage, QColorSpace, 
                            QIntValidator, QDoubleValidator, QRegExpValidator)

from PySide2.QtCore import QRegExp
import sys

class MainWindow(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)

        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True) # 읽기만 가능

        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText("비밀번호를 입력해주세요")
        # self.passwordEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.textChanged.connect(self.textChanged)
        self.passwordEdit.editingFinished.connect(self.editingFinished)
        self.passwordEdit.returnPressed.connect(self.returnPressed)

        self.comboBox = QComboBox()
        self.comboBox.addItem("사과")
        self.comboBox.addItem("딸기")
        self.comboBox.addItem("복숭아")
        self.comboBox.addItem("샤인머스켓")
        self.comboBox.setEditable(True)
        # 선택되었을 때 함수 호출
        self.comboBox.currentIndexChanged.connect(self.onSelected)

        self.validatorLineEdit1 = QLineEdit()
        self.validatorLineEdit1.setValidator(QIntValidator(self))
        self.validatorLineEdit1.setPlaceholderText("정수만 입력하세요")

        self.validatorLineEdit2 = QLineEdit()
        self.validatorLineEdit2.setValidator(QDoubleValidator(self))
        self.validatorLineEdit2.setPlaceholderText("실수만 가능합니다")

        regExp = QRegExp("[A-Za-z][1-9][0-9]{0,2}")
        regExp1 = QRegExp("[A-Za-z]*") # 알파벳만 임의의 갯수만큼 가능
        regExp2 = QRegExp("[0-9]*") # 숫자만 임의의 갯수만큼 가능 (\d와 같은 표현)
        regExp3 = QRegExp("[A-Za-z0-9]*") # 알파벳과 숫자만 임의의 갯수만큼 가능
        self.validatorLineEdit3 = QLineEdit()
        # self.validatorLineEdit3.setValidator(QRegExpValidator(regExp,self))
        self.validatorLineEdit3.setValidator(QRegExpValidator(regExp3,self))
        self.validatorLineEdit3.setPlaceholderText("정규식")

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.passwordEdit)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.validatorLineEdit1)
        layout.addWidget(self.validatorLineEdit2)
        layout.addWidget(self.validatorLineEdit3)

        self.setLayout(layout)
        
        pass

    # 텍스트 변경시 호출되는 함수
    def textChanged(self):
        text = self.passwordEdit.text()
        print("textChanged:: text:", text)
        self.lineEdit.setText(text)
        pass
    
    # 포커스를 잃을 때 발생
    def editingFinished(self):
        print("editingFinished::")
        pass

    # 리턴/엔터키를 누를 때 발생
    def returnPressed(self):
        print("returnPressed::")
        pass

    # 콤보박스 선택되었을 때 
    def onSelected(self):
        # print("onSelected:: ")
        currentIndex = self.comboBox.currentIndex()
        currentText = self.comboBox.currentText()
        p = f"onSelected:: currentIndex: {currentIndex}, currentText: {currentText}"
        print(p)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 실제 화면에 그려줌
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()