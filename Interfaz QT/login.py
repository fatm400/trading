# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaLogin(object):
    def setupUi(self, VentanaLogin):
        VentanaLogin.setObjectName("VentanaLogin")
        VentanaLogin.resize(800, 600)
        VentanaLogin.setStyleSheet("/*Cambiamos el color de la ventana*/\n"
"    #VentanaLogin{\n"
"        background-color: #009688;\n"
"    }\n"
"\n"
"    /*Estilos para el botón*/\n"
"    QPushButton{\n"
"        background-color: #ff5722;\n"
"        border-radius: 4px;\n"
"        color: #fff;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"    \n"
"    /*Definimos el estilo para un efecto hover sobre el botón,\n"
"    este cambiará su background cuando pasemos el mouse por\n"
"    encima*/\n"
"    QPushButton:hover{\n"
"    background-color: #ff7043;\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLineEdit*/\n"
"    QLineEdit{\n"
"        border-radius: 3px;\n"
"        border: 2px solid #00796b;\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLabel*/\n"
"    QLabel{\n"
"        font-family: \'Roboto\';\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLabels cuyos nombres son\n"
"    \'label_usuario\' y \'label-password\'*/\n"
"    #label_usuario, #label_password{\n"
"        font-size: 17px;\n"
"        color: #212121;\n"
"    }\n"
"    \n"
"    /*Estilo para el QLable cuyo nombre es #label_login*/\n"
"    #label_login{\n"
"        font-size:30px;\n"
"        color: #fff;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(VentanaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.button_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.button_iniciar.setGeometry(QtCore.QRect(70, 260, 101, 23))
        self.button_iniciar.setObjectName("button_iniciar")
        self.line_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.line_usuario.setGeometry(QtCore.QRect(70, 150, 113, 23))
        self.line_usuario.setObjectName("line_usuario")
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_password.setGeometry(QtCore.QRect(70, 200, 113, 23))
        self.line_password.setObjectName("line_password")
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setGeometry(QtCore.QRect(70, 130, 71, 16))
        self.label_usuario.setObjectName("label_usuario")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(70, 180, 81, 16))
        self.label_password.setObjectName("label_password")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(70, 70, 81, 31))
        self.label_login.setObjectName("label_login")
        VentanaLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        VentanaLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaLogin)
        self.statusbar.setObjectName("statusbar")
        VentanaLogin.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaLogin)
        QtCore.QMetaObject.connectSlotsByName(VentanaLogin)

    def retranslateUi(self, VentanaLogin):
        _translate = QtCore.QCoreApplication.translate
        VentanaLogin.setWindowTitle(_translate("VentanaLogin", "MainWindow"))
        self.button_iniciar.setText(_translate("VentanaLogin", "PushButton"))
        self.label_usuario.setText(_translate("VentanaLogin", "Usuario"))
        self.label_password.setText(_translate("VentanaLogin", "Password"))
        self.label_login.setText(_translate("VentanaLogin", "Login"))

