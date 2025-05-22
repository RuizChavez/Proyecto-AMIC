import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import StatsRead
from classes.Form import Form

class StatRead(Form):
    def __init__(self):
        self.Form = StatsRead()
        self.father: Form