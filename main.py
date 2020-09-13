import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from App.design import Ui_Dialog
import requests
from bs4 import BeautifulSoup


app = QtWidgets.QApplication(sys.argv) #Create app

#init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#Logic
def main():
    year = ui.lineEdit.text()
    url = f"https://filmix.co/detektivy/y{year}"
    result = requests.get(url)
    resp = result.text
    soup = BeautifulSoup(resp, 'lxml')

    try:
       for h2 in soup.findAll('h2'):
            list = f"{h2['content']}"
            print(list)
            ui.label.setText(list)

    except KeyError:
        pass

ui.pushButton.clicked.connect(main)



sys.exit(app.exec())