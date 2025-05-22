import clr
import re



clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import FilesUpdate, RJMessageBox
from classes.Form import Form, Panel
from forms.FileUpdateStepA import FileUpdateStepA
from forms.FileUpdateStepB import FileUpdateStepB
from modules.Validations import *
from modules.ModuleFile import Update
from modules.Database import Database
from models.File import File

class FileUpdate(Form):
    def __init__(self,db: Database, oldFile: File):
        self.db = db
        self.Form = FilesUpdate()
        self.father: Form
        self.step = 0
        self.noControlPattern = re.compile(r"[\d]{3}\/[\d]{3}")
       
        self.stepA = FileUpdateStepA(oldFile)
        self.stepA.Form.btnCancel.Click += self.btnCancel_Click
        self.stepA.Form.btnNext.Click += self.btnNext_Click

        self.stepB = FileUpdateStepB(oldFile)
        self.stepB.Form.btnCancel.Click += self.btnCancel_Click
        self.stepB.Form.btnBack.Click += self.btnBack_Click
        self.stepB.Form.btnSave.Click += self.btnSave_Click

        self.Form.pnlFileCreate.Controls.Add(self.stepA.Form)
        self.stepA.Show()

        self.oldFile = oldFile

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
            file = File(data["base"],data["no_control"],data["fecha_recibido"],
                data["fecha_emitido"],data["agencia"], data["nuc"], data["delitos"], 
                data["clasificacion_hecho"],data["imputados"],data["ofendidos"], 
                data["status_"],data["no_oficio_cumplimiento"],data["colaboracion"], 
                data["fecha_cumplimentacion"], data["semaforo"])
            file.id = self.oldFile.id
            self.db.File_Update(file)
            self.stepA.Close()
            self.stepB.Close()
            self.Close()
