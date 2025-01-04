import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Diyalog göster!")
        button.clicked.connect(self.tiklama)
        self.setCentralWidget(button)

    def tiklama(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("MERHABA!")
        dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

import sys
from PyQt6.QtWidgets import *

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SELAM!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("OK'a basarsanız olur, yoksa iptal edilir.")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        yerlesim = QVBoxLayout()      
        buton1 = QPushButton("Diyalog göster!")
        yerlesim.addWidget(QLabel("Diyalog gösterme uygulaması"))
        yerlesim.addWidget(buton1)
        buton1.clicked.connect(self.tiklama)
        araclar = QWidget()
        araclar.setLayout(yerlesim)
        self.setCentralWidget(araclar)

    def tiklama(self, s):
        diyalog = QDialog()
        # diyalog.setWindowTitle("MERHABA!")
        diyalog.exec()

        diyalog = CustomDialog()
        diyalog.setWindowTitle("DİKKAT!")
        diyalog.exec()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
