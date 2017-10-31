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
        self.showScoreDB()
        
        
    def initUI(self):


        NameBox = QLabel('Name:')
        Name_Box = QLineEdit()
        AgeBox = QLabel('Age:')
        Age_Box = QLineEdit()
        ScoreBox = QLabel('Score:')
        Score_Box = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(NameBox)
        hbox1.addWidget(Name_Box)
        hbox1.addWidget(AgeBox)
        hbox1.addWidget(Age_Box)
        hbox1.addWidget(ScoreBox)
        hbox1.addWidget(Score_Box)

        AmountBox = QLabel('Amount:')
        Amount_Box = QLineEdit()
        KeyBox = QLabel('Key:')
        Key_Box = QComboBox()
        Key_Box.addItems(['Name','Age','Score'])

        hbox2 = QHBoxLayout()
        hbox2.addStretch(4)
        hbox2.addWidget(AmountBox)
        hbox2.addWidget(Amount_Box)
        hbox2.addWidget(KeyBox)
        hbox2.addWidget(Key_Box)


        Addpushbutton = QPushButton("Add")
        Delpushbutton = QPushButton("Del")
        Findpushbutton = QPushButton("Find")
        Incpushbutton = QPushButton("Inc")
        Showpushbutton = QPushButton("Show")

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(Addpushbutton)
        hbox3.addWidget(Delpushbutton)
        hbox3.addWidget(Findpushbutton)
        hbox3.addWidget(Incpushbutton)
        hbox3.addWidget(Showpushbutton)

        ResultBox = QLabel('Result:')
        hbox4 = QHBoxLayout()
        hbox4.addWidget(ResultBox)

        Result_Box = QTextEdit()
        hbox5 = QHBoxLayout()
        hbox5.addWidget(Result_Box)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)


        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

        Addpushbutton.clicked.connect(self.Addclicked)
        Delpushbutton.clicked.connect(self.Delclicked)
        Findpushbutton.clicked.connect(self.Findclicked)
        Incpushbutton.clicked.connect(self.Incclicked)
        Showpushbutton.clicked.connect(self.Showclicked)

    def Addclicked(self,scdb):
        record = {'Name': self.Name_box(),'Age': int(self.Age_box()), 'Score': int(self.Score_box())}
        scdb += [record]

    def Delclicked(self,scdb):
        del2 = []
        index = 0
        for p in scdb:
            if p['Name'] == self.name_box():
                del2.append(index)
            index += 1
        for i in reversed(del2):
        scdb.pop(i)

    def Findclicked(self,scdb):
        sortKey = 'Name' if len(self.Name_box.text()) == 1 else

    def Incclicked(self,scdb):
        for p in scdb:
            if p['Name'] == self.Namebox.text():
                p['Score'] = int(p['Score'])
        p['Score'] += int(self.Scorebox.text())

    def Showclicked(self,scdb):
        sortKey = 'Name' if len(self.Name_box.text()) == 1 else


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        scdb=[]
        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()
        return scdb


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,scdb):
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + p[attr], end=' ')
        print()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





