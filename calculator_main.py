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

        ######### 레이아웃 초기 설정 #########
        main_layout = QVBoxLayout()
        layout_bottom = QHBoxLayout()
        layout_equation_solution = QVBoxLayout()
        layout_top_first = QHBoxLayout()
        layout_top_second = QHBoxLayout()
        layout_bottom_first = QGridLayout()
        layout_bottom_second = QVBoxLayout()



        ######### layout_equation_solution #########
        ### later
        self.number_display = QLineEditText("")
        self.equation = QLineEditText("")
        self.solution = QLineEditText("0")
        self.equation.setAlignment(Qt.AlignRight)
        self.solution.setAlignment(Qt.AlignRight)



        ######### layout_top_first #########
        ### create widget
        button_backspace = QPushButtonOperation("<=")
        button_clear = QPushButtonOperation("C")
        button_clear_entry = QPushButtonOperation("CE")
        button_per = QPushButtonOperation("%")

        ### addWidget ot layout_top_first
        layout_top_first.addWidget(button_per)
        layout_top_first.addWidget(button_clear_entry)
        layout_top_first.addWidget(button_clear)
        layout_top_first.addWidget(button_backspace)

        ### function - later
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clear_entry.clicked.connect(self.button_clear_entry_clicked)
        button_per.clicked.connect(self.button_per_clicked)



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
        button_reverse.clicked.connect(self.button_reverse_clicked)
        button_pow.clicked.connect(self.button_pow_clicked)
        button_sqrt.clicked.connect(self.button_sqrt_clicked)
        button_division.clicked.connect(lambda state, operation = "÷": self.button_operation_clicked(operation))



        ######### layout_bottom_first #########
        ### create widget + add widget + function
        number_button_dict = {}
        button_dot = QPushButtonNumber(".")
        button_negate = QPushButtonNumber("⁺/₋")

        layout_bottom_first.addWidget(button_negate, 3, 0)
        layout_bottom_first.addWidget(button_dot, 3, 2)

        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        button_negate.clicked.connect(self.button_negate_clicked)

        for number in range(0, 10):
            number_button_dict[number] = QPushButtonNumber(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))
            if number > 0:
                x, y = int(6/number), (number-1)%3
                if number == 2:
                    layout_bottom_first.addWidget(number_button_dict[number], 2, y)
                elif number == 1:
                    layout_bottom_first.addWidget(number_button_dict[number], 2, y)
                else :
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

        ### function - later
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "x": self.button_operation_clicked(operation))
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

        self.entry = 0
        self.operand = 0
        self.result = 0
        self.operator = ""
        self.chkop = True
        self.inputNum = False
        self.enter = False
        self.swap = False
        self.bs = False

    def is_int(self, n):
        if abs(n - int(n)) < 0.0000001:
            return int(n)
        else:
            return n

    def number_button_clicked(self, num):
        if self.inputNum:
            solution = ""
            self.inputNum = False
        elif self.enter:
            self.entry = self.operand
            solution = ""
            self.equation.setText("")
            self.enter = False
            self.swap = True
        else:
            solution = "" if self.solution.text() == "0" else self.solution.text()

        if num == '.' and solution == "":
            solution = "0"
        solution += str(num)
        self.operand = float(solution)
        self.solution.setText(solution)
        self.bs = True

    def calculator(self, op, op2):
        print("Check!", self.entry, self.operand, self.result)
        print(str(11111.66666))
        if self.operand:
            if op == '+':
                self.result = self.entry + self.operand
            elif op == '-':
                self.result = self.entry - self.operand
            elif op == '÷':
                self.entry = 1 if self.entry == 0 else self.entry
                self.result = self.entry / self.operand
                print(type(self.result))
            elif op == 'x':
                self.entry = 1 if self.entry == 0 else self.entry
                self.result = self.entry * self.operand
            else:
                self.result = float(self.solution.text())

            self.result = self.is_int(self.result)
            self.equation.setText(str(self.result)+op2)
            self.solution.setText(str(self.result))
            self.entry = float(self.solution.text())

        else:
            return

    def button_operation_clicked(self, operation):
        if self.chkop:
            equation = self.solution.text()
            self.chkop = False
        else:
            equation = self.solution.text() if self.equation.text()=="" else self.equation.text()

        equation += operation
        self.equation.setText(equation)


        self.calculator(self.operator, operation)

        self.operator = operation
        self.operand = 0
        self.inputNum = True
        self.chkop = True
        self.bs = False

    def button_equal_clicked(self):
        print(self.operator, self.entry, self.result, self.operand)
        if self.operator == "":
            self.result=self.operand
            self.result=self.is_int(self.result)
            self.equation.setText(str(self.result)+"=")
            self.solution.setText(str(self.result))
            return

        self.entry = self.is_int(self.entry)
        self.operand = self.is_int(self.operand)
        if self.operand == 0:
            self.result = self.entry
            self.operand = self.entry
        if self.swap:
            self.result = self.operand
            self.operand = self.entry
            self.swap = False

        self.entry = self.result
        equation = str(self.result)+self.operator+str(self.operand)
        equation+="="

        print(self.result, self.entry, self.operand, self.operator, self.equation)
        if self.operator == "+":
            self.result = float(self.result) + self.operand
        elif self.operator == "÷":
            self.result = float(self.result) / self.operand
        elif self.operator == "x":
            self.result = float(self.result) * self.operand
        elif self.operator == "-":
            self.result = float(self.result) - self.operand

        self.result = self.is_int(self.result)
        print(self.entry)
        self.equation.setText(equation)
        self.solution.setText(str(self.result))
        self.enter = True
        self.bs = True

    def button_clear_clicked(self):
        self.entry = 0
        self.operand = 0
        self.result = 0
        self.operator = ""
        self.chkop = True
        self.inputNum = False
        self.enter = False
        self.swap = False
        self.equation.setText("")
        self.solution.setText("")

    def button_clear_entry_clicked(self):
        print(self.entry, self.operand, self.result)

        if self.enter:
            self.entry = self.operand
            self.result = 0
            self.entry = 0

            self.solution.setText("")
            self.equation.setText("")
        else:
            self.solution.setText("")
            self.operand = 0
        self.chkop = True
        self.inputNum = False
        self.enter = False
        self.swap = False


    def button_reverse_clicked(self):
        if self.enter:
            self.result = 1/self.result
            self.result = self.is_int(self.result)
            self.solution.setText(str(self.result))
        elif self.operand == 0:
            self.operand = 1/float(self.result)
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))
        else:
            print("CHECK", self.operand, self.result, self.entry)
            self.operand = 1/float(self.operand)
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))
        self.equation.setText("역수")
        self.bs = False

    def button_pow_clicked(self):
        if self.enter:
            self.result = float(self.result) ** 2
            self.result = self.is_int(self.result)
            self.solution.setText(str(self.result))
        elif self.operand == 0:
            self.operand = float(self.result)**2
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))
        else:
            self.operand = float(self.operand)**2
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))
        self.equation.setText("제곱")
        self.bs = False


    def button_sqrt_clicked(self):
        if self.enter:
            self.result = float(self.result) ** 0.5
            self.result = self.is_int(self.result)
            self.solution.setText(str(self.result))
        elif self.operand == 0:
            self.operand = float(self.result)**0.5
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))
        else:
            self.operand = float(self.operand)**0.5
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))

        self.equation.setText("제곱근")
        self.bs = False

    def button_per_clicked(self):
        print(self.operator, self.entry, self.result, self.operand)
        if self.operator=="x" or self.operator=="÷":
            print("CHECK")
            if self.enter:
                print("CHECK1")
                self.result = float(self.result) * 0.01
                self.result = self.is_int(self.result)
                self.solution.setText(str(self.result))
            elif self.operand == 0:
                self.operand = float(self.result) * 0.01
                self.operand = self.is_int(self.operand)
                self.solution.setText(str(self.operand))
            else:
                print("CHECK2")
                self.operand = float(self.operand)*0.01
                self.operand = self.is_int(self.operand)
                self.solution.setText(str(self.operand))
        elif self.operator=="+" or self.operator == "-":
            if self.enter:
                print("CHECK1")
                self.result = float(self.result) * float(self.result)
                self.result = self.is_int(self.result)
                self.solution.setText(str(self.result))
            elif self.operand == 0:
                self.operand = float(self.result) ** 2 * 0.01
                self.operand = self.is_int(self.operand)
                self.solution.setText(str(self.operand))
            else:
                print("CHECK2")
                self.operand = float(self.entry) * self.operand * 0.01
                self.operand = self.is_int(self.operand)
                self.solution.setText(str(self.operand))
        else:
            self.operand = 0
            self.solution.setText(str(self.operand))

        self.equation.setText("퍼센트로 전환")
        self.bs = False

    def button_negate_clicked(self):
        print(self.operand)
        if self.enter:
            self.result = -self.result
            self.result = self.is_int(self.result)
            self.solution.setText(str(self.result))
        elif self.operand==0:
            self.operand = -self.entry
            self.operand = self.is_int(self.operand)
            self.solution.setText(str(self.operand))
        else:
            self.operand = -self.operand
            print(self.operand)
            self.operand = self.is_int(self.operand)
            print(self.operand)
            self.solution.setText(str(self.operand))
        self.equation.setText("역수로 전환")

    def button_backspace_clicked(self):
        if self.bs:
            print("CHECK")
            if self.enter:
                self.equation.setText("")
                self.enter = False
            else:
                solution = self.solution.text()
                solution = solution[:-1]
                if solution == "": solution = "0"
                self.operand = float(solution)
                print("CHECK", solution, self.operand)
                self.solution.setText(solution)
        else:
            return
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())