import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget


class DataInputWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        pass
        # Создаем виджеты

        # Создаем главный макет

        # Устанавливаем макет для главного окна

        # Назначаем обработчик события для кнопки

        # Устанавливаем параметры главного окна

    def add_data_to_list(self):
        pass
        # Получаем текст из поля ввода

        # Добавляем текст в список

        # Очищаем поле ввода



app = QApplication(sys.argv)
data_input_window = DataInputWidget()
data_input_window.show()
app.exec_()
