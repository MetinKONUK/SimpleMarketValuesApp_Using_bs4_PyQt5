import sys
from currencytrace import values,keys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        self.manage_data()
    def manage_data(self):
        at = datetime.now()
        data = ""
        for (key,value) in zip(keys,values):
            data += "{} : {} Time:{}\n--------------------\n".format(key.text,value.text,at)
        self.info.setText(data)
    def ui(self):
        self.update = QPushButton("Update")
        self.update.clicked.connect(self.manage_data)
        self.header = QLabel("MARKET VALUES")
        self.header.setAlignment(Qt.AlignCenter)
        self.info = QLabel("")
        v_box = QVBoxLayout()
        v_box.addWidget(self.header)
        v_box.addWidget(self.info)
        v_box.addStretch()
        v_box.addWidget(self.update)
        
        self.setLayout(v_box)
        self.setWindowTitle("MARKET VALUES")
        self.setGeometry(100,100,300,300)
        self.show()
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
