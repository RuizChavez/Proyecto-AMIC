import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *

class Form():

    def __init__(self):
        self.Form: Form

    def Show(self):
        self.Form.Show()

    def Hide(self):
        self.Form.Hide()

    def Close(self):
        self.Form.Close()

    def Run(self):
        Application.Run(self.Form)

    def Exit(self):
        Application.Exit()
