from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QComboBox, 
                                QSpinBox, QSlider, QProgressBar, QHBoxLayout)

from PySide2.QtGui import (QPixmap, QImage, QColorSpace, 
                            QIntValidator, QDoubleValidator, QRegExpValidator)

from PySide2.QtCore import QRegExp, Qt
import sys

class MainWindow(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)

        self.spin = QSpinBox()
        self.spin.setRange(0,100)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100)

        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setRange(0,100)

        # self.spin.valueChanged.connect(self.slider.setValue)
        self.spin.valueChanged.connect(self.progressBar.setValue)
        self.spin.valueChanged.connect(self.valueChanged)
        self.slider.valueChanged.connect(self.spin.setValue)
        

        layout = QHBoxLayout()
        layout.addWidget(self.spin)
        layout.addWidget(self.slider)
        layout.addWidget(self.progressBar)

        self.setLayout(layout)
        self.setWindowTitle("Spin Slider ProgressBar Example")
        
        pass

    def valueChanged(self, value):
        print("valueChanged:: value: ", value)
        self.slider.setValue(value)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 실제 화면에 그려줌
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()