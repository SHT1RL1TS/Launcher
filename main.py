import sys
from PyQt5.QtWidgets import QApplication, QMainWindow as qm, QWidget as qw
from application import appli

col = set.color
class home_page(qm):
    def __init__(self, app):
        super(home_page, self).__init__()
        self.app: QApplication = app
        self.setStyleSheet("background-color: "+col['black']+";")
    def showEvent(self, e):
        self.app.setWindowTitle('Главная страница')

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()

if __name__ == '__main__':
    app = appli(sys.argv)
    app.setWindows(app.windowsList)
    app.exec_()