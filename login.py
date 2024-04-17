from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from signup import Signup

class Login(QDialog):
    def __init__(self, widget):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.widget = widget
        self.loginbutton.clicked.connect(self.loginFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccountbutton.clicked.connect(self.gottosignup)
    
    def loginFunction(self):
        email = self.email.text()
        password = self.password.text()
        print(email, password)
    
    def gottosignup(self):
        signup = Signup()
        self.widget.addWidget(signup)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
