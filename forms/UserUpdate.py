import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from System.Drawing import *
from AMIC import UsersUpdate, RJMessageBox
from classes.Form import Form
from modules.ModuleUser import ModuleUser
from models.User import User
from modules.Database import Database
from tkinter import messagebox
from modules.Dicts import *


class UserUpdate(Form):
    def __init__(self,db: Database, id: int,data: User):
        self.db = db
        self.Form = UsersUpdate()
        self.Form.btnSave.Click += self.btnSave_Click
        self.Form.btnCancel.Click += self.btnCancel_Click
        self.father: Form
        self.data = data
        self.id = id
        self.Form.txtName.Texts = str(data.username)
        self.Form.txtPassword.Texts = data.password
        #self.Form.cbxRol.Texts = data.rol
        self.Form.cbxAgencia.Texts = data.base

        self.Form.cbxAgencia.Items.Clear()
        self.Form.cbxRol.Items.AddRange(["Solo Expedientes","Solo Estadisticas","Admin"])

        self.Form.cbxAgencia.Items.Clear()
        self.Form.cbxAgencia.Items.AddRange(dictBasesValues.keys())
        
        self.Form.cbxRol.SelectedIndex = self.Form.cbxRol.Items.IndexOf(str(self.data.rol))
        self.Form.cbxRol.SelectedItem = self.Form.cbxRol.SelectedIndex
        
        self.Form.cbxAgencia.Texts = getValueBases(self.data.base)
        self.Form.cbxAgencia.SelectedIndex = self.Form.cbxAgencia.Items.IndexOf((self.Form.cbxAgencia.Texts).upper())
        self.Form.cbxAgencia.SelectedItem = self.Form.cbxAgencia.SelectedIndex
        
    def btnSave_Click(self, sender, e):
        if self.verify():
            data = self.Form

            usuarioNuevo = User(f"'{data.txtName.Texts}'", f"'{data.txtPassword.Texts}'", f"'{dictBasesValues[data.cbxAgencia.SelectedItem]}'", f"'{data.cbxRol.SelectedItem}'")
            self.db.User_Update(usuarioNuevo,self.id,)

            messagebox.showinfo(message="Usuario Modificado Exitosamente", title="Usuario Modificado")

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