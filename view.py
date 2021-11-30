from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from edit import Ui_EditWindow
import sqlite3


class Ui_ViewWindow(object):
    def setupUi(self, ViewWindow):
        ViewWindow.setObjectName("ViewWindow")
        ViewWindow.resize(940, 690)
        ViewWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        ViewWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ViewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 914, 541))
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setGeometry(QtCore.QRect(810, 610, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.delete_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.edit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.edit_pushButton.setGeometry(QtCore.QRect(680, 610, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.edit_pushButton.setFont(font)
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(400, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        ViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 26))
        self.menubar.setObjectName("menubar")
        ViewWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewWindow)
        self.statusbar.setObjectName("statusbar")
        ViewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewWindow)

    def editWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditWindow()
        self.ui.setupUi(self.window)
        clicked = self.tableWidget.currentRow()
        conn = sqlite3.connect('password_manager.db')
        c = conn.cursor()
        c.execute('SELECT * from password WHERE rowid =' + str(clicked+1))
        record = c.fetchall()
        for i in record:
            self.ui.siteLineEdit.setText(i[0])
            self.ui.usernameLineEdit.setText(i[1])
            self.ui.passwordLineEdit.setText(i[2])

        conn.commit()
        conn.close()

        self.ui.saveBtn.clicked.connect(self.save_edit)
        self.window.show()

    def save_edit(self):
        conn = sqlite3.connect('password_manager.db')
        c = conn.cursor()
        clicked = self.tableWidget.currentRow()
        c.execute("""UPDATE password SET
                website = :site,
                username = :user,
                password = :password

                WHERE rowid = :oid
            """,
                  {
                      'site': self.ui.siteLineEdit.text(),
                      'user': self.ui.usernameLineEdit.text(),
                      'password': self.ui.passwordLineEdit.text(),
                      'oid': (clicked+1)
                  }
                  )
        conn.commit()
        conn.close()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg = QMessageBox()
        msg.setWindowTitle("Sucess")
        msg.setText("Sucessfully Updates!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        self.window.close()

    def retranslateUi(self, ViewWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewWindow.setWindowTitle(_translate("ViewWindow", "View Passwords"))
        self.tableWidget.setSortingEnabled(False)
        self.delete_pushButton.setText(_translate("ViewWindow", "Delete"))
        self.edit_pushButton.setText(_translate("ViewWindow", "Edit"))
        self.infoLabel.setText(_translate("ViewWindow", "Saved Passwords"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewWindow()
    ui.setupUi(ViewWindow)
    ViewWindow.show()
    sys.exit(app.exec_())
