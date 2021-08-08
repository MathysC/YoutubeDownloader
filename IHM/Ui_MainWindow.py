# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YoutubeDownloaderMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(720, 190)
		MainWindow.setMinimumSize(QtCore.QSize(720, 190))
		MainWindow.setMaximumSize(QtCore.QSize(720, 190))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.singleBox = QtWidgets.QGroupBox(self.centralwidget)
		self.singleBox.setGeometry(QtCore.QRect(11, 11, 701, 144))
		self.singleBox.setObjectName("singleBox")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.singleBox)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.formLayout = QtWidgets.QFormLayout()
		self.formLayout.setObjectName("formLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.layout_link = QtWidgets.QHBoxLayout()
		self.layout_link.setObjectName("layout_link")
		self.l_link = QtWidgets.QLabel(self.singleBox)
		self.l_link.setObjectName("l_link")
		self.layout_link.addWidget(self.l_link)
		self.le_link = QtWidgets.QLineEdit(self.singleBox)
		self.le_link.setMinimumSize(QtCore.QSize(581, 24))
		self.le_link.setMaximumSize(QtCore.QSize(581, 24))
		self.le_link.setObjectName("le_link")
		self.layout_link.addWidget(self.le_link)
		self.verticalLayout.addLayout(self.layout_link)
		self.layout_folder = QtWidgets.QHBoxLayout()
		self.layout_folder.setObjectName("layout_folder")
		self.l_folderBasic = QtWidgets.QLabel(self.singleBox)
		self.l_folderBasic.setObjectName("l_folderBasic")
		self.layout_folder.addWidget(self.l_folderBasic)
		self.pb_chooseFolder = QtWidgets.QPushButton(self.singleBox)
		self.pb_chooseFolder.setObjectName("pb_chooseFolder")
		self.layout_folder.addWidget(self.pb_chooseFolder)
		self.l_currentFolder = QtWidgets.QLabel(self.singleBox)
		self.l_currentFolder.setMinimumSize(QtCore.QSize(401, 16))
		self.l_currentFolder.setMaximumSize(QtCore.QSize(401, 16))
		self.l_currentFolder.setObjectName("l_currentFolder")
		self.layout_folder.addWidget(self.l_currentFolder)
		self.verticalLayout.addLayout(self.layout_folder)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
		self.layout_buttons = QtWidgets.QHBoxLayout()
		self.layout_buttons.setObjectName("layout_buttons")
		self.pb_mp3 = QtWidgets.QPushButton(self.singleBox)
		self.pb_mp3.setObjectName("pb_mp3")
		self.layout_buttons.addWidget(self.pb_mp3)
		self.pb_mp4 = QtWidgets.QPushButton(self.singleBox)
		self.pb_mp4.setObjectName("pb_mp4")
		self.layout_buttons.addWidget(self.pb_mp4)
		self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.layout_buttons)
		self.horizontalLayout_4.addLayout(self.formLayout)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.singleBox.setTitle(_translate("MainWindow", "Téléchargement unique"))
		self.l_link.setText(_translate("MainWindow", "Lien Youtube :"))
		self.le_link.setText(_translate("MainWindow", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"))
		self.l_folderBasic.setText(_translate("MainWindow", "Dossier enregistrement :"))
		self.pb_chooseFolder.setText(_translate("MainWindow", "Choisir un dossier"))
		self.l_currentFolder.setText(_translate("MainWindow", "Aucun dossier défini"))
		self.pb_mp3.setText(_translate("MainWindow", "MP3"))
		self.pb_mp4.setText(_translate("MainWindow", "MP4"))


	def start(self):
		"""
		Function that start the project in the main
		"""
		import sys
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		ui = Ui_MainWindow()
		ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(app.exec_())