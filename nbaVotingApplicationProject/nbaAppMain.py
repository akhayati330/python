from PyQt6.QtWidgets import QApplication, QMainWindow
from nbaVotingGui import VotingApp

def main():
    """Main function to launch the NBA voting app."""
    app = QApplication([])
    window = QMainWindow()
    ui = VotingApp(window)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()