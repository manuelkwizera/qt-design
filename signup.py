from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("signup.ui", self)
        self.submitbutton.clicked.connect(self.signupFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def signupFunction(self):
        print("submit button clicked")
