import clr

clr.AddReference('AMIC')

from System.Windows.Forms import *
from System.Drawing import *
from AMIC import FilesCreateStepA, RJMessageBox
from classes.Form import Form
from modules.Dicts import *
from modules.Validations import *
from datetime import datetime

class FileCreateStepA(Form):
    def __init__(self):
        self.Form = FilesCreateStepA()
        self.Form.cbxDepto.Items.AddRange(dictBases.values())
        self.Form.cbxAgencia.Items.AddRange(dictAgencias.values())
        self.Form.cbxClasificacionHecho.Items.AddRange(dictClasificacionHecho.values())
        self.Form.cbxStatus.Items.AddRange(dictStatus.values())
        self.Form.cbxStatus.OnSelectedIndexChanged += self.cbxStatus_OnSelectedIndexChanged
        self.Form.cbxColaboracion.Items.AddRange(['Si','No'])   

        self.Form.LimitDay(datetime.now().year,datetime.now().month,datetime.now().day)

    def isValidated(self):
        date_fecha_emi = datetime.strptime(self.Form.dpFechaEmi.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")
        date_fecha_cum = datetime.strptime(self.Form.dpFechaCumpli.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")
        date_fecha_rec = datetime.strptime(self.Form.dpFechaRec.Value.ToString("yyyy-MM-dd"),"%Y-%m-%d")

        dDiasEmiRec = (date_fecha_rec - date_fecha_emi).days
        dDiasEmiCum = (date_fecha_cum - date_fecha_emi).days
        
        self.Form.cbxDepto.BorderColor = Color.FromArgb(221, 220, 221)
        self.Form.cbxAgencia.BorderColor = Color.FromArgb(221, 220, 221)
        self.Form.cbxClasificacionHecho.BorderColor = Color.FromArgb(221, 220, 221)
        self.Form.cbxColaboracion.BorderColor = Color.FromArgb(221, 220, 221)
        self.Form.cbxStatus.BorderColor = Color.FromArgb(221, 220, 221)
        self.Form.txtNuc.BorderColor = Color.FromArgb(203,184,125)
        self.Form.txtNoControl.BorderColor = Color.FromArgb(203,184,125)
        self.Form.txtNoOficioCumplimiento.BorderColor = Color.FromArgb(203,184,125)
        
        self.Form.labelObl1.Visible = False
        self.Form.labelObl2.Visible = False
        self.Form.labelObl3.Visible = False
        self.Form.labelObl4.Visible = False
        self.Form.labelObl5.Visible = False
        self.Form.labelObl6.Visible = False
        self.Form.labelObl7.Visible = False

        if not self.Form.dpFechaCumpli.Visible:
            dDiasEmiCum = 0

        if not self.Form.cbxDepto.SelectedIndex >= 0:
            self.Form.cbxDepto.BorderColor = Color.FromArgb(255,128,128)
            self.Form.labelObl1.Visible = True
            RJMessageBox.Show("No has seleccionado la base o el departamento",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not self.Form.cbxAgencia.SelectedIndex >= 0:
            self.Form.cbxAgencia.BorderColor = Color.FromArgb(255,128,128)
            self.Form.labelObl2.Visible = True
            RJMessageBox.Show("No has seleccionado la agencia",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not self.Form.cbxClasificacionHecho.SelectedIndex >= 0:
            self.Form.cbxClasificacionHecho.BorderColor = Color.FromArgb(255,128,128)
            self.Form.labelObl3.Visible = True
            RJMessageBox.Show("No has seleccionado la clasificacion del hecho",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not self.Form.cbxColaboracion.SelectedIndex >= 0:
            self.Form.cbxColaboracion.BorderColor = Color.FromArgb(255,128,128)
            self.Form.labelObl4.Visible = True
            RJMessageBox.Show("No has seleccionado la colaboracion del expediente",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not self.Form.cbxStatus.SelectedIndex >= 0:
            self.Form.cbxStatus.BorderColor = Color.FromArgb(255,128,128)
            self.Form.labelObl5.Visible = True
            RJMessageBox.Show("No has seleccionado el status",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not nucValidation.fullmatch(self.Form.txtNuc.Texts):
            self.Form.txtNuc.BorderColor = Color.FromArgb(255,128,128)
            print(self.Form.txtNuc.Texts)
            self.Form.labelObl6.Visible = True
            RJMessageBox.Show("No has colocado un NUC valido",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not noControlValidation.fullmatch(self.Form.txtNoControl.Texts):
            self.Form.txtNoControl.BorderColor = Color.FromArgb(255,128,128)
            self.Form.labelObl7.Visible = True
            RJMessageBox.Show("No has colocado un No. Control valido",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif not noOficioValidation.fullmatch(self.Form.txtNoOficioCumplimiento.Texts) and self.Form.txtNoOficioCumplimiento.Texts != "":
            self.Form.txtNoOficioCumplimiento.BorderColor = Color.FromArgb(255,128,128)
            RJMessageBox.Show("No has colocado un No. Oficio Cumplimiento valido",
                    "Faltan campos por seleccionar",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        elif dDiasEmiRec < 0:
            RJMessageBox.Show("La fecha de recepcion no puede ser antes de la fecha de emision",
                    "Fecha invalida",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);

        elif dDiasEmiCum < 0:
            RJMessageBox.Show("La fecha de cumplimentacion no puede ser antes de la fecha de emision",
                    "Fecha invalida",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
        else:
            return True
        return False
    
    def cbxStatus_OnSelectedIndexChanged(self, sender, e):
        item = str(sender.SelectedItem)

        if item == "CUMPLIMIENTADA":
            self.Form.dpFechaCumpli.Visible = True
            self.Form.lblFechaCum.Visible = True
        else:
            self.Form.dpFechaCumpli.Visible = False
            self.Form.lblFechaCum.Visible = False
    
    def getValues(self):
        date_fecha_init = self.Form.dpFechaEmi.Value.ToString("yyyy-MM-dd")
        date_fecha_end = self.Form.dpFechaCumpli.Value.ToString("yyyy-MM-dd")

        if self.Form.dpFechaCumpli.Visible:
            fecha_init = datetime.strptime(date_fecha_init,"%Y-%m-%d")
            fecha_end = datetime.strptime(date_fecha_end,"%Y-%m-%d")
            dDias = (fecha_end-fecha_init).days
        else: 
            date_fecha_end = "0001-01-01"
            dDias = -1

        semaforo = "R"
        if dDias > 0:
            if dDias <= 30: semaforo = "G"
            elif dDias <= 60: semaforo = "Y"

        data = {
            "base": dictBasesValues[self.Form.cbxDepto.SelectedItem], 
            "no_control": self.Form.txtNoControl.Texts, 
            "fecha_recibido": self.Form.dpFechaRec.Value.ToString("yyyy-MM-dd"),
            "fecha_emitido": date_fecha_init, 
            "agencia": dictAgenciaValues[self.Form.cbxAgencia.SelectedItem], 
            "nuc": self.Form.txtNuc.Texts,
            "clasificacion_hecho": dictClasificacionHechoValues[self.Form.cbxClasificacionHecho.SelectedItem],
            "status_": dictStatusValues[self.Form.cbxStatus.SelectedItem], 
            "no_oficio_cumplimiento": self.Form.txtNoOficioCumplimiento.Texts, 
            "colaboracion": self.Form.cbxColaboracion.SelectedItem, 
            "fecha_cumplimentacion": date_fecha_end, 
            "semaforo": semaforo
        }

        return data