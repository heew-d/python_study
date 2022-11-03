import PySide2
import PySide2.QtCore

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QCheckBox, QRadioButton, QGroupBox
# from PySide2.QtWidgets import *
import sys # 시스템 종료 시 사용하기 위해 import

class MyForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Button Demo")

        self.button = QPushButton("OK")
        self.button.clicked.connect(self.okButtonClicked)

        self.checkBox = QCheckBox('Case Sensitivity', self)
        self.checkBox.toggled.connect(self.onCaseSensitivity)

        self.nameLabel = QLabel("라면")
        box = QGroupBox("음식")

        # self.button1 = QRadioButton("Male", box)
        # self.button2 = QRadioButton("Female", box)
        self.button1 = QRadioButton("라면", box)
        self.button2 = QRadioButton("국수", box)
        self.button1.setChecked(True)

        groupBoxLayout = QVBoxLayout(box)
        groupBoxLayout.addWidget(self.button1)
        groupBoxLayout.addWidget(self.button2)
        # self.button1.toggled.connect(self.onMale)

        self.button1.toggled.connect(self.onToggle1)
        self.button2.toggled.connect(self.onToggle2)
        # self.button1.toggled.connect(self.onToggle3)

        self.nameLabel = QLabel()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.checkBox)
        mainLayout.addWidget(self.nameLabel)
        mainLayout.addWidget(box)

        self.setLayout(mainLayout)
        
        pass

    def okButtonClicked(self):
        print('okButtonClicked')

    def onCaseSensitivity(self, toggle):
        print('okCaseSensitivity', toggle)
        print(self.checkBox.isChecked())

    def onMale(self, toggle):
        print('male' if toggle else 'female')

    def onToggle1(self, toggle):
        # print('라면') if toggle else None
        self.nameLabel.setText('라면')
        pass

    def onToggle2(self, toggle):
        # print('국수') if toggle else None
        self.nameLabel.setText('국수')
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = MyForm()
    form.show()

    # form.button.setText('버튼')
   
    app.exec_()

