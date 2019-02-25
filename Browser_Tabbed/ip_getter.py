from PyQt5.QtWidgets import *


class IPDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(IPDialog, self).__init__(*args, **kwargs)

        self.layout = QFormLayout()
        self.ip_input = QLineEdit()
        self.button = QPushButton("Enter")
        self.layout.addRow(self.button, self.ip_input)
        self.button.clicked.connect(self.getText)

    def getText(self):
        text, ok = QInputDialog.getText(self, 'IP Input', "Enter the IP")

        if ok:
            self.ip_input.setText(str(text))
            print(str(text))
            return str(text)
