from PyQt5.QtCore import Qt, QRect, QTimer
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QLabel


class ScrollLabel(QLabel):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move)

    def move(self):
        if self.countdown > 0:
            self.countdown -= self.timer.interval()
        elif self.reverse:
            if self.x >= 0:
                self.refresh(cooldown=True)
            else:
                self.x += 1
        else:
            if self.textWidth + self.x <= self.width():
                self.refresh(reverse=True, cooldown=True)
            else:
                self.x -= 1

        self.update()

    def refresh(self, reverse=False, cooldown=False):
        self.x = self.width() - self.textWidth if reverse else 0
        self.countdown = 2000 if cooldown else 0
        self.reverse = reverse
        self.update()

    def setText(self, a0):
        self.txt = a0
        self.refresh()

    def enterEvent(self, event):
        self.timer.start(50)

    def leaveEvent(self, event):
        self.timer.stop()
        self.refresh()

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setFont(self.font())
        painter.setPen(QColor('transparent'))
        painter.setBrush(QColor('transparent'))

        self.textWidth = painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignHCenter,
                                          self.txt).width()

        painter.setPen(self.palette().windowText().color())
        painter.setBrush(self.palette().windowText())

        if self.textWidth > self.width():
            painter.drawText(QRect(self.x, 0, self.textWidth, self.height()),
                             Qt.AlignHCenter | (self.alignment() & Qt.AlignVCenter), self.txt)
        else:
            painter.drawText(QRect(0, 0, self.width(), self.height()), self.alignment(), self.txt)
            self.timer.stop()
