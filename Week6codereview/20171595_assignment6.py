import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb, 'Name')

    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

        lbl_name = QLabel('Name', self)
        lbl_age = QLabel('Age', self)
        lbl_score = QLabel('Score', self)
        lbl_amount = QLabel('Amount', self)
        lbl_key = QLabel('key', self)
        lbl_result = QLabel('Result:', self)

        btn_add = QPushButton('Add')
        btn_del = QPushButton('Del')
        btn_find = QPushButton('Find')
        btn_inc = QPushButton('Inc')
        btn_show = QPushButton('Show')

        self.txt_name = QLineEdit()
        self.txt_age = QLineEdit()
        self.txt_score = QLineEdit()
        self.txt_amount = QLineEdit()
        self.txt_result = QTextEdit()

        self.com_key = QComboBox(self)
        self.com_key.addItem('Name')
        self.com_key.addItem('Age')
        self.com_key.addItem('Score')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(lbl_name)
        hbox1.addWidget(self.txt_name)
        hbox1.addWidget(lbl_age)
        hbox1.addWidget(self.txt_age)
        hbox1.addWidget(lbl_score)
        hbox1.addWidget(self.txt_score)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(lbl_amount)
        hbox2.addWidget(self.txt_amount)
        hbox2.addWidget(lbl_key)
        hbox2.addWidget(self.com_key)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(btn_add)
        hbox3.addWidget(btn_del)
        hbox3.addWidget(btn_find)
        hbox3.addWidget(btn_inc)
        hbox3.addWidget(btn_show)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(lbl_result)
        hbox4.addStretch(1)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.txt_result)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        btn_add.clicked.connect(self.buttonClicked)
        btn_del.clicked.connect(self.buttonClicked)
        btn_find.clicked.connect(self.buttonClicked)
        btn_inc.clicked.connect(self.buttonClicked)
        btn_show.clicked.connect(self.buttonClicked)

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def doScoreDB(self, txt, scdb):
        if txt == 'Add':
            try:
                record = {'Name': self.txt_name.text(), 'Age': int(self.txt_age.text()), 'Score': int(self.txt_score.text())}
            except ValueError:
                self.txt_result.setText("Enter a right command")
            else:
                scdb += [record]
                self.doScoreDB('Show', self.scoredb)
        elif txt == 'Del':
            new_list = [x for x in scdb if x['Name'] != self.txt_name.text()]
            self.scoredb = new_list
            self.doScoreDB('Show', self.scoredb)
        elif txt == 'Show':
            sortKey = self.com_key.currentText()
            try:
                self.showScoreDB(scdb, sortKey)
            except:
                self.txt_result.setText("Enter a right command")
        elif txt == 'Find':
            s = ""
            for p in scdb:
                if p['Name'] == self.txt_name.text():
                    for attr in sorted(p):
                        s += attr + "=" + str(p[attr]) + " "
                    s += '\n'
            self.txt_result.setText(s)
        elif txt == 'Inc':
            try:
                exception = int(self.txt_amount.text())
            except ValueError:
                self.txt_result.setText('Enter a right command')
            else:
                for p in scdb:
                    if p['Name'] == self.txt_name.text():
                        p['Score'] += int(self.txt_amount.text())
                self.doScoreDB('Show', self.scoredb)

    def showScoreDB(self, scdb, keyname):
        s = ""
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                s += attr + "=" + str(p[attr])
                s += " "
            s += '\n'
        self.txt_result.setText(s)

    def buttonClicked(self):
        sender = self.sender()
        self.doScoreDB(sender.text(), self.scoredb)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())