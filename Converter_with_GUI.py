import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import os
import sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'converter.ui')
app = QtWidgets.QApplication(sys.argv)
win = uic.loadUi(path)

data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
rates = data['rates']
log = []



def main(amount, frm_crr, to_crr):
    try:
        amount = float(amount)
        frm_crr = frm_crr.upper()
        to_crr = to_crr.upper()

        if frm_crr not in rates:
            out = f"ERROR: Currency '{frm_crr}' not found"
            return out

        if to_crr not in rates:
            out = f"ERROR: Currency '{to_crr}' not found"
            return out
        
        if frm_crr == "USD":
            res = amount * rates[to_crr]
        else:
            usd_amount = amount / rates[frm_crr]
            res = usd_amount * rates[to_crr]
        
        out =(f'>>>  {amount} {frm_crr} = {res:.2f} {to_crr}')
    
    except ValueError:
        out =(">>> ERROR: Enter a valid number")
    except Exception as e:
        out =(f">>> ERROR: Something went wrong - {e}")
    return out


        

def ui():
    amount = win.lineEdit.text()
    frm = win.comboBox.currentText()
    to = win.comboBox_2.currentText()
    result = main(amount, frm, to)
    win.textBrowser.append(result)
    log.append(result)

currencies = rates
win.comboBox.addItems(currencies)
win.comboBox_2.addItems(currencies)
win.pushButton.clicked.connect(ui)

win.show()
sys.exit(app.exec_())


