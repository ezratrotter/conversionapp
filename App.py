from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit
from os import path

from converter import converter
from updater import updater



class Ui_MainWindow(object):
    
    
    def setupUi(self, MainWindow):
        
        xoff = 10
        yoff = 5
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 180)
        MainWindow.setFixedSize(474, 180)
        
        self.error_dialog = QtWidgets.QErrorMessage()
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(180+xoff, 120+yoff, 91, 31))
        self.run_button.setObjectName("run_button")
        self.run_button.clicked.connect(self.run_handler)
        
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(25+xoff, 20+yoff, 91, 16))
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5+xoff, 50+yoff, 91, 16))
        self.label.setObjectName("label")
        self.in_epsg = QtWidgets.QLineEdit(self.centralwidget)
        self.in_epsg.setGeometry(QtCore.QRect(105+xoff, 20+yoff, 91, 20))
        self.in_epsg.setText("")
        self.in_epsg.setObjectName("in_epsg")
        self.in_epsg.textChanged.connect(self.on_change1)
        self.out_epsg = QtWidgets.QLineEdit(self.centralwidget)
        self.out_epsg.setGeometry(QtCore.QRect(105+xoff, 50+yoff, 91, 20))
        self.out_epsg.setObjectName("out_epsg")
        self.out_epsg.textChanged.connect(self.on_change2)
        self.in_epsg_label = QtWidgets.QLabel(self.centralwidget)
        self.in_epsg_label.setGeometry(QtCore.QRect(225+xoff, 20+yoff, 81, 16))
        self.in_epsg_label.setObjectName("in_epsg_label")
#         self.in_epsg_label.adjustSize()
        self.out_epsg_label = QtWidgets.QLabel(self.centralwidget)
        self.out_epsg_label.setGeometry(QtCore.QRect(225+xoff, 50+yoff, 81, 16))
        self.out_epsg_label.setObjectName("out_epsg_label")
#         self.out_epsg_label.adjustSize()
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(45+xoff, 80+yoff, 91, 16))
        self.label_4.setObjectName("label_4")
        self.filePath = QtWidgets.QLineEdit(self.centralwidget)
        self.filePath.setGeometry(QtCore.QRect(105+xoff, 80+yoff, 271, 20))
        self.filePath.setObjectName("filePath")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(385+xoff, 79+yoff, 60, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fileButton_handler)
        
        MainWindow.setCentralWidget(self.centralwidget)
        ### Menu Bar
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 20))
#         self.menubar.setObjectName("menubar")
#         self.menuFile = QtWidgets.QMenu(self.menubar)
#         self.menuFile.setObjectName("menuFile")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.actionquit = QtWidgets.QAction(MainWindow)
#         self.actionquit.setObjectName("actionquit")
#         self.menuFile.addAction(self.actionquit)
#         self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
        
    def error_handler(self, epsgIn, epsgInLabel, epsgOut, epsgOutLabel, filePath):
        
        errors = [
            {"check": epsgInLabel=="invalid EPSG code", "msg": 'Invalid Input EPSG code'},
            {"check": epsgOutLabel=="invalid EPSG code", "msg": 'Invalid Destination EPSG code'},
            {"check": epsgInLabel=="...", "msg": 'Enter an Input EPSG code'},
            {"check": epsgOutLabel=="...", "msg": 'Enter an Output EPSG code'},
            {"check": path.exists(filePath) == False, "msg": 'Path Invalid'},
            {"check": path.isfile(filePath) == False, "msg": 'No File Found'}
        ]
        
        passTests = True
    
#         [ self.error_dialog.showMessage(e["msg"]) if e["check"] else print("pass") for e in errors ]
        
        for e in errors:
            if e["check"]:
                self.error_dialog.showMessage(e["msg"])
                passTests = False
        return passTests
        
    def run_handler(self):
      
        epsgIn = self.in_epsg.text()
        
        epsgInLabel = self.in_epsg_label.text()
        
        epsgOut = self.out_epsg.text()
        epsgOutLabel = self.out_epsg_label.text()
        
        filePath = self.filePath.text()
        
        if self.error_handler(epsgIn, epsgInLabel, epsgOut, epsgOutLabel, filePath):
            try:
                converter(epsgIn, epsgOut, filePath)
                self.error_dialog.showMessage("conversion from {} to {} successful".format(epsgIn, epsgOut))
            except:
                self.error_dialog.showMessage("ERROR: Conversion Unsuccessful")
                               

    def on_click(self):
        #run conversion on SELECTED EPSG's
        epsgIn = self.in_epsg.text()
        epsgOut = self.out_epsg.text()

        converter(epsgIn, epsgOut)
    ###for epsg_in_label   
    def on_change1(self):
        text = self.in_epsg.text()
        try:
            self.in_epsg_label.setText(updater(text))
        except:
            self.in_epsg_label.setText("invalid EPSG code")
        self.in_epsg_label.adjustSize()
    ###for epsg_out_label         
    def on_change2(self):
        text = self.out_epsg.text()
        try:
            self.out_epsg_label.setText(updater(text))
        except:
            self.out_epsg_label.setText("invalid EPSG code")
        self.out_epsg_label.adjustSize()
        
    def fileButton_handler(self):
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        path = filename[0]
        self.update_path(path)
    
    def update_path(self, path):
        self.filePath.setText(path)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NIRAS DB Coordinate Converter"))
        self.run_button.setStatusTip(_translate("MainWindow", "Run Transformation"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.label1.setText(_translate("MainWindow", "Current EPSG:"))
        self.label.setText(_translate("MainWindow", "Destination EPSG:"))
        self.in_epsg.setStatusTip(_translate("MainWindow", "input EPSG code"))
        self.in_epsg.setPlaceholderText(_translate("MainWindow", "EPSG #"))
        self.out_epsg.setStatusTip(_translate("MainWindow", "output EPSG code"))
        self.out_epsg.setPlaceholderText(_translate("MainWindow", "EPSG #"))
        self.in_epsg_label.setText(_translate("MainWindow", "..."))
        self.out_epsg_label.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "File Path:"))
        self.filePath.setStatusTip(_translate("MainWindow", "input file path"))
        self.filePath.setPlaceholderText(_translate("MainWindow", "path/to/database"))
        self.pushButton.setStatusTip(_translate("MainWindow", "browse for input"))
        self.pushButton.setText(_translate("MainWindow", "Open File"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())