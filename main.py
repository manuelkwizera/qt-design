import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from login import Login
from signup import Signup

app = QApplication(sys.argv)
widget = QStackedWidget()
mainwindow = Login(widget)  # Pass widget to the Login class constructor
widget.addWidget(mainwindow)
widget.setFixedWidth(380)
widget.setFixedHeight(520)
widget.show()
app.exec_()
