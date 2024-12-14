class Calculator:
    def calculate(self, expression: str) -> str:
        """Calculate the result of a mathematical expression."""
        try:
            # Replace symbols with Python operators
            expression = expression.replace("÷", "/").replace("×", "*")
            result = eval(expression)

            # Return as integer if no decimal places are needed
            return str(int(result)) if result.is_integer() else str(result)
        except ZeroDivisionError:
            return "Error"  # Handle division by zero
        except Exception:
            return "Error"  # Handle invalid inputs

    def calculate_tip(self, amount: float, percentage: float) -> float:
        """Calculate tip based on amount and percentage."""
        return round(amount * percentage, 2)