
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox)

from PySide2.QtGui import QPixmap, QImage
import sys

class MainWindow(QWidget):
    def __init__(self,parent=None):
        # super().__init__(parent)
        QWidget.__init__(self, parent)

        self.setWindowTitle("Imager viewer")

        self.imageLabel = QLabel()
        self.imageLabel.setFrameStyle(QFrame.WinPanel)
        # self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.imageLabel.setMinimumSize(500,500)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.imageLabel.setScaledContents(True)
        # 위젯에 표시될 이미지를 정의(화면에 그림)
        self.imageLabel.setPixmap(QPixmap())

        openButton = QPushButton("Load image")

        layout = QVBoxLayout() # 위젯이 세로로 들어감
        layout.addWidget(self.imageLabel)
        layout.addWidget(openButton)

        # 해당 윈도우는 레이아웃이 1개
        self.setLayout(layout)

        openButton.clicked.connect(self.open)
        self.resize(QApplication.primaryScreen().availableSize()*2/5)

    def open(self):
        # QFileDialog : 파일 열기, 저장을 위한 파일이름을 받아오는 공용다이얼로그
        fileName,_ = QFileDialog.getOpenFileName(self, "Open Image File", ".", "Images (*.png *.xpm *.jpg *.jpeg)")
        # print("fileName:", fileName)
        if fileName != "":
            self.load(fileName)
    
    def load(self, fileName):
        image = QImage(fileName)
        # image.invertPixels(QImage.InvertMode.InvertRgba) # 색상 반전

        if image.isNull():
            QMessageBox.information(self, QApplication.applicationName(), "Cannot load"+fileName)

            self.setWindowTitle("Imager viewer")
            self.setPixmap(QPixmap())
            return

        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.setWindowTitle(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 실제 화면에 그려줌
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()