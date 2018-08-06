from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMdiArea
from PyQt5.QtWidgets import QMdiSubWindow
from PyQt5.QtWidgets import QProxyStyle
from PyQt5.QtWidgets import QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


import sys
from random import randint

from Browser_Tabbed import browser_tabbed
from Calculator import calculator
from Notepad import notepad
from Paint import paint
from Solitaire import solitaire


class MDIArea(QMdiArea):
    def __init__(self, background_pixmap, parent = None):
        QMdiArea.__init__(self, parent)
        self.background_pixmap = background_pixmap
        self.centered = False
        self.display_pixmap = None

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self.viewport())
        if not self.centered:
            painter.drawPixmap(0, 0, self.width(), self.height(), self.background_pixmap)
        else:
            painter.fillRect(event.rect(), self.palette().color(QPalette.Window))
            x = (self.width() - self.display_pixmap.width())/2
            y = (self.height() - self.display_pixmap.height())/2
            painter.drawPixmap(x, y, self.display_pixmap)
        painter.end()

    def resizeEvent(self, event):
        global ex
        self.display_pixmap = self.background_pixmap.scaled(ex.window_width(), ex.window_height(), Qt.KeepAspectRatio)


class MyProxyStyle(QProxyStyle):
    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):
        if QStyle_PixelMetric == QStyle.PM_SmallIconSize:
            return 40
        else:
            return QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)


class Desktop(QMainWindow):
    def check_position(self, y, width, height, sub_window):
        if y <= 40:
            sub_window.move(randint(0, self.width - width), randint(0, self.height - height))
            print("Sub Window Moved")

    @staticmethod
    def close_desktop():
        print("Closing Remote Desktop")
        exit(0)

    def open_browser(self):
        print("Opening Browser")
        sub = QMdiSubWindow()
        sub.setWidget(browser_tabbed.MainWindow())
        sub.setWindowTitle("Browser")
        self.mdi.addSubWindow(sub)
        widget_position = sub.pos()
        widget_dimensions = sub.frameGeometry()
        self.check_position(y=widget_position.y(), width=widget_dimensions.width(), height=widget_dimensions.height(), sub_window=sub)
        sub.show()

    def open_calculator(self):
        print("Opening Calculator")
        sub = QMdiSubWindow()
        sub.setWidget(calculator.MainWindow())
        sub.setWindowTitle("Calculator")
        self.mdi.addSubWindow(sub)
        widget_position = sub.pos()
        widget_dimensions = sub.frameGeometry()
        self.check_position(y=widget_position.y(), width=widget_dimensions.width(), height=widget_dimensions.height(), sub_window=sub)
        sub.show()

    def open_notepad(self):
        print("Opening Notepad")
        sub = QMdiSubWindow()
        sub.setWidget(notepad.MainWindow())
        sub.setWindowTitle("Notepad")
        self.mdi.addSubWindow(sub)
        widget_position = sub.pos()
        widget_dimensions = sub.frameGeometry()
        self.check_position(y=widget_position.y(), width=widget_dimensions.width(), height=widget_dimensions.height(), sub_window=sub)
        sub.show()

    def open_paint(self):
        print("Opening Paint")
        sub = QMdiSubWindow()
        sub.setWidget(paint.MainWindow())
        sub.setWindowTitle("Paint")
        self.mdi.addSubWindow(sub)
        widget_position = sub.pos()
        widget_dimensions = sub.frameGeometry()
        self.check_position(y=widget_position.y(), width=widget_dimensions.width(), height=widget_dimensions.height(), sub_window=sub)
        sub.show()

    def open_solitaire(self):
        print("Opening Solitaire")
        sub = QMdiSubWindow()
        sub.setWidget(solitaire.MainWindow())
        sub.setWindowTitle("Solitaire")
        self.mdi.addSubWindow(sub)
        widget_position = sub.pos()
        widget_dimensions = sub.frameGeometry()
        self.check_position(y=widget_position.y(), width=widget_dimensions.width(), height=widget_dimensions.height(), sub_window=sub)
        sub.show()

    def __init__(self):
        super(QMainWindow, self).__init__()
        # Uncomment to Ask User Their Screen Resolution

        # self.width = int(input("Please input your computer screen's width (in pixels): "))
        # self.height = int(input("Please input your computer screen's height (in pixels): "))
        self.width = 1920
        self.height = 1080

        self.title = "Remote Desktop"
        self.left = 10
        self.top = 10
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def create_menu(self):
        menu = QMenuBar(self)
        menu.setNativeMenuBar(False)

        exitButton = QAction(QIcon("Power.jpeg"), "Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip("Power Off")

        browser = QAction(QIcon("browser.jpeg"), "Boron", self)
        browser.setShortcut("Ctrl+B")
        browser.setStatusTip("Open Browser")

        calculator = QAction(QIcon("Calculator.jpeg"), "Cobalt", self)
        calculator.setShortcut("Ctrl+C")
        calculator.setStatusTip("Open Calculator")

        notepad = QAction(QIcon("Notepad.png"), "Neon", self)
        notepad.setShortcut("Ctrl+N")
        notepad.setStatusTip("Open Notepad")

        paint = QAction(QIcon("Paint.png"), "Paint", self)
        paint.setShortcut("Ctrl+P")
        paint.setStatusTip("Open Paint")

        solitaire = QAction(QIcon("Solitaire.jpeg"), "Xenon", self)
        solitaire.setShortcut("Ctrl+S")
        solitaire.setStatusTip("Open Solitaire")

        menu.addAction(exitButton)
        menu.addAction(browser)
        menu.addAction(calculator)
        menu.addAction(notepad)
        menu.addAction(paint)
        menu.addAction(solitaire)

        exitButton.triggered.connect(self.close_desktop)
        browser.triggered.connect(self.open_browser)
        calculator.triggered.connect(self.open_calculator)
        notepad.triggered.connect(self.open_notepad)
        paint.triggered.connect(self.open_paint)
        solitaire.triggered.connect(self.open_solitaire)

    def window_width(self):
        return self.width

    def window_height(self):
        return self.height

    def create_mdi(self):
        self.pixmap = QPixmap()
        self.pixmap.load("mt-mckinley.jpg")
        self.mdi = MDIArea(self.pixmap)
        self.setCentralWidget(self.mdi)
        self.mdi.cascadeSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Desktop()
    ex.create_mdi()
    ex.create_menu()
    my_style = MyProxyStyle("Fusion")
    app.setStyle(my_style)
    app.exec_()
