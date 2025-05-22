import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from System.Drawing import *
from AMIC import FilesUpdateStepB, RJMessageBox
from classes.Form import Form
from modules.Dicts import *
from modules.Validations import *
from models.File import *

class FileUpdateStepB(Form):
    def __init__(self, oldFile: File):
        self.Form = FilesUpdateStepB()
        self.Form.cbxDelito.Items.AddRange(dictDelitos.values())
        self.Form.btnSaveDelito.Click += self.btnSaveDelito_Click
        self.Form.btnSaveImputado.Click += self.btnSaveImputado_Click
        self.Form.btnSaveOfendido.Click += self.btnSaveOfendido_Click
        self.Form.txtImputado.KeyPress += self.txtImputado_KeyPress
        self.Form.txtOfendido.KeyPress += self.txtOfendido_KeyPress

        if str(oldFile.delito).__contains__(","):
            listDelitos = oldFile.delito.split(",")
        else:
            listDelitos = [oldFile.delito]

        if str(oldFile.imputado).__contains__(","):
            listImputados = oldFile.imputado.split(",")
        else:
            listImputados = [oldFile.imputado]

        if str(oldFile.ofendido).__contains__(","):
            listOfendidos = oldFile.ofendido.split(",")
        else:
            listOfendidos = [oldFile.ofendido]

        for d in listDelitos:
            if d == "---": break
            self.Form.flpDelitosAdd(d)

        for d in listImputados:
            if d == "---": break
            self.Form.flpImputadosAdd(d)

        for d in listOfendidos:
            if d == "---": break
            self.Form.flpOfendidosAdd(d)

    def btnSaveDelito_Click(self, sender, e):
        self.Form.cbxDelito.BorderColor = Color.FromArgb(221, 220, 221)
        if self.Form.cbxDelito.SelectedIndex >= 0:
            self.Form.flpDelitosAdd(str(self.Form.cbxDelito.SelectedItem))
            self.Form.cbxDelito.SelectedIndex = -1
        else:
            self.Form.cbxDelito.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("No has seleccionado un delito",
                "Faltan campos por seleccionar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);

    def btnSaveImputado_Click(self, sender, e):
        self.Form.txtImputado.BorderColor = Color.FromArgb(203,184,125)
        if not nombresValidation.fullmatch(self.Form.txtImputado.Texts):
            if not self.Form.txtImputado.Texts:
                self.Form.txtImputado.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("No has ingresado el nombre del imputado",
                    "Faltan campos por ingresar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            else:
                self.Form.txtImputado.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("No puedes agregar comas (,) en los nombres",
                    "Campo no valido",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        else:
            self.Form.flpImputadosAdd(self.Form.txtImputado.Texts)
            self.Form.txtImputado.Texts = ""

    def btnSaveOfendido_Click(self, sender, e):
        self.Form.txtOfendido.BorderColor = Color.FromArgb(203,184,125)
        if not nombresValidation.fullmatch(self.Form.txtOfendido.Texts):
            if not self.Form.txtOfendido.Texts:
                self.Form.txtOfendido.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("No has ingresado el nombre del ofendido",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            else:
                self.Form.txtOfendido.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("No puedes agregar comas (,) en los nombres",
                    "Campo no valido",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        else:
            self.Form.flpOfendidosAdd(self.Form.txtOfendido.Texts)
            self.Form.txtOfendido.Texts = ""

    def txtImputado_KeyPress(self, sender, e):
        self.Form.txtImputado.BorderColor = Color.FromArgb(203,184,125)
        if e.KeyChar == chr(Keys.Enter):
            if not nombresValidation.fullmatch(self.Form.txtImputado.Texts):
                if not self.Form.txtImputado.Texts:
                    self.Form.txtImputado.BorderColor = Color.FromArgb(255,128,128)
                    RJMessageBox.Show("No has ingresado el nombre del imputado",
                        "Faltan campos por seleccionar",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                else:
                    self.Form.txtImputado.BorderColor = Color.FromArgb(255,128,128)
                    RJMessageBox.Show("No puedes agregar comas (,) en los nombres",
                        "Campo no valido",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
            else:
                self.Form.flpImputadosAdd(self.Form.txtImputado.Texts)
                self.Form.txtImputado.Texts = ""

    def txtOfendido_KeyPress(self, sender, e):
        self.Form.txtOfendido.BorderColor = Color.FromArgb(203,184,125)
        if e.KeyChar == chr(Keys.Enter):
            if not nombresValidation.fullmatch(self.Form.txtOfendido.Texts):
                if not self.Form.txtOfendido.Texts:
                    self.Form.txtOfendido.BorderColor = Color.FromArgb(255,128,128)
                    RJMessageBox.Show("No has ingresado el nombre del ofendido",
                        "Faltan campos por seleccionar",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                else:
                    self.Form.txtOfendido.BorderColor = Color.FromArgb(255,128,128)
                    RJMessageBox.Show("No puedes agregar comas (,) en los nombres",
                        "Campo no valido",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
            else:
                self.Form.flpOfendidosAdd(self.Form.txtOfendido.Texts)
                self.Form.txtOfendido.Texts = ""

    def isValidated(self):
        if len(self.Form.flpDelitos.Controls) == 0:
            RJMessageBox.Show("No has ingresado un delito",
                "Faltan campos por seleccionar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return False
        else:
            return True
        
    def getValues(self):
        delitos = ""
        imputados = ""
        ofendidos = ""

        listDelitos = list(self.Form.listDelitos)
        listImputados = list(self.Form.listImputados)
        listOfendidos = list(self.Form.listOfendidos)

        for d in listDelitos:
            delitos += f"{dictDelitosValues[d]},"
        delitos += ","
        delitos = delitos.replace(",,","")

        if len(listImputados) > 0:
            for i in listImputados:
                imputados += f"{i},"
            imputados += ","
            imputados = imputados.replace(",,","")
        else:
            imputados = "---"

        if len(listOfendidos) > 0:
            for o in listOfendidos:
                ofendidos += f"{o},"
            ofendidos += ","
            ofendidos = ofendidos.replace(",,","")
        else:
            ofendidos = "---"

        data = {
            "delitos":delitos,
            "imputados":imputados,
            "ofendidos":ofendidos
        }

        return data
