from PyQt5.QtCore import Qt, QRect, QTimer
from PyQt5.QtGui import QFontMetrics, QPainter
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

    def makeShort(self):
        self.short = self.long
        metrics = QFontMetrics(self.font())
        width = metrics.width(self.short)

        if width >= self.width():
            while width >= self.width():
                self.short = self.short[:-1]
                width = metrics.width(self.short + '...')

            self.short = self.short + '...'

    def setText(self, a0):
        self.long = a0
        self.makeShort()

        self.txt = self.short
        self.refresh()

    def enterEvent(self, event):
        self.txt = self.long
        self.refresh()
        self.timer.start(50)

    def leaveEvent(self, event):
        self.timer.stop()
        self.txt = self.short
        self.refresh()

    def paintEvent(self, a0):
        self.textWidth = QFontMetrics(self.font()).width(self.txt)

        painter = QPainter(self)
        painter.setFont(self.font())
        painter.setPen(self.palette().windowText().color())
        painter.setBrush(self.palette().windowText())

        if self.textWidth > self.width():
            painter.drawText(QRect(self.x, 0, self.textWidth, self.height()),
                             Qt.AlignHCenter | (self.alignment() & Qt.AlignVCenter), self.txt)
        else:
            painter.drawText(QRect(0, 0, self.width(), self.height()), self.alignment(), self.txt)
            self.timer.stop()
