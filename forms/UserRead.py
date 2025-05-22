import clr

clr.AddReference('AMIC')

from modules.ModuleEstadisticas import dataFrameToList
from System.Windows.Forms import *
from AMIC import UsersRead, RJMessageBox
from classes.Form import Form
from forms.UserUpdate import UserUpdate
from modules.Database import Database
from tkinter import messagebox
from models.User import User
class UserRead(Form):
    def __init__(self, db: Database):
        self.db = db
        self.Form = UsersRead()
        self.father: Form
        self.Form.btnDelete.Click += self.btnDelete_Click
        self.Form.btnUpdate.Click += self.btnUpdate_Click

        self.df = self.db.User_Read()
        df_lista = self.df.loc[:, self.df.columns != "password"]
        self.lista = dataFrameToList(df_lista)

        for n in self.df.columns:
            if str(n) != "password":
                self.Form.dgvUsuarios.Columns.Add(str(n),str(n))
            
        for n in self.lista:
            self.Form.dgvUsuarios.Rows.Add(n)

    def btnUpdate_Click(self, sender, e):
        usuarioviejo = int(self.Form.dgvUsuarios.SelectedCells[0].Value)
        query = self.df.loc[self.df["id"]==usuarioviejo]
        query = query.iloc[0]
        
        usuarioPrueba = User(query["username"], str(query["password"]),  query["base"],query["rols"])
        userUpdate = UserUpdate(self.db,query["id"],usuarioPrueba)
        self.father.Form.pnlForm.Controls.Clear()
        self.father.Form.pnlForm.Controls.Add(userUpdate.Form)
        userUpdate.Show()
        self.Close()

    def btnDelete_Click(self, sender, e):
            id = self.Form.dgvUsuarios.SelectedCells[0].Value
            print(id)
            self.db.User_Delete(id)
            messagebox.showinfo(message="Usuario Borrado Exitosamente", title="Usuario Borrado")
            self.actualizarDgv()
            
    def actualizarDgv(self):
        df = self.db.User_Read()
        df = df.loc[:, df.columns != "password"]
        lista = dataFrameToList(df)

        self.Form.dgvUsuarios.Rows.Clear()
        self.Form.dgvUsuarios.Columns.Clear()

        for n in df.columns:
            self.Form.dgvUsuarios.Columns.Add(str(n),str(n))
            
        for n in lista:
            self.Form.dgvUsuarios.Rows.Add(n)
        
