import clr

clr.AddReference('AMIC')

from System import *
from forms.UserLogin import UserLogin
from modules.Database import Database

class App():
    def __init__(self):   
        self.db = Database()   
        self.Login = UserLogin(self.db)
        

    def Run(self):
        if self.db.IsOn:
            self.Login.Run()
        