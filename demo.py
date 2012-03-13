from PyQt4.QtCore import *
from PyQt4.QtGui import *
from TrieController import *
import sys


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	controller = TrieController()
	controller.getView().show()
	app.exec_()
