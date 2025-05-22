import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import UsersRead, RJMessageBox
from classes.Form import Form
from forms.UserUpdate import UserUpdate
from database import dataUsers

class UserRead(Form):
    def __init__(self):
        self.Form = UsersRead()
        self.father: Form
        self.Form.Load += self.form_Load

    def form_Load(self, sender, e):
        for key in dataUsers.keys():
            self.Form.lbxUsers.Items.Add(key)

    def btnUpdate_Click(self, sender, e):
        if self.Form.lblUsers.SelectedIndex < 0:
            RJMessageBox.Show("Primero seleccione un usuario",
                "Error",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
        else:
            userUpdate = UserUpdate()
            self.father.Form.pnlPral.Controls.Clear()
            self.father.Form.pnlPral.Controls.Add(userUpdate.Form)
            userUpdate.Show()
            self.Close()

    def btnDelete_Click(self, sender, e):
        if self.Form.lblUsers.SelectedIndex < 0:
            RJMessageBox.Show("Primero seleccione un usuario",
                "Error",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);