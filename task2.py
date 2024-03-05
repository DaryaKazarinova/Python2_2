import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Создаем виджеты
        self.label = QLabel('Введите текст:')
        self.text_edit = QLineEdit()

        # Создаем главный макет
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        layout.addWidget(button)

        # Устанавливаем макет для главного окна
        self.setLayout(layout)

        # Назначаем обработчик события для кнопки
        button.clicked.connect(self.on_button_click)

        # Устанавливаем параметры главного окна
        self.setWindowTitle('Пример приложения с PySide')
        self.setGeometry(100, 100, 400, 200)

    def on_button_click(self):
        # Обработчик события для кнопки
        self.label.setText(f'Введенный текст: {entered_text}')



app = QApplication(sys.argv)
main_window = MainWindow()
app.exec_()
