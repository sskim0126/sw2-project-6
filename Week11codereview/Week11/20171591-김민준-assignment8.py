from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy, QLayout, QGridLayout

from listtool import constant
from keypad import numPadList, operatorList, constantList, functionList
import calcfunction

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()
        for i in range(0, 4): #list 모듈
            if key == constantList[i]:
                self.display.setText(constant[i]) #반복문 사용후에 text값을 constant 인덱스값으로 리턴한다.
                return
        for j in range(0,4): #함수
            if key == functionList[j]:
                n = self.display.text()
                if j == 0:
                    value = calcfunction.factorial(n)
                elif j == 1:
                    value = calcfunction.decToBin(n)
                elif j == 2:
                    value = calcfunction.binToDec(n)
                elif j == 3:
                    value = calcfunction.decToRoman(n)
                self.display.setText(str(value))
                return
        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except ZeroDivisionError:
                result = 'do not divide 0' #0으로 나누는 예외처리
            # except self.display.setMaxLength() > 15:
            #     result = 'key range = 15' #key값이 15가 넘으면 예외처리
            except :
                result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()

        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())