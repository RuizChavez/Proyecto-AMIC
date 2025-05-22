import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import frmMenu
from classes.Form import Form
from forms.FileCreate import FileCreate
from forms.FileRead import FileRead
from forms.FileStats import FileStats
from forms.UserCreate import UserCreate
from forms.UserRead import UserRead
from modules.Database import Database


class Menu(Form):
    def __init__(self,db: Database, rol: str):
        self.db = db
        self.Form = frmMenu()
        self.rol = rol
        self.Form.FormClosing += self.Menu_FormClosing

        if self.rol == "Solo Expedientes":
            self.Form.btnStats.Visible = False
            self.Form.btnUsers.Visible = False
        
        if self.rol == "Solo Estadisticas":
            self.Form.btnFiles.Visible = False
            self.Form.btnUsers.Visible = False
        
        if self.rol == "Admin":
            self.Form.btnUsers.Visible = True

        self.Form.itemFilesCreate.Click += self.itemFilesCreate_Click
        self.Form.itemFilesRead.Click += self.itemFilesRead_Click
        self.Form.itemUsersCreate.Click += self.itemUsersCreate_Click
        self.Form.itemUsersRead.Click += self.itemUsersRead_Click        
        self.Form.btnStats.Click += self.btnStats_Click
        self.Form.btnCerrarSesion.Click += self.btnCerrarSesion_Click

        self.father: Form
        self.ActualForm = frmMenu()

    def Menu_FormClosing(self, sender, e):   
        self.father.Close()

    def itemFilesCreate_Click(self, sender, e):
        self.ActualForm.Close()
        self.ActualForm = FileCreate(self.db)
        self.ActualForm.pnlFather = self.Form.pnlForm
        self.Form.pnlForm.Controls.Clear()
        self.Form.pnlForm.Controls.Add(self.ActualForm.Form)
        self.ActualForm.Show()

    def itemFilesRead_Click(self, sender, e):
        self.ActualForm.Close()
        self.ActualForm = FileRead(self.db)
        self.Form.pnlForm.Controls.Clear()
        self.Form.pnlForm.Controls.Add(self.ActualForm.Form)
        self.ActualForm.Show()

    def itemUsersCreate_Click(self, sender, e):
        self.ActualForm.Close()
        self.ActualForm = UserCreate(self.db)
        self.Form.pnlForm.Controls.Clear()
        self.Form.pnlForm.Controls.Add(self.ActualForm.Form)
        self.ActualForm.Show()

    def itemUsersRead_Click(self, sender, e):
        self.ActualForm.Close()
        self.ActualForm = UserRead(self.db)
        self.ActualForm.father = self
        self.Form.pnlForm.Controls.Clear()
        self.Form.pnlForm.Controls.Add(self.ActualForm.Form)
        self.ActualForm.Show()

    def btnStats_Click(self, sender, e):
        self.ActualForm.Close()
        self.ActualForm = FileStats(self.db)
        self.Form.pnlForm.Controls.Clear()
        self.Form.pnlForm.Controls.Add(self.ActualForm.Form)
        self.ActualForm.Show()
        
    def btnCerrarSesion_Click(self, sender, e): 
        self.Form.Hide()
        self.father.Show()


        