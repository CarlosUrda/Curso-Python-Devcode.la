# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3enraya.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import re

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wPrincipal(QtGui.QWidget):
    def setupUi(self, wPrincipal):
        wPrincipal.setObjectName(_fromUtf8("wPrincipal"))
        wPrincipal.setWindowModality(QtCore.Qt.NonModal)
        wPrincipal.setEnabled(True)
        wPrincipal.resize(680, 418)
        wPrincipal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        wPrincipal.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lPuntuacion = QtGui.QLabel(wPrincipal)
        self.lPuntuacion.setGeometry(QtCore.QRect(430, 20, 175, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lPuntuacion.setFont(font)
        self.lPuntuacion.setObjectName(_fromUtf8("lPuntuacion"))
        self.bReiniciar = QtGui.QPushButton(wPrincipal)
        self.bReiniciar.setGeometry(QtCore.QRect(460, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bReiniciar.setFont(font)
        self.bReiniciar.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.bReiniciar.setObjectName(_fromUtf8("bReiniciar"))
        self.layoutWidget = QtGui.QWidget(wPrincipal)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 301))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.glTablero = QtGui.QGridLayout(self.layoutWidget)
        self.glTablero.setObjectName(_fromUtf8("glTablero"))
        self.b1_2 = QtGui.QPushButton(self.layoutWidget)
        self.b1_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1_2.sizePolicy().hasHeightForWidth())
        self.b1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b1_2.setFont(font)
        self.b1_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1_2.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b1_2.setText(_fromUtf8(""))
        self.b1_2.setObjectName(_fromUtf8("b1_2"))
        self.glTablero.addWidget(self.b1_2, 1, 2, 1, 1)
        self.b2_2 = QtGui.QPushButton(self.layoutWidget)
        self.b2_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2_2.sizePolicy().hasHeightForWidth())
        self.b2_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b2_2.setFont(font)
        self.b2_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2_2.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b2_2.setText(_fromUtf8(""))
        self.b2_2.setObjectName(_fromUtf8("b2_2"))
        self.glTablero.addWidget(self.b2_2, 2, 2, 1, 1)
        self.b1_0 = QtGui.QPushButton(self.layoutWidget)
        self.b1_0.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1_0.sizePolicy().hasHeightForWidth())
        self.b1_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b1_0.setFont(font)
        self.b1_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1_0.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b1_0.setText(_fromUtf8(""))
        self.b1_0.setObjectName(_fromUtf8("b1_0"))
        self.glTablero.addWidget(self.b1_0, 1, 0, 1, 1)
        self.b0_2 = QtGui.QPushButton(self.layoutWidget)
        self.b0_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b0_2.sizePolicy().hasHeightForWidth())
        self.b0_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b0_2.setFont(font)
        self.b0_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b0_2.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b0_2.setText(_fromUtf8(""))
        self.b0_2.setObjectName(_fromUtf8("b0_2"))
        self.glTablero.addWidget(self.b0_2, 0, 2, 1, 1)
        self.b2_1 = QtGui.QPushButton(self.layoutWidget)
        self.b2_1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2_1.sizePolicy().hasHeightForWidth())
        self.b2_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b2_1.setFont(font)
        self.b2_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2_1.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b2_1.setText(_fromUtf8(""))
        self.b2_1.setObjectName(_fromUtf8("b2_1"))
        self.glTablero.addWidget(self.b2_1, 2, 1, 1, 1)
        self.b0_0 = QtGui.QPushButton(self.layoutWidget)
        self.b0_0.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b0_0.sizePolicy().hasHeightForWidth())
        self.b0_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b0_0.setFont(font)
        self.b0_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b0_0.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b0_0.setText(_fromUtf8(""))
        self.b0_0.setObjectName(_fromUtf8("b0_0"))
        self.glTablero.addWidget(self.b0_0, 0, 0, 1, 1)
        self.b2_0 = QtGui.QPushButton(self.layoutWidget)
        self.b2_0.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2_0.sizePolicy().hasHeightForWidth())
        self.b2_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b2_0.setFont(font)
        self.b2_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2_0.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b2_0.setText(_fromUtf8(""))
        self.b2_0.setObjectName(_fromUtf8("b2_0"))
        self.glTablero.addWidget(self.b2_0, 2, 0, 1, 1)
        self.b0_1 = QtGui.QPushButton(self.layoutWidget)
        self.b0_1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b0_1.sizePolicy().hasHeightForWidth())
        self.b0_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b0_1.setFont(font)
        self.b0_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b0_1.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b0_1.setText(_fromUtf8(""))
        self.b0_1.setObjectName(_fromUtf8("b0_1"))
        self.glTablero.addWidget(self.b0_1, 0, 1, 1, 1)
        self.b1_1 = QtGui.QPushButton(self.layoutWidget)
        self.b1_1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1_1.sizePolicy().hasHeightForWidth())
        self.b1_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b1_1.setFont(font)
        self.b1_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1_1.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(8, 50, 255);\n"
"\n"
""))
        self.b1_1.setText(_fromUtf8(""))
        self.b1_1.setObjectName(_fromUtf8("b1_1"))
        self.glTablero.addWidget(self.b1_1, 1, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(wPrincipal)
        self.layoutWidget1.setGeometry(QtCore.QRect(57, 363, 241, 41))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.lEleccionMaquina = QtGui.QHBoxLayout(self.layoutWidget1)
        self.lEleccionMaquina.setObjectName(_fromUtf8("lEleccionMaquina"))
        self.cbMaquina2 = QtGui.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbMaquina2.setFont(font)
        self.cbMaquina2.setObjectName(_fromUtf8("cbMaquina2"))
        self.lEleccionMaquina.addWidget(self.cbMaquina2)
        self.cbMaquina1 = QtGui.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbMaquina1.setFont(font)
        self.cbMaquina1.setTristate(False)
        self.cbMaquina1.setObjectName(_fromUtf8("cbMaquina1"))
        self.lEleccionMaquina.addWidget(self.cbMaquina1)
        self.eTurno = QtGui.QLabel(wPrincipal)
        self.eTurno.setGeometry(QtCore.QRect(85, 330, 48, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eTurno.setFont(font)
        self.eTurno.setObjectName(_fromUtf8("eTurno"))
        self.layoutWidget2 = QtGui.QWidget(wPrincipal)
        self.layoutWidget2.setGeometry(QtCore.QRect(391, 90, 271, 171))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.glPuntuacion = QtGui.QGridLayout(self.layoutWidget2)
        self.glPuntuacion.setObjectName(_fromUtf8("glPuntuacion"))
        self.eJugador1 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eJugador1.setFont(font)
        self.eJugador1.setObjectName(_fromUtf8("eJugador1"))
        self.glPuntuacion.addWidget(self.eJugador1, 0, 0, 1, 1)
        self.lcdJugador1 = QtGui.QLCDNumber(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdJugador1.setFont(font)
        self.lcdJugador1.setProperty("value", 0.0)
        self.lcdJugador1.setObjectName(_fromUtf8("lcdJugador1"))
        self.glPuntuacion.addWidget(self.lcdJugador1, 0, 1, 1, 1)
        self.eJugador2 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eJugador2.setFont(font)
        self.eJugador2.setObjectName(_fromUtf8("eJugador2"))
        self.glPuntuacion.addWidget(self.eJugador2, 1, 0, 1, 1)
        self.lcdJugador2 = QtGui.QLCDNumber(self.layoutWidget2)
        self.lcdJugador2.setObjectName(_fromUtf8("lcdJugador2"))
        self.glPuntuacion.addWidget(self.lcdJugador2, 1, 1, 1, 1)
        self.eEmpate = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eEmpate.setFont(font)
        self.eEmpate.setObjectName(_fromUtf8("eEmpate"))
        self.glPuntuacion.addWidget(self.eEmpate, 2, 0, 1, 1)
        self.lcdEmpate = QtGui.QLCDNumber(self.layoutWidget2)
        self.lcdEmpate.setObjectName(_fromUtf8("lcdEmpate"))
        self.glPuntuacion.addWidget(self.lcdEmpate, 2, 1, 1, 1)
        self.leTurno = QtGui.QLineEdit(wPrincipal)
        self.leTurno.setGeometry(QtCore.QRect(150, 330, 113, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.leTurno.setFont(font)
        self.leTurno.setText(_fromUtf8(""))
        self.leTurno.setObjectName(_fromUtf8("leTurno"))
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.lPuntuacion.raise_()
        self.bReiniciar.raise_()
        self.eTurno.raise_()
        self.leTurno.raise_()

        self.retranslateUi(wPrincipal)
        QtCore.QMetaObject.connectSlotsByName(wPrincipal)

        self.__botonesTablero = [self.b0_0, self.b0_1, self.b0_2, 
                                 self.b1_0, self.b1_1, self.b1_2,
                                 self.b2_0, self.b2_1, self.b2_2]

        self.__victorias1 = 0
        self.__victorias2 = 0
        self.__empates = 0
        for boton in self.__botonesTablero:
            QtCore.QObject.connect( boton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                                    self.pincharBotonTablero)
        QtCore.QObject.connect( self.bReiniciar, QtCore.SIGNAL(_fromUtf8("clicked()")),
                                self.pincharBotonReiniciar)
        self.iniciarPartida()


    def pincharBotonTablero( self):
        posicion = re.search( "b(\d+)_(\d+)", self.sender().objectName())
        fila = int( posicion.group(1))
        columna = int( posicion.group(2))
        self.cambiarCasilla( fila, columna)
        
    def cambiarCasilla( self, fila, columna):
        if self.__movimiento == 9: return False

       if self.__tablero[fila][columna] != 0: return False

        boton.setText( "X" if self.__turno == 1 else "O")
        boton.setEnabled( False)
        self.__tablero[fila][columna] = self.__turno
        self.__movimiento += 1

        ganador = self.comprobarFinal( fila, columna)
        if ganador == 3:
            self.__turno = 1 if self.__turno == 2 else 2
            self.leTurno.setText( "Jugador 1" if self.__turno == 1 else "Jugador 2")
            return True
        elif ganador == 1:
            self.__victorias1 += 1
            self.lcdJugador1.display( self.__victorias1)
            # Poner un mensaje del resultado
        elif ganador == 2:
            self.__victorias2 += 1
            self.lcdJugador2.display( self.__victorias2)
        elif ganador == 0:
            self.__empates += 1
            self.lcdEmpate.display( self.__empates)
        
        self.finalizarPartida()
        return True             

    def finalizarPartida( self):
        for boton in self.__botonesTablero:
            if boton.isEnabled(): boton.setEnabled( False)
        self.__movimiento = 9
        self.leTurno.setText( "")

    def pincharBotonReiniciar( self):
        self.iniciarPartida()

    def iniciarPartida( self):
        self.__turno = 1
        for boton in self.__botonesTablero:
            boton.setText( " ")
            boton.setEnabled( True)
        self.__tablero = [[0]*3,[0]*3,[0]*3]
        self.__movimiento = 0
        self.leTurno.setText( "Jugador 1" if self.__turno == 1 else "Jugador 2")

        while movimiento < 9:
            if self.cbMaquina1.isChecked():
                (fila, columna) = self.generarMovimiento()
                self.cambiarCasilla( 




    def comprobarFinal( self, fil, col):
        if (self.__tablero[fil][col] == self.__tablero[(fil+1)%3][col] and 
            self.__tablero[fil][col] == self.__tablero[(fil+2)%3][col] or 
            self.__tablero[fil][col] == self.__tablero[fil][(col+1)%3] and 
            self.__tablero[fil][col] == self.__tablero[fil][(col+2)%3] or 
            fil == col and 
            self.__tablero[fil][col] == self.__tablero[(fil+1)%3][(col+1)%3] and
            self.__tablero[fil][col] == self.__tablero[(fil+2)%3][(col+2)%3] or 
            abs(fil-col) == 2 and 
            self.__tablero[fil][col] == self.__tablero[(fil+1)%3][(col-1)%3] and
            self.__tablero[fil][col] == self.__tablero[(fil+2)%3][(col-2)%3]):
            return self.__turno

        if self.__movimiento == 9: return 0
        return 3

    def retranslateUi(self, wPrincipal):
        wPrincipal.setWindowTitle(_translate("wPrincipal", "3 en Raya", None))
        self.lPuntuacion.setText(_translate("wPrincipal", "PUNTUACIÓN", None))
        self.bReiniciar.setText(_translate("wPrincipal", "Reiniciar", None))
        self.cbMaquina2.setText(_translate("wPrincipal", "J2 Máquina", None))
        self.cbMaquina1.setText(_translate("wPrincipal", "J1 Máquina", None))
        self.eTurno.setText(_translate("wPrincipal", "Turno", None))
        self.eJugador1.setText(_translate("wPrincipal", "Jugador 1", None))
        self.eJugador2.setText(_translate("wPrincipal", "Jugador 2", None))
        self.eEmpate.setText(_translate("wPrincipal", "Empate", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    wPrincipal = QtGui.QWidget()
    ui = Ui_wPrincipal()
    ui.setupUi(wPrincipal)
    wPrincipal.show()
    sys.exit(app.exec_())

