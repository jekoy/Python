import turtle
import sys
from pySide.QtCore import *
from pySide.QtGui import *

class TurtleControl(Qwidgeh):
    def __init__(self,turtle):
        super(TurtleControl,self).__init__()
        self.turtle=turtle

        self.left_btn=QPushButton("left",self)
        self.right_btn=QPushButton("right",self)
        self.move_btn=QPushButton("move",self)
        self.distance_spin=QSpinBox()

        self.controlsLayout=QGridLayout()
        self.controlsLayout.addWidget(self.left_btn,0,0)
        self.controlsLayout.addWidget(self.right_btn,0,1)
        self.controlsLayout.addWidget(self.distance_spin,1,0)
        self.controlsLayout.addWidget(self.move_btn,1,1)
        self.setLayout(self.controlsLayout)

        self.distance_spin.setRange(0,100)
        self.distance_spin.setSinleStep(5)
        self.distance_spin.setValue(20)
window=turtle.Screen()
babbage=turtle.Turtle()

app=QApplication(sys,argv)
control_window=TurtleControl(babbage)
comtrol_window.show()

app.exec_()
sys.exit()

