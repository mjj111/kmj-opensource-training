import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class QPushButtonOperation(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class QPushButtonNumber(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class QLineEditText(QLineEdit):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        layout_bottom = QHBoxLayout()
        layout_equation_solution = QVBoxLayout()
        layout_top_first = QHBoxLayout()
        layout_top_second = QHBoxLayout()
        layout_bottom_first = QGridLayout()
        layout_bottom_second = QVBoxLayout()

######### layout_equation_solution #########
        ### later
        self.equation = QLineEditText("")
        self.solution = QLineEditText("")
        self.equation.setAlignment(Qt.AlignRight)
        self.solution.setAlignment(Qt.AlignRight)



        ######### layout_top_first #########
        ### create widget
        button_backspace = QPushButtonOperation("<=")
        button_clear = QPushButtonOperation("C")
        button_clear_entry = QPushButtonOperation("CE")
        button_mod = QPushButtonOperation("%")

        ### addWidget ot layout_top_first
        layout_top_first.addWidget(button_mod)
        layout_top_first.addWidget(button_clear_entry)
        layout_top_first.addWidget(button_clear)
        layout_top_first.addWidget(button_backspace)
         ### function - later
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        #button_clear_entry.clicked.connect(self.button_clear_entry_clicked)
        #button_mod.clicked.connect(self.button_negate_clicked)



        ######### layout_top_second #########
        ### create widget
        button_reverse = QPushButtonOperation("¹/×")
        button_pow = QPushButtonOperation("pow")
        button_sqrt = QPushButtonOperation("sqrt")
        button_division = QPushButtonOperation("÷")

        ### addWidget ot layout_top_second
        layout_top_second.addWidget(button_reverse)
        layout_top_second.addWidget(button_pow)
        layout_top_second.addWidget(button_sqrt)
        layout_top_second.addWidget(button_division)
        
        
       ### function - later
        #button_reverse.clicked.connect(self.button_reverse_clicked)
        #button_pow.clicked.connect(self.button_pow_clicked)
        #button_sqrt.clicked.connect(self.button_sqrt_clicked)
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))



        

        ######### layout_bottom_first #########
        ### create widget + add widget + function
        number_button_dict = {}
        button_dot = QPushButtonNumber(".")
        button_negate = QPushButtonNumber("⁺/₋")

        layout_bottom_first.addWidget(button_negate, 3, 0)
        layout_bottom_first.addWidget(button_dot, 3, 2)

        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        #button_negate.clicked.connect(self.button_negate_clicked)
        
        for number in range(0, 10):
            number_button_dict[number] = QPushButtonNumber(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number:
                                                       self.number_button_clicked(num))
            if number > 0:
                x, y = divmod(number - 1, 3)
                layout_bottom_first.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_bottom_first.addWidget(number_button_dict[number], 3, 1)

        ######### layout_bottom_second #########
        ### create widget
        button_product = QPushButtonNumber("×")
        button_plus = QPushButtonNumber("＋")
        button_minus = QPushButtonNumber("－")
        button_equal = QPushButtonNumber("=")

        ### add widget to layout_bottom_second
        layout_bottom_second.addWidget(button_product)
        layout_bottom_second.addWidget(button_plus)
        layout_bottom_second.addWidget(button_minus)
        layout_bottom_second.addWidget(button_equal)
######### layout_bottom_second #########
        ### create widget
        button_product = QPushButtonNumber("×")
        button_plus = QPushButtonNumber("＋")
        button_minus = QPushButtonNumber("－")
        button_equal = QPushButtonNumber("=")

        ### add widget to layout_bottom_second
        layout_bottom_second.addWidget(button_product)
        layout_bottom_second.addWidget(button_plus)
        layout_bottom_second.addWidget(button_minus)
        layout_bottom_second.addWidget(button_equal)

        ### function - later
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_equal.clicked.connect(self.button_equal_clicked)



        ######### layout_equation_solution #########
        layout_equation_solution.addWidget(self.equation, stretch = 1)
        layout_equation_solution.addWidget(self.solution, stretch = 9)


        ######### layout_bottom #########
        layout_bottom.addLayout(layout_bottom_first, stretch = 75)
        layout_bottom.addLayout(layout_bottom_second,  stretch = 25)



        ### function - later
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_equal.clicked.connect(self.button_equal_clicked)



        ######### layout_equation_solution #########
        layout_equation_solution.addWidget(self.equation, stretch = 1)
        layout_equation_solution.addWidget(self.solution, stretch = 9)


        ######### layout_bottom #########
        layout_bottom.addLayout(layout_bottom_first, stretch = 75)
        layout_bottom.addLayout(layout_bottom_second,  stretch = 25)



        ######### layout_main #########
        main_layout.addLayout(layout_equation_solution, stretch = 250)
        main_layout.addLayout(layout_top_first, stretch = 125)
        main_layout.addLayout(layout_top_second, stretch = 125)
        main_layout.addLayout(layout_bottom, stretch = 500)


        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())