from PyQt5 import QtGui, QtWidgets
import First
import FinishUpd
import FinishQ
import sys
import AC_Automaton
import tryi
import CntMatrixCal
import time
import IC
import NewCalculation

class Form1(QtWidgets.QWidget, First.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Update)
        self.pushButton_2.clicked.connect(self.Cal)
        self.pushButton_3.clicked.connect(self.getRoute3)
        self.pushButton_5.clicked.connect(self.getRoute5)
        self.pushButton_6.clicked.connect(self.bye)
        self.Windows2 = None
        self.Windows3 = None

    def bye(self):
        inRoute = self.textEdit_3.toPlainText().strip()
        print(inRoute)
        outRoute = self.textEdit_4.toPlainText().strip()
        print(outRoute)
        NewCalculation.main(inRoute, outRoute)

    def getRoute3(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.textEdit_3.append(filename)

    def getRoute5(self):
        #filename = QtWidgets.QFileDialog.getExistingDirectory()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.textEdit_4.append(filename)

    def Update(self):
        if self.Windows2 == None:
            self.Windows2 = Form2()
        s = time.time()
        print (s)
        Text1 = self.textEdit.toPlainText()
        list = AC_Automaton.get_symptom(Text1)
        Text2 = self.textEdit_2.toPlainText()
        medi = Text2.split()
        file = open('Stat.txt', 'a', encoding='utf-8')
        file.write(str(s))
        for adr in list:
            file.write('|' + adr)
        file.write('\n')
        file.close()
        file = open('SourceData\ItemID.txt', 'a', encoding='utf-8')
        file.write(str(s))
        for medicine in medi:
            file.write('|' + medicine)
        file.write('\n')
        file.close()
        CntMatrixCal.main()
        IC.main()
        self.Windows2.show()

    def Cal(self):
        if self.Windows3 == None:
            self.Windows3 = Form3()
        Text1 = self.textEdit.toPlainText()
        Text2 = self.textEdit_2.toPlainText()
        medi = Text2.split()
        list = AC_Automaton.get_symptom(Text1)
        vis = []
        for x in list:
            vis.append(x)
        a,b,c,d = tryi.get(medi)
        for x in a:
            if x in vis:
                vis.remove(x)
                self.Windows3.textBrowser.append(x)
        for x in b:
             if x in vis:
                 vis.remove(x)
                 self.Windows3.textBrowser_2.append(x)
        for x in c:
            if x in vis:
                vis.remove(x)
                self.Windows3.textBrowser_3.append(x)
        for x in d:
            if x in vis:
                vis.remove(x)
                self.Windows3.textBrowser_4.append(x)
        self.Windows3.show()

class Form2(QtWidgets.QWidget, FinishUpd.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

class Form3(QtWidgets.QWidget, FinishQ.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())