import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog, QDialogButtonBox

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog, QDialogButtonBox

class TextInputDialog(QDialog):
    def __init__(self, parent=None):
        super(TextInputDialog, self).__init__(parent)

        self.setWindowTitle("Введите текст")
        self.layout = QVBoxLayout(self)

        self.text_input = QLineEdit(self)
        self.layout.addWidget(self.text_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def get_text(self):
        return self.text_input.text()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Текст будет отображаться здесь")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Получить текст")
        self.button.clicked.connect(self.show_dialog)
        self.layout.addWidget(self.button)

    def show_dialog(self):
        text_dialog = TextInputDialog(self)
        result = text_dialog.exec_()

        if result == QDialog.Accepted:
            entered_text = text_dialog.get_text()
            self.label.setText(f"Введенный текст: {entered_text}")

app = QApplication(sys.argv)
main_window = MainWindow()

# Применение стилей к виджетам
main_window.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
    }
    
    QLabel {
        color: #333;
        font-size: 18px;
    }

    QPushButton {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        margin: 4px 2px;
        border-radius: 8px;
    }

    QPushButton:hover {
        background-color: #45a049;
    }

    QLineEdit {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }

    QDialogButtonBox {
        padding: 10px;
    }
""")

main_window.show()
sys.exit(app.exec_())
