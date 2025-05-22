import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from AMIC import FilesRead
from classes.Form import Form
from modules.Database import Database
from modules.ModuleEstadisticas import dataFrameToList
from modules.Dicts import dictAgencias, dictBases, dictClasificacionHecho, dictStatus,dictDelitos
from modules.ModuleFile import *
from models.File import *
from tkinter import messagebox
from forms.FileUpdate import FileUpdate
import pprint as pp
from datetime import datetime
from AMIC import RJMessageBox

class FileRead(Form):
    def __init__(self, db: Database):
        self.db = db
        self.agencia = "agencia"
        self.base = "base"
        self.delitos = "delitos"
        self.status = "status_"
        self.Form = FilesRead()
        self.father: Form
        self.Form.cbxAgencia.OnSelectedIndexChanged += self.cbxAgencia_OnSelectedIndexChanged
        self.Form.cbxAgencia.Items.Add("...")
        self.Form.cbxBase.OnSelectedIndexChanged += self.cbxBase_OnSelectedIndexChanged
        self.Form.cbxBase.Items.Add("...")
        self.Form.cbxDelito.OnSelectedIndexChanged += self.cbxDelito_OnSelectedIndexChanged
        self.Form.cbxDelito.Items.Add("...")
        self.Form.cbxStatus.OnSelectedIndexChanged += self.cbxStatus_OnSelectedIndexChanged
        self.Form.cbxStatus.Items.Add("...")
        self.Form.btnDelete.Click += self.btnDelete_Click
        self.Form.btnUpdate.Click += self.btnUpdate_Click
        self.Form.cbxAgencia.Items.AddRange(dictAgencias.values())
        self.Form.cbxBase.Items.AddRange(dictBases.values())
        self.Form.cbxDelito.Items.AddRange(dictDelitos.values())
        self.Form.cbxStatus.Items.AddRange(dictStatus.values())
        self.Form.dtpFechaInicio.ValueChanged += self.dtpFechaInicio_ValueChanged
        self.Form.dtpFechaFin.ValueChanged += self.dtpFechaFin_ValueChanged
        

        self.df = self.db.File_Read()
        self.df["agencia"] = self.df["agencia"].map(self.traducirDictAgencias)
        self.df["base"] = self.df["base"].map(self.traducirDictBase)
        self.df["status_"] = self.df["status_"].map(self.traducirDictStatus)
        self.df["delitos"] = self.df["delitos"].map(self.traducirDictDelitos)
        self.df["clasificacion_hecho"] = self.df["clasificacion_hecho"].map(self.traducirDictClasificacion)

        self.df = self.df.query("agencia=="+self.agencia+" & base=="+self.base+" & delitos=="+self.delitos+" & status_=="+self.status+"")
        self.Form.dgvExpedientes.Rows.Clear()
        lista = dataFrameToList(self.df)
        for n in self.df.columns:
            self.Form.dgvExpedientes.Columns.Add(str(n),str(n))
            
        for n in lista:
            self.Form.dgvExpedientes.Rows.Add(n)
    
    def cbxAgencia_OnSelectedIndexChanged(self, sender, e):
        if self.Form.cbxAgencia.SelectedIndex >=0 and str(self.Form.cbxAgencia.SelectedItem) != "...":
            self.agencia = "'"+str(self.Form.cbxAgencia.SelectedItem)+"'"
        else:
            self.agencia = "agencia"
        self.actualizarDgv()

    def cbxBase_OnSelectedIndexChanged(self, sender, e):
        if self.Form.cbxBase.SelectedIndex >=0 and str(self.Form.cbxBase.SelectedItem) != "...":
            self.base = "'"+str(self.Form.cbxBase.SelectedItem)+"'"
        else:
            self.base = "base"
        self.actualizarDgv()
    
    def cbxDelito_OnSelectedIndexChanged(self, sender, e):
        if self.Form.cbxDelito.SelectedIndex >=0 and str(self.Form.cbxDelito.SelectedItem) != "...":
            self.delitos = "'"+str(self.Form.cbxDelito.SelectedItem)+"'"
        else:
            self.delitos = "delitos"
        self.actualizarDgv()

    def cbxStatus_OnSelectedIndexChanged(self, sender, e):
        if self.Form.cbxStatus.SelectedIndex >=0 and str(self.Form.cbxStatus.SelectedItem) != "...":
            self.status = "'"+str(self.Form.cbxStatus.SelectedItem)+"'"
        else:
            self.status = "status_"
        self.actualizarDgv()

    def btnDelete_Click(self, sender, e):
            id = self.Form.dgvExpedientes.SelectedCells[0].Value
            self.db.File_Delete(id)
            messagebox.showinfo(message="Expediente Borrado Exitosamente", title="Expediente Borrado")
            self.actualizarDgv()
        
    def dtpFechaInicio_ValueChanged(self,sender, e):
        date_fecha_inicio = datetime.strptime(self.Form.dtpFechaInicio.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")
        date_fecha_fin = datetime.strptime(self.Form. dtpFechaFin.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")

        dDiasFechas = (date_fecha_fin - date_fecha_inicio).days

        if dDiasFechas < 0:
            RJMessageBox.Show("La fecha de inicio no puede ser mayor a la de fin",
                    "Fecha invalida",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
    
        self.actualizarDgv()
    
    def dtpFechaFin_ValueChanged(self,sender, e):
        date_fecha_inicio = datetime.strptime(self.Form.dtpFechaInicio.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")
        date_fecha_fin = datetime.strptime(self.Form. dtpFechaFin.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")

        dDiasFechas = (date_fecha_fin - date_fecha_inicio).days

        if dDiasFechas < 0:
            RJMessageBox.Show("La fecha de inicio no puede ser mayor a la de fin",
                    "Fecha invalida",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);

    def traducirDictAgencias(self,x):
        return dictAgencias[x]
    
    def traducirDictDelitos(self, x):
        if x.__contains__(","):
            result = ""
            listX = x.split(",")
            for i, y in enumerate(listX):
                result += dictDelitos[y]
                if i != len(listX)-1:
                    result += ", "
            return result
        else:
            return dictDelitos[x]
    
    def traducirDictBase(self,x):
        return dictBases[x]
    
    def traducirDictStatus(self,x):
        return dictStatus[x]
    
    def traducirDictClasificacion(self,x):
        return dictClasificacionHecho[x]

    def actualizarDgv(self):

        self.df = self.db.File_Read()
        self.df["agencia"] = self.df["agencia"].map(self.traducirDictAgencias)
        self.df["base"] = self.df["base"].map(self.traducirDictBase)
        self.df["status_"] = self.df["status_"].map(self.traducirDictStatus)
        self.df["delitos"] = self.df["delitos"].map(self.traducirDictDelitos)
        self.df["clasificacion_hecho"] = self.df["clasificacion_hecho"].map(self.traducirDictClasificacion)
        
        date_fecha_inicio = self.Form.dtpFechaInicio.Value.ToString("yyyy-MM-dd")
        date_fecha_fin = self.Form.dtpFechaFin.Value.ToString("yyyy-MM-dd")
        
        date_fecha_inicio = datetime.strptime(date_fecha_inicio, "%Y-%m-%d").date()
        date_fecha_fin = datetime.strptime(date_fecha_fin, "%Y-%m-%d").date()
        
        self.df = self.df.query("agencia=="+self.agencia+" & base=="+self.base+" & delitos=="+self.delitos+" & status_=="+self.status+
                                " & @date_fecha_inicio <= fecha_emitido <= @date_fecha_fin")
        self.Form.dgvExpedientes.Rows.Clear()
        lista = dataFrameToList(self.df)
        
        for n in lista:
            self.Form.dgvExpedientes.Rows.Add(n)

    def btnUpdate_Click(self, sender, e):
        id = int(self.Form.dgvExpedientes.SelectedCells[0].Value)
        query = self.df.where(self.df["id"]==id).dropna()
        query["INDEX"] = [0]
        query = query.set_index("INDEX")
        file = File(query["base"][0],query["no_control"][0],query["fecha_recibido"][0],query["fecha_emitido"][0],query["agencia"][0],query["nuc"][0],query["delitos"][0],query["clasificacion_hecho"][0],query["imputados"][0],query["ofendidos"][0],query["status_"][0],query["no_oficio_cumplimiento"][0],query["colaboracion"][0],query["fecha_cumplimentacion"][0],query["semaforo"][0])
        
        print(file.fecha_cumplimentacion)
        file.id = id
        form = FileUpdate(self.db,file)
        parent = self.Form.Parent
        parent.Controls.Clear()
        parent.Controls.Add(form.Form)
        form.Show()

        self.Close()    


    def btnDelete_Click(self, sender, e):
            id = self.Form.dgvExpedientes.SelectedCells[0].Value
            self.db.File_Delete(id)
            messagebox.showinfo(message="Expediente Borrado Exitosamente", title="Expediente Borrado")
            self.actualizarDgv()
            

        