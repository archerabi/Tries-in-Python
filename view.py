from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt,pyqtSignal
import sys

class TrieDemoView(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self,None)
		#self.setObjectName("TrieDemoView")
		self.resize(800,600)
		self.vLayout = QtGui.QVBoxLayout(self)
		self.tabWidget = QtGui.QTabWidget(self)

		#create the autocomplete tab
		self.autoCompleteTab = QtGui.QWidget()
		self.autoCompleteTabLayout = QtGui.QVBoxLayout()
		self.autoCompleteTab.setLayout(self.autoCompleteTabLayout)
		self.lineEdit = QtGui.QLineEdit(self)
		self.autoCompleteTabLayout.addWidget(self.lineEdit,0,Qt.AlignTop)
		self.tabWidget.addTab(self.autoCompleteTab,"Auto Complete")
		
		#create trie tab
		self.trieTab = QtGui.QWidget()
		self.trieTabLayout = QtGui.QVBoxLayout()
		self.trieTab.setLayout(self.trieTabLayout)
		self.tabWidget.addTab(self.trieTab,"Trie")

		self.vLayout.addWidget(self.tabWidget)

		self.lineEdit.textChanged.connect(self.handleTextChanged)

	def handleTextChanged(self,text):
		self.textEntered.emit(self.lineEdit.text())

	textEntered = pyqtSignal('QString')
