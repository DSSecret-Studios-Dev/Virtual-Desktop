from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import sys
from random import randint

from Browser_Tabbed import browser_tabbed
from Browser_Tabbed import titanium
from Calculator import calculator
from Notepad import notepad
from Paint import paint
from Solitaire import solitaire
import proxy_closest_match


class MDIArea(QMdiArea):
    def __init__(self, *args, **kwargs):
        super(MDIArea, self).__init__(*args, **kwargs)
        self.parent = args[0]
        self.background_pixmap = self.parent.pixmap
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
        self.display_pixmap = self.background_pixmap.scaled(self.parent.window_width(),
                                                            self.parent.window_height(),
                                                            Qt.KeepAspectRatio)


class MyProxyStyle(QProxyStyle):
    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):
        if QStyle_PixelMetric == QStyle.PM_SmallIconSize:
            return 40
        else:
            return QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)


class Desktop(QMainWindow):
    def check_position(self, width, sub_window):
        if width < 500:
            sub_window.move(randint(0, self.window_width()-(int(self.window_width()/2))),
                            randint(0, self.window_height()-(int(self.window_height()/2))) )
        else:
            sub_window.move(randint(0, self.window_width()-(int(self.window_width()/1.5))),
                            randint(0, self.window_height()-(int(self.window_height()/1.5))) )
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
        widget_dimensions = sub.frameGeometry()
        self.check_position(width=widget_dimensions.width(), sub_window=sub)
        sub.show()

    def open_titanium(self):
        print("Opening Titanium")
        sub = QMdiSubWindow()
        sub.setWidget(titanium.MainWindow())
        sub.setWindowTitle("Titanium")
        self.mdi.addSubWindow(sub)
        widget_dimensions = sub.frameGeometry()
        self.check_position(width=widget_dimensions.width(), sub_window=sub)
        sub.show()

    def open_calculator(self):
        print("Opening Calculator")
        sub = QMdiSubWindow()
        sub.setWidget(calculator.MainWindow())
        sub.setWindowTitle("Calculator")
        self.mdi.addSubWindow(sub)
        widget_dimensions = sub.frameGeometry()
        self.check_position(width=widget_dimensions.width(), sub_window=sub)
        sub.show()

    def open_notepad(self):
        print("Opening Notepad")
        sub = QMdiSubWindow()
        sub.setWidget(notepad.MainWindow())
        sub.setWindowTitle("Notepad")
        self.mdi.addSubWindow(sub)
        widget_dimensions = sub.frameGeometry()
        self.check_position(width=widget_dimensions.width(), sub_window=sub)
        sub.show()

    def open_paint(self):
        print("Opening Paint")
        sub = QMdiSubWindow()
        sub.setWidget(paint.MainWindow())
        sub.setWindowTitle("Paint")
        self.mdi.addSubWindow(sub)
        widget_dimensions = sub.frameGeometry()
        self.check_position(width=widget_dimensions.width(), sub_window=sub)
        sub.show()

    def open_solitaire(self):
        print("Opening Solitaire")
        sub = QMdiSubWindow()
        sub.setWidget(solitaire.MainWindow())
        sub.setWindowTitle("Solitaire")
        self.mdi.addSubWindow(sub)
        widget_dimensions = sub.frameGeometry()
        self.check_position(width=widget_dimensions.width(), sub_window=sub)
        sub.show()

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.screen = QDesktopWidget().screenGeometry()
        self.width = self.screen.width()
        self.height = self.screen.height()

        self.title = "Remote Desktop"
        self.left = 10
        self.top = 10
        self.initUI()
        self.create_mdi()
        self.create_menu()

        self.center_widget = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.mdi)
        self.center_widget.setLayout(layout)
        self.setCentralWidget(self.center_widget)

        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    # noinspection PyUnresolvedReferences
    def create_menu(self):
        self.menu = QMenuBar(self)
        self.menu.setNativeMenuBar(False)

        exitButton = QAction(QIcon("power.png"), "Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip("Power Off")

        browser = QAction(QIcon("browser.png"), "Boron", self)
        browser.setShortcut("Ctrl+B")
        browser.setStatusTip("Open Browser")

        titanium = QAction(QIcon("titanium.png"), "Titanium", self)
        titanium.setShortcut("Ctrl+T")
        titanium.setStatusTip("Open Titanium")

        calculator = QAction(QIcon("calculator.png"), "Cobalt", self)
        calculator.setShortcut("Ctrl+C")
        calculator.setStatusTip("Open Calculator")

        notepad = QAction(QIcon("notepad.png"), "Neon", self)
        notepad.setShortcut("Ctrl+N")
        notepad.setStatusTip("Open Notepad")

        paint = QAction(QIcon("paint.png"), "Paint", self)
        paint.setShortcut("Ctrl+P")
        paint.setStatusTip("Open Paint")

        solitaire = QAction(QIcon("solitaire.png"), "Xenon", self)
        solitaire.setShortcut("Ctrl+S")
        solitaire.setStatusTip("Open Solitaire")

        self.menu.addAction(exitButton)
        self.menu.addAction(browser)
        self.menu.addAction(titanium)
        self.menu.addAction(calculator)
        self.menu.addAction(notepad)
        self.menu.addAction(paint)
        self.menu.addAction(solitaire)

        exitButton.triggered.connect(self.close_desktop)
        browser.triggered.connect(self.open_browser)
        titanium.triggered.connect(self.open_titanium)
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
        self.pixmap.load("mt-mckinley.jpg")  # Change this to change the background photo
        self.mdi = MDIArea(self)
        self.mdi.cascadeSubWindows()


if __name__ == '__main__':
    available_styles = QStyleFactory.keys()
    print("The available styles are: " + str(available_styles) + ".")
    inputted_style = input("Please Enter a Style: ")

    app = QApplication(sys.argv)
    ex = Desktop()
    my_style = None
    if inputted_style == "":
        my_style = MyProxyStyle("")
    elif proxy_closest_match.closest_match(inputted_style) is not None:
        my_style = MyProxyStyle(proxy_closest_match.closest_match(inputted_style))
    else:
        print("""
Invalid Style
Valid Styles: Windows, Fusion, and macintosh""")
        exit(1)
    app.setStyle(my_style)
    app.exec_()
