import clr
import re



clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import FilesCreate, RJMessageBox
from classes.Form import Form, Panel
from forms.FileCreateStepA import FileCreateStepA
from forms.FileCreateStepB import FileCreateStepB
from modules.Validations import *
from modules.ModuleFile import Create
from modules.Database import Database
import pprint as pp

class FileCreate(Form):
    def __init__(self, db: Database):
        self.db = db
        self.Form = FilesCreate()
        self.father: Form
        self.step = 0
        self.noControlPattern = re.compile(r"[\d]{3}\/[\d]{3}")
       
        self.stepA = FileCreateStepA()
        self.stepA.Form.btnCancel.Click += self.btnCancel_Click
        self.stepA.Form.btnNext.Click += self.btnNext_Click

        self.stepB = FileCreateStepB()
        self.stepB.Form.btnCancel.Click += self.btnCancel_Click
        self.stepB.Form.btnBack.Click += self.btnBack_Click
        self.stepB.Form.btnSave.Click += self.btnSave_Click

        self.Form.pnlFileCreate.Controls.Add(self.stepA.Form)
        self.stepA.Show()

    def btnNext_Click(self, sender, e):
        if (self.stepA.isValidated()):
            self.Form.pnlFileCreate.Controls.Clear()
            self.Form.pnlFileCreate.Controls.Add(self.stepB.Form)
            self.stepB.Show()
            self.stepA.Hide()

    def btnCancel_Click(self, sender, e):
        self.Form.Parent.Controls.Clear()
        self.stepB.Close()
        self.stepA.Close()
        self.Close()

    def btnBack_Click(self, sender, e):
        self.Form.pnlFileCreate.Controls.Clear()
        self.Form.pnlFileCreate.Controls.Add(self.stepA.Form)
        self.stepA.Show()
        self.stepB.Hide()

    def btnSave_Click(self, sender, e):
        if (self.stepB.isValidated()):
            data = self.stepA.getValues() | self.stepB.getValues()
            Create(self.db, data)
            self.stepA.Close()
            self.stepB.Close()
            self.Close()


