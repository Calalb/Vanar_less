


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 504)
        font = QtGui.QFont()
        font.setPointSize(18)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 101, 61))
        self.pushButton.setStyleSheet("color: rgb(254, 251, 216);\n"
"\n"
"background-color: rgb(66, 133, 244);\n"
"font: 75 11pt \"Century Gothic\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(196, 208, 206);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 150, 391, 321))
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: rgb(196, 208, 206);")
        self.label.setWordWrap(True)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Arată filme"))
        self.label.setText(_translate("Dialog", "TextLabel"))
