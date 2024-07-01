from typing import List
from PyQt5.QtWidgets import QApplication, QStackedWidget as qs
from main import home_page
class appli(QApplication):
    windows = []
    def __init__(self, argv) -> None:
        super(appli).__init__(argv)
        self.root = self.createRootWidget()
        self.windows = {
            'main': home_page(self),
        }
    def exec_(self):
        self.addWidgetsToRoot()
        self.root.show()
        super(appli, self).exec_()
    def createRootWidget(self):
        root = qs()
        root.setFixedSize(self.desktop().screenGeometry().width(), self.desktop().availableGeometry().height() - 40)

        root.setMinimumWidth(900)
        root.setMinimumHeight(600)

        root.setMaximumWidth(self.desktop().screenGeometry().width())
        root.setMaximumHeight(self.desktop().availableGeometry().height() - 40)

        return root
    def Update(self):
        for win in self.windows.keys():
            self.windows[win].update()
    def set(self, windows):
        self.windows = windows
    def get(self, windowName):
        return self.windows[windowName]
    def add(self):
        for window in self.windows:
            self.root.addWidget(self.windows[window])
    def go(self, windowName, pattern = {}):
        window = self.windows[windowName]
        self.windows[windowName].header.update()
        self.windows[windowName].update()
        for pattern_name in pattern:
            pattern_value = pattern[pattern_name]
            setattr(window, pattern_name,pattern_value)
        index = list(self.windows).index(windowName)
        self.root.setCurrentIndex(index)
    def setTitle(self, title):
        self.root.setWindowTitle(title)