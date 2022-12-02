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
        self.number_display = QLineEditText("")
        self.solution = QLineEditText("0")
        
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
                x, y = int(6/number), (number-1)%3
                if number == 2:
                    layout_bottom_first.addWidget(number_button_dict[number], 2, y)
                elif number == 1:
                    layout_bottom_first.addWidget(number_button_dict[number], 2, y)
                else :
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
        self.operand = 0
        self.result = 0
        self.operator = ""
        self.entry = ""
        self.temp = ""
        self.chkop = True
        self.ce = False
        self.inputNum = False

    def number_button_clicked(self, num):
        if self.operator != "":
            self.solution.setText("")
        self.temp+=str(num)
        print(f"num_button {self.ce}  {self.inputNum}  {self.temp}")
        if self.ce and not self.inputNum and self.chkop:
            self.equation.setText("")
            self.entry = self.operand
            self.inputNum = True

        self.operand = int(self.temp)
        self.solution.setText(self.temp)
        self.chkop = True    

    def button_operation_clicked(self, operation):
        self.entry = "0" if self.entry == "" else self.entry
        self.temp = "0" if self.temp == "" else self.temp
        print(operation)
        if not self.chkop == False and self.operator == "":
            if operation == "+" :
                self.result = int(self.entry)+self.operand
                self.entry = str(self.result)
            elif operation == "-" :
                print(self.entry)
                self.result = self.operand if self.entry == "0" else int(self.entry) - self.operand
                self.entry = str(self.result)
            elif operation == "*":
                self.result = 1*self.operand
                self.entry = str(self.result)
        elif not self.chkop == False:
            if self.operator == "+" :
                self.result = int(self.entry)+self.operand
                self.entry = str(self.result)
            elif self.operator == "-" :
                print(self.entry)
                self.result = self.operand if self.entry == "0" else int(self.entry) - self.operand
                self.entry = str(self.result)
            elif self.operator == "*":
                self.result = int(self.entry)*self.operand
                self.entry = str(self.result)


        print(self.entry + " cc " + str(self.operand) + "   " + str(self.result))

        self.operator = operation
        equation = self.temp if self.equation.text() =="" else self.entry
        equation += operation
        self.equation.setText(equation)
        self.solution.setText(str(self.result))
        self.temp = ""
        self.chkop = False



    def button_equal_clicked(self):
        if self.inputNum:
            self.temp = self.entry
            self.entry = str(self.operand)
            self.operand = int(self.temp)
            self.temp = "0"
            self.ce = False
            self.inputNum = False
        else:
            self.ce = False
        equation = self.entry + self.operator + str(self.operand) + "="
        self.entry = "0" if self.entry=="" else self.entry
        if self.operator == "+":
            self.result = int(self.entry)+self.operand
        elif self.operator == "-":
            self.result = int(self.entry)-self.operand
        elif self.operator == "*":
            self.result = int(self.entry)*self.operand
        self.entry = str(self.result)
        self.equation.setText(equation)
        self.solution.setText(str(self.result))
        self.temp = ""
        self.chkop = False
        self.ce = True

        print(f"{self.entry} + {self.operator} + {self.operand} + {self.result}")


    def button_clear_clicked(self):
        self.operand = 0
        self.result = 0
        self.operator = ""
        self.entry = ""
        self.temp = ""
        self.chkop = True
        self.ce = False
        self.inputNum = False
        self.solution.setText("")

    def button_clear_entry_clicked(self):
        self.result = 0
        self.temp = ""
        self.entry = "0"
        self.chkop = True
        self.ce = True
        self.equation.setText("")
        self.solution.setText("0")
        
    def button_backspace_clicked(self):
        if self.chkop and not self.temp == "":
            self.operand = int(self.operand/10)
            self.temp = "" if self.operand==0 else str(self.operand)
            solution = "0" if len(self.solution.text()) == 1 else self.solution.text()[:-1]
            self.solution.setText(solution)
        else:
            self.equation.setText("")
            self.temp = self.entry

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())