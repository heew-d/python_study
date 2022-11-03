from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QComboBox, 
                                QSpinBox, QSlider, QProgressBar, QHBoxLayout,
                                QGroupBox, QCheckBox)

from PySide2.QtGui import (QPixmap, QImage, QColorSpace, 
                            QIntValidator, QDoubleValidator, QRegExpValidator)

from PySide2.QtCore import QRegExp, Qt
import sys

class MainWindow(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)

        self.allChecked = False

        self.appleCheckBox = QCheckBox("apple")
        self.grapeCheckBox = QCheckBox("grape")
        self.orangeCheckBox = QCheckBox("orange")
        self.bananaCheckBox = QCheckBox("banana")

        self.appleCheckBox.toggled.connect(self.onToggled)
        self.grapeCheckBox.toggled.connect(self.onToggled)
        self.orangeCheckBox.toggled.connect(self.onToggled)
        self.bananaCheckBox.toggled.connect(self.onToggled)

        layout = QVBoxLayout()
        layout.addWidget(self.appleCheckBox)
        layout.addWidget(self.grapeCheckBox)
        layout.addWidget(self.orangeCheckBox)
        layout.addWidget(self.bananaCheckBox)
        
        self.groupBox = QGroupBox("fruit")
        self.groupBox.setLayout(layout)
        # self.groupBox.setCheckable(True)
        # self.groupBox.setChecked(False)

        self.button = QPushButton("전체 선택")
        self.button.clicked.connect(self.allToggle)

        self.checkToggle = QCheckBox("전체 선택")
        # self.checkToggle.toggled.connect(self.onToggledAll)
        self.checkToggle.clicked.connect(self.onToggledAll)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        mainLayout.addWidget(self.button)       
        mainLayout.addWidget(self.checkToggle)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("QGroupBox QFrame Example")
        # self.resize(400,400)
        pass
    
    def onToggled(self, toggled):
        print("onToggled:: toggled: ", toggled)

        # 전체선택 버튼과 체크박스의 상태변경 (전체해제 or 전체선택, 체크박스의 체크 포함)
        # all = True
        all = (
            self.appleCheckBox.isChecked() 
            and self.grapeCheckBox.isChecked() 
            and self.orangeCheckBox.isChecked()
            and self.bananaCheckBox.isChecked()
        )

        self.checkToggle = all

        if all:
            self.button.setText("전체 해제")
            self.checkToggle.setText("전체 해제")
            self.checkToggle.setChecked(True)
        else:
            self.button.setText("전체 선택")
            self.checkToggle.setText("전체 선택")
            self.checkToggle.setChecked(False)        
        
        pass

    def onToggledAll(self, toggled):
        print("onToggledAll:: toggled: ", toggled)

        self.appleCheckBox.setChecked(toggled)
        self.grapeCheckBox.setChecked(toggled)
        self.orangeCheckBox.setChecked(toggled)
        self.bananaCheckBox.setChecked(toggled)
        

        self.allChecked = toggled

        if toggled:
            self.button.setText("전체 해제")
            self.checkToggle.setText("전체 해제")
        else:
            self.button.setText("전체 선택")
            self.checkToggle.setText("전체 선택")
        pass
        
    def allToggle(self):
        # allChecked 가 참이면 거짓으로, 거짓이면 참으로 반전
        all = not self.allChecked

        self.onToggledAll(all)
        self.checkToggle.setChecked(all)

        #반전
        # self.appleCheckBox.setChecked(not self.appleCheckBox.isChecked)
        # self.appleCheckBox.setChecked(all)
        # self.grapeCheckBox.setChecked(all)
        # self.orangeCheckBox.setChecked(all)
        # self.bananaCheckBox.setChecked(all)
        # self.checkToggle.setChecked(all)

        # self.allChecked = all
        
        # if all:
        #     self.button.setText("전체 해제")
        #     self.checkToggle.setText("전체 해제")
        #     print("toggle:: 전체 선택" )

        # else:
        #     self.button.setText("전체 선택")
        #     self.checkToggle.setText("전체 선택")
        #     print("toggle:: 전체 해제" )
        # pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 실제 화면에 그려줌
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()