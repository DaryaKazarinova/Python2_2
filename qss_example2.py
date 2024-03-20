import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Выберите элемент из списка:")
        self.label.setObjectName("myLabel")  # Добавляем имя для применения стилей
        self.layout.addWidget(self.label)

        self.list_widget = QListWidget()
        self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3"])
        self.list_widget.currentItemChanged.connect(self.on_list_item_changed)
        self.list_widget.setObjectName("myListWidget")  # Добавляем имя для применения стилей
        self.layout.addWidget(self.list_widget)

    def on_list_item_changed(self, current_item):
        if current_item is not None:
            self.label.setText(f"Выбран элемент: {current_item.text()}")


app = QApplication(sys.argv)

# Применяем стили QSS
app.setStyleSheet("""
    #myLabel {
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
    }
    #myListWidget {
        background-color: #f0f0f0;
        border: 2px solid #ccc;
        border-radius: 5px;
        padding: 5px;
    }
    #myListWidget::item {
        padding: 5px;
    }
    #myListWidget::item:selected {
        background-color: #cce5ff;
    }
""")

main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())