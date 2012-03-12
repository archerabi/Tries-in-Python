from PyQt4.QtCore import *
from PyQt4.QtGui import *
from view import *
import sys


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	f = TrieDemoView()
	f.show()
	app.exec_()
