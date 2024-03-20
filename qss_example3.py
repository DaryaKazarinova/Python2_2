import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QSpinBox, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Выберите число:")
        self.layout.addWidget(self.label)

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(100)
        self.spin_box.valueChanged.connect(self.on_spin_box_value_changed)
        self.layout.addWidget(self.spin_box)

        # Применяем стили из файла styles.qss
        with open('style.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def on_spin_box_value_changed(self, value):
        self.label.setText(f"Выбрано число: {value}")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
