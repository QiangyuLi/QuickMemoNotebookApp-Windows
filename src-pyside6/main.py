import sys
from PySide6.QtWidgets import QApplication
from app.windows.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 