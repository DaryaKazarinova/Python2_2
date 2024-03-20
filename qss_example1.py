import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton


class TextTransferApp(QWidget):
    def __init__(self):
        super(TextTransferApp, self).__init__()

        self.layout = QVBoxLayout(self)

        self.text_field = QLineEdit(self)
        self.layout.addWidget(self.text_field)

        self.transfer_button = QPushButton("Переместить текст", self)
        self.transfer_button.clicked.connect(self.transfer_text)
        self.layout.addWidget(self.transfer_button)

        # Применение стилей к кнопке
        self.transfer_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )

        # Применение стилей к текстовому полю
        self.text_field.setStyleSheet(
            """
            QLineEdit {
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #ccc;
            }
            """
        )

    def transfer_text(self):
        text_from_field = self.text_field.text()
        self.transfer_button.setText(text_from_field)


app = QApplication(sys.argv)
text_transfer_app = TextTransferApp()
text_transfer_app.show()
sys.exit(app.exec_())
