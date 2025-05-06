import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QInputDialog
)
from PyQt5.QtCore import Qt, pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text=''):
        super().__init__(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QLabel {
                border: 1px solid gray;
                background-color: #f0f0f0;
                padding: 5px 10px;
                border-radius: 4px;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog Demo")
        self.setGeometry(100, 100, 450, 200)

        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        self.label_list = ClickableLabel("Pilih bahasa")
        self.line_list = QLineEdit()
        self.line_list.setReadOnly(True)
        row1.addWidget(self.label_list)
        row1.addWidget(self.line_list)

        row2 = QHBoxLayout()
        self.label_name = ClickableLabel("Nama")
        self.line_name = QLineEdit()
        self.line_name.setReadOnly(True)
        row2.addWidget(self.label_name)
        row2.addWidget(self.line_name)

        row3 = QHBoxLayout()
        self.label_int = ClickableLabel("Nomor")
        self.line_int = QLineEdit()
        self.line_int.setReadOnly(True)
        row3.addWidget(self.label_int)
        row3.addWidget(self.line_int)

        self.footer = QLabel("Nama: Muhammad Ridho Fahru Rozy\nNIM: F1D022076")
        self.footer.setAlignment(Qt.AlignCenter)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addWidget(self.footer)

        self.setLayout(main_layout)

        self.label_list.clicked.connect(self.get_item)
        self.label_name.clicked.connect(self.get_name)
        self.label_int.clicked.connect(self.get_integer)

    def get_item(self):
        items = ("C", "C++", "Java", "Python", "JavaScript")
        item, ok = QInputDialog.getItem(self, "Pilih Bahasa Program", "List Bahasa:", items, 0, False)
        if ok and item:
            self.line_list.setText(item)

    def get_name(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Masukkan Nama:")
        if ok and text:
            self.line_name.setText(text)

    def get_integer(self):
        number, ok = QInputDialog.getInt(self, "Integer Input Dialog", "Masukkan Nomor:")
        if ok:
            self.line_int.setText(str(number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
