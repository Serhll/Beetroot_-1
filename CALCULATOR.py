# ~~~~~~CALCULATOR~~~~~~~#
import sys
from functools import partial
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QGridLayout,
    QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

ERROR = 'Error'


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 350)
        self.general_layout = QVBoxLayout()

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)

        # Create display calculator
        self._create_display()

        # Create buttons
        self._create_buttons()

    def _create_display(self):
        """Calculator Display."""
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setReadOnly(True)

        self.general_layout.addWidget(self.display)
        self.display.setFont(QFont('GOST', 15))

    def _create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            'C': (0, 3),
            '/': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }
        for buttons_text, position in buttons.items():
            self.buttons[buttons_text] = QPushButton(buttons_text)
            self.buttons[buttons_text].setFixedSize(50, 50)
            buttons_layout.addWidget(
                self.buttons[buttons_text], position[0], position[1]
            )

        self.general_layout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def display_clear(self):
        self.set_display_text('')


class CalculatorController:

    def __init__(self, window, function):
        self._window = window
        self._evaluate = function
        self._connect_signals()

    def _build_expression(self, expression):
        if self._window.display_text() == ERROR:
            self._window.display_clear()
        expression = self._window.display_text() + expression
        self._window.set_display_text(expression)

    def _connect_signals(self):
        for button_text, button in self._window.buttons.items():
            if button_text not in {'=', 'C'}:
                button.clicked.connect(
                    partial(self._build_expression, button_text)
                )
        self._window.buttons['='].clicked.connect(self._calculate_result)
        self._window.display.returnPressed.connect(self._calculate_result)
        self._window.buttons['C'].clicked.connect(self._window.display_clear)

    def _calculate_result(self):
        result = self._evaluate(expression=self._window.display_text())
        self._window.set_display_text(result)


def evaluate_expression(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR
    return result


def main():
    calculator = QApplication(sys.argv)
    window = Calculator()
    window.show()
    CalculatorController(window=window, function=evaluate_expression)
    sys.exit(calculator.exec_())


if __name__ == '__main__':
    main()
