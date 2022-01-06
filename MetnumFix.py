
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 421)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label_2.setObjectName("label_2")
        self.x1 = QtWidgets.QLineEdit(Dialog)
        self.x1.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.x1.setObjectName("x1")
        self.x2 = QtWidgets.QLineEdit(Dialog)
        self.x2.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.x2.setObjectName("x2")
        self.tombol = QtWidgets.QPushButton(Dialog)
        self.tombol.setGeometry(QtCore.QRect(230, 60, 75, 23))
        self.tombol.setObjectName("tombol")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.label_4.setObjectName("label_4")
        self.H1 = QtWidgets.QLineEdit(Dialog)
        self.H1.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.H1.setObjectName("H1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 210, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 230, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 250, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 270, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 290, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(30, 310, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(30, 330, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(30, 360, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.tombol.clicked.connect(self.tampung)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Masukan X0"))
        self.label_2.setText(_translate("Dialog", "Masukan X1"))
        self.tombol.setText(_translate("Dialog", "Hitung"))
        self.label_4.setText(_translate("Dialog", "Masukan H"))
        self.label_3.setText(_translate("Dialog", "Jawaban :"))


    def tampung(self):
        self.angka(int(self.x1.text()),int(self.x2.text()),float(self.H1.text()))


    def angka(self,X1,X2,tol):
        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_5.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+1) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+1) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_6.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+2) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+2) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_7.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+3) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+3) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_8.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+4) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+4) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_9.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+5) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+5) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_10.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+6) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+6) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_11.setText(str(a))

        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+7) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+7) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        #c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_12.setText(str(a))


        num_iter=2
        for i in range(1,num_iter,1):
            f_x_1=self.func(X1)
            f_x_2 =self.func(X2)
            print('x' + str(i+8) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            a = ('x' + str(i+8) + ' = ' + str(X2) + ' f(x) = ' + str(f_x_2))
            if abs(f_x_2) < tol:
                break
            x_3 = X2 - f_x_2 * ((X2 - X1) / (f_x_2 - f_x_1))
            X1 = X2
            X2 = x_3
        c = ('Error di : [' + str(X2) + ', ' + str(f_x_2) + ']')
        self.label_13.setText(str(a))
        self.label_14.setText(str(c))







    def func(self,x):
       f_x = (x ** 2) - 13 * x + 30
       return f_x



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
