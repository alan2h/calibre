#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2013, Kovid Goyal <kovid at kovidgoyal.net>'

import weakref

from PyQt5.Qt import (
    QPushButton, QPixmap, QIcon, QColor, Qt, QColorDialog, pyqtSignal,
    QKeySequence, QToolButton, QDialog, QDialogButtonBox, QComboBox, QFont,
    QAbstractListModel, QModelIndex, QApplication, QStyledItemDelegate,
    QUndoCommand, QUndoStack, QLayout, QRect, QSize, QStyle, QSizePolicy,
    QPoint, QWidget, QLabel, QCheckBox)

from PyQt5 import QtCore, QtGui, QtWidgets


from calibre.ebooks.metadata import rating_to_stars
from calibre.gui2 import gprefs, rating_font
from calibre.gui2.complete2 import LineEdit, EditWithComplete
from calibre.gui2.widgets import history


class MyFirstGuiProgram(Ui_myfirstgui):
    	def __init__(self, dialog):
		Ui_myfirstgui.__init__(self)
		self.setupUi(dialog)

		# Connect "add" button with a custom function (addInputTextToListbox)
		self.addBtn.clicked.connect(self.addInputTextToListbox)

	def addInputTextToListbox(self):
		txt = self.myTextInput.text()
		self.listWidget.addItem(txt)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = MyFirstGuiProgram(dialog)

	dialog.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
    from calibre.gui2 import Application
    app = Application([])
    app.load_builtin_fonts()
    w.show()
    app.exec_()
