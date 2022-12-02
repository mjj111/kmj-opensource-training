import sys
from PyQt5.QtWidgets import *

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

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addWidget(self.equation)
        layout_equation_solution.addWidget(self.solution)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_backspace = QPushButton("<=")
        button_clear = QPushButton("C")
        button_clear_entry = QPushButton("CE")
        button_mod = QPushButton("%")
        button_reverse = QPushButton("¹/×")
        button_pow = QPushButton("pow")
        button_sqrt = QPushButton("sqrt")
        button_division = QPushButton("÷")
        button_dot = QPushButton(".")
        button_negate = QPushButton("⁺/₋")
        button_equal = QPushButton("=")

        layout_top_first.addWidget(button_mod)
        layout_top_first.addWidget(button_clear_entry)
        layout_top_first.addWidget(button_clear)
        layout_top_first.addWidget(button_backspace)
        layout_top_second.addWidget(button_reverse)
        layout_top_second.addWidget(button_pow)
        layout_top_second.addWidget(button_sqrt)
        layout_top_second.addWidget(button_division)
        layout_bottom_first.addWidget(button_negate, 3, 0)
        layout_bottom_first.addWidget(button_dot, 3, 2)
        layout_bottom_second.addWidget(button_product)
        layout_bottom_second.addWidget(button_plus)
        layout_bottom_second.addWidget(button_minus)
        layout_bottom_second.addWidget(button_equal)
        
        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))



        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)


        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number:
                                                       self.number_button_clicked(num))
            if number > 0:
                x, y = divmod(number - 1, 3)
                layout_bottom_first.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_bottom_first.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        layout_bottom.addLayout(layout_bottom_first)
        layout_bottom.addLayout(layout_bottom_second)
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_top_first)
        main_layout.addLayout(layout_top_second)
        main_layout.addLayout(layout_bottom)

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