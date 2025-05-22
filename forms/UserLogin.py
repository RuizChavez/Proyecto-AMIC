import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import UsersLogin, RJMessageBox
from classes.Form import Form
from modules.Database import Database
from forms.Menu import Menu

class UserLogin(Form):
    def __init__(self, db: Database):
        self.db = db
        self.Form = UsersLogin()
        self.Form.btnIngresar.Click += self.btnIngresar_Click
        self.Form.FormClosing += self.UserLogin_Closed

    def btnIngresar_Click(self, sender, e):
        user = self.Form.txtUser.Texts
        password = self.Form.txtPassword.Texts
        
        validacion_usuario = self.db.select_Usuario(user)
        validacion_contrasena = self.db.select_UsuarioPassword(user,password)
                
        if validacion_usuario.empty == False:
                
            if validacion_contrasena.empty == False: 
                self.Form.txtUser.Texts = ""
                self.Form.txtPassword.Texts = ""
                
                validacion_rol = validacion_contrasena.iloc[0,4]
                
                self.Menu = Menu(self.db,validacion_rol)
                self.Menu.father = self
                
                self.Form.Hide()
                self.Menu.Show()
                
            else:
                RJMessageBox.Show("Contraseña incorrecta",
                    "Error al ingresar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        else:
            RJMessageBox.Show("No existe el usuario",
                "Error al ingresar",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);

    def btnClose_Click(self, sender, e): 
        self.Form.Show()

    def UserLogin_Closed(self, sender, e):
        self.Exit()
