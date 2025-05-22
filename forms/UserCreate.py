import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from System.Drawing import *
from AMIC import UsersCreate, RJMessageBox
from classes.Form import Form
from models.User import User
from modules.Database import Database
from modules.ModuleUser import ModuleUser
from modules.Dicts import dictBasesValues

class UserCreate(Form):
    def __init__(self, db: Database):
        self.db = db
        self.Form = UsersCreate()
        self.Form.btnSave.Click += self.btnSave_Click
        self.Form.btnCancel.Click += self.btnCancel_Click
        self.father: Form
        self.Form.cbxAgencia.Items.Clear()
        self.Form.cbxRol.Items.AddRange(["Solo Expedientes","Solo Estadisticas","Admin"])
        self.Form.cbxAgencia.Items.Clear()
        self.Form.cbxAgencia.Items.AddRange(dictBasesValues.keys())

    def btnSave_Click(self, sender, e):
        if self.verify():
            self.id = self.db.User_Count()+1
            self.data = self.Form
            usuarioNuevo = User(f"'{self.data.txtName.Texts}'", f"'{self.data.txtPassword.Texts}'", f"'{dictBasesValues[self.data.cbxAgencia.SelectedItem]}'", f"'{self.data.cbxRol.SelectedItem}'")
            self.db.User_Create(usuarioNuevo)
            RJMessageBox.Show("Usuario registrado correctamente",
                "Registro correcto",
                MessageBoxButtons.OK);

            self.Close()

    def btnCancel_Click(self, sender, e):
        self.Form.Close()

    def verify(self):
        self.data = self.Form
        self.Form.txtName.BorderColor = Color.FromArgb(203, 184, 125)
        self.Form.txtPassword.BorderColor = Color.FromArgb(203, 184, 125)
        self.Form.txtPassword2.BorderColor = Color.FromArgb(203, 184, 125)
        self.Form.cbxRol.BorderColor = Color.FromArgb(203, 184, 125)
        self.Form.cbxAgencia.BorderColor = Color.FromArgb(203, 184, 125)
        
        if len(self.data.txtName.Texts) < 1:
            self.Form.txtName.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("Falto registrar el Nombre del usuario",
                "Faltan datos por ingresar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return False
        if len(self.data.txtName.Texts) < 8:
                self.Form.txtName.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("El nombre de usuario es demasiado corto",
                "El usuario tiene que ser almenos 8 caracteres",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
                return False
        for character in range(0, len(self.data.txtName.Texts)):
            if ord(self.data.txtName.Texts[character])<42 or ord(self.data.txtName.Texts[character])>122:
                self.Form.txtName.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("Se ha detectado un simbolo desconocido",
                "Porfavor escriba su usuario con valores normales",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
                return False    
        if len(self.data.txtPassword.Texts) < 1:
            self.Form.txtPassword.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("Falto registrar la Contraseña del usuario",
                "Faltan datos por ingresar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return False
        if len(self.data.txtPassword.Texts) < 8:
                self.Form.txtPassword.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("La contraseña es demasiado corta",
                "La contraseña tiene que ser almenos 8 caracteres",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
                return False
        for character in range(0, len(self.data.txtPassword.Texts)):
            if ord(self.data.txtPassword.Texts[character])<42 or ord(self.data.txtPassword.Texts[character])>122:
                self.Form.txtPassword.BorderColor = Color.FromArgb(255,128,128)
                RJMessageBox.Show("Se ha detectado un simbolo desconocido",
                "Porfavor escriba su contraseña con valores normales",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
                return False
        if self.data.txtPassword.Texts != self.data.txtPassword2.Texts:
            self.Form.txtPassword2.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("Las contraseñas entre ambos campos son diferentes",
                "Asegurence de que el campo de confirmar contraseña sea igual que contraseña",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return False     
        if self.data.cbxRol.SelectedIndex < 0:
            self.Form.cbxRol.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("Falto registrar la Base o Departamento",
                "Faltan datos por ingresar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return False
        if self.data.cbxAgencia.SelectedIndex < 0:
            self.Form.cbxAgencia.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("Falto registrar la Base o Departamento",
                "Faltan datos por ingresar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
            return False   
        return True
    
    