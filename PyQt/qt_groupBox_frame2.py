from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QComboBox, 
                                QSpinBox, QSlider, QProgressBar,
                                QCheckBox, QGroupBox,
                                )

from PySide2.QtGui import (
    QPixmap, QImage, QColorSpace, 
    QIntValidator, QDoubleValidator, QRegExpValidator
)

from PySide2.QtCore import Qt, QRegExp
import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.allChecked = False

        self.appleCheckBox = QCheckBox("apple")
        self.grapeCheckBox = QCheckBox("grape")
        self.bananaCheckBox = QCheckBox("banana")

        # self.appleCheckBox.toggled.connect(self.onToggled)
        # self.grapeCheckBox.toggled.connect(self.onToggled)
        # self.bananaCheckBox.toggled.connect(self.onToggled)
        self.appleCheckBox.clicked.connect(self.onClickToggle)
        self.grapeCheckBox.clicked.connect(self.onClickToggle)
        self.bananaCheckBox.clicked.connect(self.onClickToggle)

        layout = QVBoxLayout()
        layout.addWidget(self.appleCheckBox)
        layout.addWidget(self.grapeCheckBox)
        layout.addWidget(self.bananaCheckBox)

        self.groupBox = QGroupBox("그룹")
        self.groupBox.setLayout(layout)
        # self.groupBox.setCheckable(True)
        # self.groupBox.setChecked()
        
        self.button = QPushButton("전체선택")
        self.button.clicked.connect(self.onClickToggleAll)

        # self.button.setText("전체해제")

        self.allCheckBox = QCheckBox("전체선택")
        # self.allCheckBox.toggled.connect(self.onToggledAll)
        self.allCheckBox.clicked.connect(self.onClickToggleAll)
        

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.allCheckBox)


        self.setLayout(mainLayout)
        self.setWindowTitle("QGroupBox QFrame Example")
        # self.resize(500,500)

        pass

    def onClickToggle(self):
        print("onClickToggle:: ")

        # self.appleCheckBox.isChecked()
        # self.grapeCheckBox.isChecked()
        # self.bananaCheckBox.isChecked()

        # 전체선택 버튼과 체크박스의 상태변경 (전체해체 or 전체선택, 체크박스의 체크 포함)
        # all = True
        all = (
            self.appleCheckBox.isChecked() 
            and self.grapeCheckBox.isChecked() 
            and self.bananaCheckBox.isChecked()
        )

        self.allChecked = all

        if all:
            self.button.setText("전체해제")
            self.allCheckBox.setText("전체해제")
            self.allCheckBox.setChecked(True)
        else:
            self.button.setText("전체선택")
            self.allCheckBox.setText("전체선택")
            self.allCheckBox.setChecked(False)

        pass

    # def onToggled(self, toggled):
    #     print("onToggled:: toggled: ", toggled)

    #     # self.appleCheckBox.isChecked()
    #     # self.grapeCheckBox.isChecked()
    #     # self.bananaCheckBox.isChecked()


    #     # 전체선택 버튼과 체크박스의 상태변경 (전체해체 or 전체선택, 체크박스의 체크 포함)
    #     # all = True
    #     all = (
    #         self.appleCheckBox.isChecked() 
    #         and self.grapeCheckBox.isChecked() 
    #         and self.bananaCheckBox.isChecked()
    #     )

    #     self.allChecked = all

    #     if all:
    #         self.button.setText("전체해제")
    #         self.allCheckBox.setText("전체해제")
    #         self.allCheckBox.setChecked(True)
    #     else:
    #         self.button.setText("전체선택")
    #         self.allCheckBox.setText("전체선택")
    #         self.allCheckBox.setChecked(False)

    #     pass


    def onToggledAll(self, toggled):
        print("onToggledAll:: toggled: ", toggled)

        self.appleCheckBox.setChecked(toggled)
        self.grapeCheckBox.setChecked(toggled)
        self.bananaCheckBox.setChecked(toggled)

        self.allChecked = toggled

        if toggled:
            self.button.setText("전체해제")
            self.allCheckBox.setText("전체해제")
            # self.allCheckBox.setChecked(True)
        else:
            self.button.setText("전체선택")
            self.allCheckBox.setText("전체선택")
            # self.allCheckBox.setChecked(False)

        pass

    def onClickToggleAll(self):
        print("onClickToggle::")
        # self.groupBox.setChecked(True)

        #  allChecked 가 참(True)이면 거짓(False)으로, 거짓이면 참으로 반전
        all = not self.allChecked

        self.onToggledAll(all)
        self.allCheckBox.setChecked(all)

        # # 반전
        # # self.appleCheckBox.setChecked(not self.appleCheckBox.isChecked)

        # self.appleCheckBox.setChecked(all)
        # self.grapeCheckBox.setChecked(all)
        # self.bananaCheckBox.setChecked(all)

        # self.allChecked = all

        # # self.groupBox.children()

        # # 1.버튼의 상태를 변경, 문구, 두가지 set(쓰기), get(읽어옴)
        #     # 국수, 라면, 삼겹살 .py 문구를 변경하는게 있어요..
        # # 2.여기에서 순서도에서 마름모꼴이 의미하는바, 그 의미와 연결된 명령
        # # 어떤상태를 기준으로 '전체해제', '전체선택'
        # # if 조건

        # # 버튼의 문구를 변경
        # # self.button.setText("전체해제")

        # # 버튼 문구가 전체선택의 상태에 따라 다르게 적용
        # # 전체가 선택되었을때에는 "전체해제", 반대의 경우는 "전체선택", if문 사용

        # # all이 참이면 버튼의 문구를 "전체해제", 거짓이면 버튼의 문구를 "전체선택"
        # if all:
        #     self.button.setText("전체해제")
        #     self.allCheckBox.setText("전체해제")
        #     self.allCheckBox.setChecked(True)
        # else:
        #     self.button.setText("전체선택")
        #     self.allCheckBox.setText("전체선택")
        #     self.allCheckBox.setChecked(False)
        # pass

        # # self.allCheckBox.setChecked(all)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()