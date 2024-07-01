from typing import List
from PyQt6.QtWidgets import QApplication as qa, QStackedWidget as qs
from main import home_page
class app(qa):
    windows = []
    def __init__(self, argv) -> None:
        super(app).__init__(argv)
        self.root = self.createRootWidget()
        self.windows = {
            'main': home_page(self),
        }
    def exec_(self):
        self.ToRo
    def createRootWidget(self):
        root = qs()
        root.setFixedSize(self.desktop().screenGeometry().width(), self.desktop().availableGeometry().height() - 40)

        root.setMinimumWidth(900)
        root.setMinimumHeight(600)

        root.setMaximumWidth(self.desktop().screenGeometry().width())
        root.setMaximumHeight(self.desktop().availableGeometry().height() - 40)

        return root