from PyQt5.QtWidgets import QApplication, QWidget
import sys
class Calculator(QWidget):
 def __init__(self):
  super().__init__()
  self.initUI()

 def initUI(self):
        self.setGeometry(300, 300, 225, 370)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())