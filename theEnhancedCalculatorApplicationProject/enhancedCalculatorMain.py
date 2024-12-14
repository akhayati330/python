from PyQt6.QtWidgets import QApplication, QMainWindow
from enhancedCalculatorGui import EnhancedCalculatorApp


def main():
    """Main function to launch the Enhanced Calculator app."""
    app = QApplication([])
    window = QMainWindow()
    ui = EnhancedCalculatorApp()
    window.setCentralWidget(ui)
    window.setWindowTitle("Enhanced Calculator App")
    window.setGeometry(100, 100, 400, 700)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()