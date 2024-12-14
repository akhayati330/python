from PyQt6.QtWidgets import (
    QVBoxLayout, QGridLayout, QPushButton, QLabel, QWidget, QStackedWidget
)
from PyQt6.QtCore import Qt
from enhancedCalculatorLogic import Calculator


class EnhancedCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the calculator logic
        self.calculator = Calculator()

        # Main layout
        self.layout = QVBoxLayout(self)

        # Stacked widget to switch between calculator and tip screen
        self.stack = QStackedWidget(self)
        self.layout.addWidget(self.stack)

        # Create calculator screen
        self.calculator_screen = QWidget()
        self.init_calculator_screen()
        self.stack.addWidget(self.calculator_screen)

        # Create tip screen
        self.tip_screen = QWidget()
        self.init_tip_screen()
        self.stack.addWidget(self.tip_screen)

        # Set the default screen
        self.stack.setCurrentWidget(self.calculator_screen)

    def init_calculator_screen(self):
        """Initialize the calculator screen layout."""
        layout = QVBoxLayout(self.calculator_screen)

        # Display for the results
        self.display = QLabel("0", alignment=Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet(
            "background-color: white; color: black; font-size: 24px; padding: 10px; border: 1px solid black;"
        )
        self.display.setFixedHeight(60)
        layout.addWidget(self.display)

        # Button layout
        buttons_layout = QGridLayout()
        layout.addLayout(buttons_layout)

        # Button texts
        buttons = [
            ("C", 0, 0), ("÷", 0, 1), ("×", 0, 2), ("-", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("Tip", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("=", 3, 3),
            ("0", 4, 0, 2), (".", 4, 2)
        ]

        # Create buttons dynamically
        for button_text, row, col, colspan in [(*b, 1) if len(b) == 3 else b for b in buttons]:
            button = QPushButton(button_text)
            button.setStyleSheet("font-size: 18px; padding: 10px;")
            button.clicked.connect(lambda _, text=button_text: self.handle_button_click(text))
            buttons_layout.addWidget(button, row, col, 1, colspan)

    def init_tip_screen(self):
        """Initialize the tip screen layout."""
        layout = QVBoxLayout(self.tip_screen)

        # Tip instructions
        layout.addWidget(QLabel("Select Tip Percentage:", alignment=Qt.AlignmentFlag.AlignCenter))

        # Tip buttons
        tip_buttons_layout = QGridLayout()
        layout.addLayout(tip_buttons_layout)

        tip_percentages = [10, 15, 20, 25]
        for i, percentage in enumerate(tip_percentages):
            button = QPushButton(f"{percentage}%")
            button.setStyleSheet("font-size: 18px; padding: 10px;")
            button.clicked.connect(lambda _, percent=percentage: self.calculate_tip(percent))
            tip_buttons_layout.addWidget(button, i // 2, i % 2)

        # Back button to return to calculator
        back_button = QPushButton("Back")
        back_button.setStyleSheet("font-size: 18px; padding: 10px;")
        back_button.clicked.connect(self.return_to_calculator)
        layout.addWidget(back_button)

    def handle_button_click(self, button_text: str):
        """Handle button clicks and update the display."""
        if button_text == "C":
            self.display.setText("0")
        elif button_text == "=":
            result = self.calculator.calculate(self.display.text())
            self.display.setText(result)
        elif button_text == "Tip":
            self.stack.setCurrentWidget(self.tip_screen)
        else:
            current_text = self.display.text()
            if current_text == "0":
                current_text = ""
            self.display.setText(current_text + button_text)

    def calculate_tip(self, percentage: int):
        """Calculate the tip based on the entered amount and percentage."""
        current_text = self.display.text()
        try:
            amount = float(current_text)
            tip = self.calculator.calculate_tip(amount, percentage / 100)
            self.display.setText(f"{tip}")
        except ValueError:
            self.display.setText("Error")
        self.stack.setCurrentWidget(self.calculator_screen)

    def return_to_calculator(self):
        """Return to the calculator screen."""
        self.stack.setCurrentWidget(self.calculator_screen)