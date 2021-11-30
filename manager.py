from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from view import Ui_ViewWindow
from edit import Ui_EditWindow
import sqlite3
import random
import string


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 404)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "/safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 491, 371))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.managerTab = QtWidgets.QWidget()
        self.managerTab.setObjectName("managerTab")
        self.siteLineEdit = QtWidgets.QLineEdit(self.managerTab)
        self.siteLineEdit.setGeometry(QtCore.QRect(170, 60, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.siteLineEdit.setFont(font)
        self.siteLineEdit.setText("")
        self.siteLineEdit.setObjectName("siteLineEdit")
        self.siteLabel = QtWidgets.QLabel(self.managerTab)
        self.siteLabel.setGeometry(QtCore.QRect(10, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.siteLabel.setFont(font)
        self.siteLabel.setObjectName("siteLabel")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.managerTab)
        self.usernameLineEdit.setGeometry(QtCore.QRect(170, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.usernameLabel = QtWidgets.QLabel(self.managerTab)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.managerTab)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setGeometry(QtCore.QRect(170, 160, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLabel = QtWidgets.QLabel(self.managerTab)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.saveBtn = QtWidgets.QPushButton(
            self.managerTab, clicked=lambda: self.save_it())
        self.saveBtn.setGeometry(QtCore.QRect(360, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.saveBtn.setFont(font)
        self.saveBtn.setFlat(False)
        self.saveBtn.setObjectName("saveBtn")
        self.viewPassword_pushBtn = QtWidgets.QPushButton(
            self.managerTab, clicked=lambda: self.viewWindow())
        self.viewPassword_pushBtn.setGeometry(QtCore.QRect(190, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.viewPassword_pushBtn.setFont(font)
        self.viewPassword_pushBtn.setFlat(False)
        self.viewPassword_pushBtn.setObjectName("viewPassword_pushBtn")
        self.tabWidget.addTab(self.managerTab, "")
        self.genTab = QtWidgets.QWidget()
        self.genTab.setObjectName("genTab")
        self.usernameLineEdit_2 = QtWidgets.QLineEdit(self.genTab)
        self.usernameLineEdit_2.setGeometry(QtCore.QRect(170, 90, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.usernameLineEdit_2.setFont(font)
        self.usernameLineEdit_2.setText("")
        self.usernameLineEdit_2.setObjectName("usernameLineEdit_2")
        self.siteLabel_2 = QtWidgets.QLabel(self.genTab)
        self.siteLabel_2.setGeometry(QtCore.QRect(10, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.siteLabel_2.setFont(font)
        self.siteLabel_2.setObjectName("siteLabel_2")
        self.usernameLabel_2 = QtWidgets.QLabel(self.genTab)
        self.usernameLabel_2.setGeometry(QtCore.QRect(10, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.usernameLabel_2.setFont(font)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.siteLineEdit_2 = QtWidgets.QLineEdit(self.genTab)
        self.siteLineEdit_2.setGeometry(QtCore.QRect(170, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.siteLineEdit_2.setFont(font)
        self.siteLineEdit_2.setText("")
        self.siteLineEdit_2.setObjectName("siteLineEdit_2")
        self.passwordLengthLabel = QtWidgets.QLabel(self.genTab)
        self.passwordLengthLabel.setGeometry(QtCore.QRect(10, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.passwordLengthLabel.setFont(font)
        self.passwordLengthLabel.setObjectName("passwordLengthLabel")
        self.passwordLength_spinBox = QtWidgets.QSpinBox(self.genTab)
        self.passwordLength_spinBox.setGeometry(
            QtCore.QRect(170, 140, 301, 34))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.passwordLength_spinBox.setFont(font)
        self.passwordLength_spinBox.setMinimum(5)
        self.passwordLength_spinBox.setMaximum(15)
        self.passwordLength_spinBox.setObjectName("passwordLength_spinBox")
        self.generateBtn = QtWidgets.QPushButton(
            self.genTab, clicked=lambda: self.generate())
        self.generateBtn.setGeometry(QtCore.QRect(170, 210, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.generateBtn.setFont(font)
        self.generateBtn.setFlat(False)
        self.generateBtn.setObjectName("generateBtn")
        self.passwordOutput_lineEdit = QtWidgets.QLineEdit(self.genTab)
        self.passwordOutput_lineEdit.setGeometry(
            QtCore.QRect(20, 280, 301, 31))
        self.passwordOutput_lineEdit.setReadOnly(True)
        self.passwordOutput_lineEdit.setObjectName("passwordOutput_lineEdit")
        self.copyBtn = QtWidgets.QPushButton(
            self.genTab, clicked=lambda: self.copy())
        self.copyBtn.setGeometry(QtCore.QRect(340, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.copyBtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "fugue-icons-3.5.6/icons/documents-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.copyBtn.setIcon(icon)
        self.copyBtn.setObjectName("copyBtn")
        self.tabWidget.addTab(self.genTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.create_table()

    def viewWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ViewWindow()
        self.ui.setupUi(self.window)
        self.tableWidget = self.ui.tableWidget
        self.ui.delete_pushButton.clicked.connect(self.delete_password)
        self.ui.edit_pushButton.clicked.connect(self.ui.editWindow)
        self.view_password()
        self.window.show()

    def view_password(self):
        # Create Database
        conn = sqlite3.connect('password_manager.db')

        # Create Cursor
        c = conn.cursor()
        records = c.execute("SELECT * FROM password")

        table = self.tableWidget

        table.setRowCount(0)
        table.setColumnCount(3)
        for row, record in enumerate(records):
            table.insertRow(row)

            for col, data in enumerate(record):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(data)))

        columns = ['Website', 'Username', 'Password']
        table.setHorizontalHeaderLabels(columns)
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        clicked = self.tableWidget.currentRow()

        conn.commit()
        conn.close()

    def delete_password(self):
        conn = sqlite3.connect('password_manager.db')
        # Create Cursor
        c = conn.cursor()

        # Get the current row selected
        clicked = self.tableWidget.currentRow()

        # Delete selected Row
        self.tableWidget.removeRow(clicked)

        c.execute(f'DELETE from password WHERE rowid= {clicked+1}')

        conn.commit()
        conn.close()

    def create_table(self):
        # Create Database
        conn = sqlite3.connect('password_manager.db')

        # Create Cursor
        c = conn.cursor()

        # Create Table
        c.execute("""CREATE TABLE if not exists password(
            website TEXT,
            username TEXT,
            password TEXT
        )
        """)

        conn.commit()
        conn.close()

    def save_it(self):
        # Create Database
        conn = sqlite3.connect('password_manager.db')

        # Create Cursor
        c = conn.cursor()

        try:
            address = self.siteLineEdit.text()
            username = self.usernameLineEdit.text()
            password = self.passwordLineEdit.text()

            if (address and username and password) == "" or (address or username or password) == "":
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(
                    "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg = QMessageBox()
                msg.setWindowIcon(icon)
                msg.setWindowTitle("Error")
                msg.setText("Please Provide all Input Values")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

            else:
                c.execute(
                    'INSERT INTO password VALUES (:website, :username, :password)',
                    {
                        'website': address,
                        'username': username,
                        'password': password
                    }
                )

                self.siteLineEdit.setText('')
                self.usernameLineEdit.setText('')
                self.passwordLineEdit.setText('')

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(
                    "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg = QMessageBox()
                msg.setWindowIcon(icon)
                msg = QMessageBox()
                msg.setWindowTitle("Saved To Database")
                msg.setText("Your Password has been Saved!")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()

            conn.commit()
            conn.close()

        except SyntaxError:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(
                "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg = QMessageBox()
            msg.setWindowIcon(icon)
            msg.setWindowTitle("Invalid Request")
            msg.setText("An Error Occured")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def random(self):
        password = 'ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$^&*?1234567890'
        length = self.passwordLength_spinBox.value()
        a = ''.join(random.sample(password, length))
        self.passwordOutput_lineEdit.setText(str(a))

    def generate(self):
        # Create Database
        conn = sqlite3.connect('password_manager.db')

        # Create Cursor
        c = conn.cursor()
        try:
            self.random()
            address = self.siteLineEdit_2.text()
            username = self.usernameLineEdit_2.text()
            password = self.passwordOutput_lineEdit.text()

            if (address and username) == "" or (address or username) == "":
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(
                    "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg = QMessageBox()
                msg.setWindowIcon(icon)
                msg.setWindowTitle("Error")
                msg.setText("Please Provide all Input Values")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

            else:
                c.execute(
                    'INSERT INTO password VALUES (:website, :username, :password)',
                    {
                        'website': address,
                        'username': username,
                        'password': password
                    }
                )

                self.siteLineEdit_2.setText('')
                self.usernameLineEdit_2.setText('')

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(
                    "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg = QMessageBox()
                msg.setWindowIcon(icon)
                msg.setWindowTitle("Password Generated")
                msg.setText("Your Password has been Generated and Saved!")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()

            conn.commit()
            conn.close()

        except SyntaxError:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(
                "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg = QMessageBox()
            msg.setWindowIcon(icon)
            msg.setWindowTitle("Invalid Request")
            msg.setText("An Error Occured")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def copy(self):
        # Get Clipboard
        cb = QtWidgets.QApplication.clipboard()

        # Clear clipboard
        cb.clear(mode=cb.Clipboard)

        # Set the clipboard text value to the output text
        cb.setText(self.passwordOutput_lineEdit.text(), mode=cb.Clipboard)

        # Set the value of the output to blank
        self.passwordOutput_lineEdit.setText('')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Copied")
        msg.setText("Your Password has been Successfully Copied to Clipboard")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.siteLabel.setText(_translate("MainWindow", "Website Address"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.viewPassword_pushBtn.setText(
            _translate("MainWindow", "View Passwords"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.managerTab), _translate("MainWindow", "Save Password"))
        self.siteLabel_2.setText(_translate("MainWindow", "Website Address"))
        self.usernameLabel_2.setText(_translate("MainWindow", "Username"))
        self.passwordLengthLabel.setText(
            _translate("MainWindow", "Password Length"))
        self.generateBtn.setText(_translate(
            "MainWindow", "Generate Password and Save"))
        self.copyBtn.setText(_translate("MainWindow", "Copy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.genTab), _translate("MainWindow", "Password Generator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
