from PyQt5 import QtCore, QtGui, QtWidgets

def pageInputDataPenjualan(self) :
    self.pageInputDataPenjualan = dict()
    self.pageInputDataPenjualan["widget"] = QtWidgets.QWidget(self.centralwidget)
    self.pageInputDataPenjualan["widget"].setGeometry(QtCore.QRect(0, 0, 500, 500))
    self.pageInputDataPenjualan["widget"].setMinimumSize(QtCore.QSize(500, 500))
    self.pageInputDataPenjualan["widget"].setMaximumSize(QtCore.QSize(500, 500))

    self.pageInputDataPenjualan["Frame"] = QtWidgets.QLabel(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["Frame"].setGeometry(QtCore.QRect(0, 0, 500, 500))
    self.pageInputDataPenjualan["Frame"].setText("")
    self.pageInputDataPenjualan["Frame"].setPixmap(QtGui.QPixmap("Picture/FrameInputDataPenjualan.jpg"))
    self.pageInputDataPenjualan["Frame"].setScaledContents(True)

    self.pageInputDataPenjualan["inputKode"] = QtWidgets.QLineEdit(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["inputKode"].setGeometry(QtCore.QRect(56, 140, 384, 26))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.pageInputDataPenjualan["inputKode"].setFont(font)
    self.pageInputDataPenjualan["inputKode"].setMaxLength(10)
    self.pageInputDataPenjualan["inputKode"].setFrame(False)
    self.pageInputDataPenjualan["inputKode"].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    self.pageInputDataPenjualan["inputNama"] = QtWidgets.QLineEdit(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["inputNama"].setGeometry(QtCore.QRect(56, 206, 384, 26))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.pageInputDataPenjualan["inputNama"].setFont(font)
    self.pageInputDataPenjualan["inputNama"].setMaxLength(50)
    self.pageInputDataPenjualan["inputNama"].setFrame(False)
    self.pageInputDataPenjualan["inputNama"].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    self.pageInputDataPenjualan["inputJumlah"] = QtWidgets.QLineEdit(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["inputJumlah"].setGeometry(QtCore.QRect(56, 272, 384, 26))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.pageInputDataPenjualan["inputJumlah"].setFont(font)
    self.pageInputDataPenjualan["inputJumlah"].setMaxLength(50)
    self.pageInputDataPenjualan["inputJumlah"].setFrame(False)
    self.pageInputDataPenjualan["inputJumlah"].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    self.pageInputDataPenjualan["inputKeterangan"] = QtWidgets.QLineEdit(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["inputKeterangan"].setGeometry(QtCore.QRect(56, 339, 384, 26))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.pageInputDataPenjualan["inputKeterangan"].setFont(font)
    self.pageInputDataPenjualan["inputKeterangan"].setMaxLength(50)
    self.pageInputDataPenjualan["inputKeterangan"].setFrame(False)
    self.pageInputDataPenjualan["inputKeterangan"].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    self.pageInputDataPenjualan["buttonInput"] = QtWidgets.QToolButton(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["buttonInput"].setGeometry(QtCore.QRect(209, 387, 84, 34))
    self.pageInputDataPenjualan["buttonInput"].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.pageInputDataPenjualan["buttonInput"].setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("Picture/buttonInput.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pageInputDataPenjualan["buttonInput"].setIcon(icon1)
    self.pageInputDataPenjualan["buttonInput"].setIconSize(QtCore.QSize(80, 30))
    self.pageInputDataPenjualan["buttonInput"].setAutoRaise(True)

    self.pageInputDataPenjualan["buttonBack"] = QtWidgets.QToolButton(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["buttonBack"].setGeometry(QtCore.QRect(37, 50, 31, 31))
    self.pageInputDataPenjualan["buttonBack"].setText("")
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("Picture/iconPrevious .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.pageInputDataPenjualan["buttonBack"].setIcon(icon2)
    self.pageInputDataPenjualan["buttonBack"].setIconSize(QtCore.QSize(100, 30))
    self.pageInputDataPenjualan["buttonBack"].setAutoRaise(True)


    self.pageInputDataPenjualan["infoInput"] = QtWidgets.QLabel(self.pageInputDataPenjualan["widget"])
    self.pageInputDataPenjualan["infoInput"].setGeometry(QtCore.QRect(56, 430, 382, 27))
    font = QtGui.QFont()
    font.setPointSize(10)
    self.pageInputDataPenjualan["infoInput"].setFont(font)
    self.pageInputDataPenjualan["infoInput"].setText("")
    self.pageInputDataPenjualan["infoInput"].setAlignment(QtCore.Qt.AlignCenter)
    self.pageInputDataPenjualan["infoInput"].setObjectName("infoInput")