import clr

clr.AddReference('AMIC')

import numpy as np
import pandas as pd
from System.Windows.Forms import *
from AMIC import frmStats, RJMessageBox
from datetime import datetime
from classes.Form import Form
from modules.Database import Database
from modules.ModuleEstadisticas import *
from modules.Reports import *
from modules.Dicts import *

class FileStats(Form):
    
    def __init__(self, db: Database):
        self.db = db
        self.Form = frmStats()
                
        self.dateInit = self.Form.dpInicio.Value.ToString("yyyy-MM-dd")
        self.dateEnd = self.Form.dpEnd.Value.ToString("yyyy-MM-dd")

        self.father: Form
        
        self.Form.dpInicio.ValueChanged += self.datePickers_ValueChanged
        self.Form.dpEnd.ValueChanged += self.datePickers_ValueChanged
        self.Form.cbxSelect.OnSelectedIndexChanged += self.cbxSelect_OnSelectedIndexChanged
        self.getStats()
        self.carga_Form()
        self.Form.btnPrint.Click += self.btnPrint_Click
        #self.Form.Load += self.form_load
        
    def btnPrint_Click(self, sender, e):
        report = Reports()
        report.createWorkbook()
        report.createSheet(f"De {self.dateInit} a {self.dateEnd}")
        report.createSheet("Delitos")
        report.createSheet("Semaforo")
        report.createSheet("Status")

        dataFecha = []
        df = self.dfFechas
        df = df.rename(columns={"Num_delitoss":"Total de casos","Fecha de emision":"Delito"})
        dataFecha.append(df.columns.tolist())
        dataFecha += df.values.tolist()

        dataDelitos = []
        df = self.dfDelitos
        df["Name"] = list(df.index)
        df["Name"] = df["Name"].map(getValueDelitos)
        df = df.reindex(columns=["Name","total"])
        df = df.rename(columns={"total":"Total de casos","Name":"Delito"})
        dataDelitos.append(df.columns.tolist())
        dataDelitos += df.values.tolist()

        dataSemaforo = []
        df = self.dfSemaforo
        df["KEY"] = df["KEY"].map(getValueSemaforo)
        df = df.rename(columns={"VALUES":"Total de casos","KEY":"Semaforo"})
        dataSemaforo.append(df.columns.tolist())
        dataSemaforo += df.values.tolist()
        
        dataStatus = []
        df = self.dfStatus.to_frame()
        df["Name"] = list(df.index)
        df["Name"] = df["Name"].map(getValueStatus)
        df = df.reindex(columns=["Name","status_"])
        df = df.rename(columns={"status_":"Total de casos","Name":"Status"})
        dataStatus.append(df.columns.tolist())
        dataStatus += df.values.tolist()
        
        report.writeDataIn(f"De {self.dateInit} a {self.dateEnd}",dataFecha, True)
        report.writeDataIn("Delitos",dataDelitos, True)
        report.writeDataIn("Semaforo",dataSemaforo, False)
        report.writeDataIn("Status",dataStatus, False)
        if report.saveWorkbook():
            RJMessageBox.Show("Reporte guardado correctamente",
                    "Reporte guardado correctamente",
                    MessageBoxButtons.OK);


    def getStats(self):
        self.dateInit = f"{datetime.now().year}-01-01"
        df = self.db.File_SelectByDate(self.dateInit,self.dateEnd)
        self.dfFechas = select_FechaDelitos(self.db,self.dateInit,self.dateEnd)
        self.dfSemaforo = df.groupby(["semaforo"])["semaforo"].count()
        self.dfStatus = df.groupby(["status_"])["status_"].count()
        self.dfDelitos = select_CountDelitos(self.db,self.dateInit,self.dateEnd)
        self.dfDelitos = pd.DataFrame({"delitos":self.dfDelitos.keys(),"total":self.dfDelitos.values()})
        self.dfDelitos = self.dfDelitos.set_index("delitos")
        self.dfTop = self.dfDelitos.sort_values("total",ascending=False)
        dfTop10 = self.dfTop.iloc[9:,:]["total"].sum()
        self.dfTop = self.dfTop.iloc[:9,:]
        self.dfTop.loc["Otros"] = [dfTop10]
        
    def carga_Form(self):
        self.form_Graficas(self.db.select_Count("fecha_emitido","status_","fecha_emitido",self.dateInit,self.dateEnd), 
                           select_FechaDelitos(self.db,self.dateInit,self.dateEnd))
    
    #def form_load(self,sender,e):
        #self.carga_Form(self)
        
        
    def form_Graficas(self,dfFiles: pd.DataFrame,dfFiles_Dias: pd.DataFrame ):
        if dfFiles.empty == False:
            
            self.ChartDias_Load(dfFiles)
            nuevo = np.array(dfFiles_Dias["fecha_emitido"])
            num = np.array(dfFiles_Dias["Num_delitoss"])
            fechas = []
            num_Delitos = []
            
            for n in nuevo:
                fechas.append(n.strftime("'%Y-%m-%d'"))
            for n in num:
                num_Delitos.append(int(n))
            
            self.Form.Fecha = fechas
            self.Form.NumDelitos = num_Delitos   
                     
            self.Form.datagrid_Datos.Rows.Clear()
            top10 = select_CountDelitos(self.db,self.dateInit,self.dateEnd)
                        
            top10 = pd.DataFrame([[key, top10[key]] for key in top10.keys()], columns=['delito','cantidad'])
            top10["delito"] = top10["delito"].map(getValueDelitos)
            print(top10)

            if top10.empty == False:
                top10 = top10.sort_values('cantidad', ascending=False)
                if  top10.shape[0] >= 10:
                    top10_delitos = np.array(top10.iloc[0:9,1])
                    otros_delitos = top10.iloc[9:,1].sum()
                    top10_delitos = np.append(top10_delitos, otros_delitos)
                    top_10 = np.array(top10.iloc[0:9,0])
                    top_10 = np.append(top_10,'Otros')
                    cantidad_del = []         
                                   
                    for n in top10_delitos:
                        cantidad_del.append(int(n))
                        
                    top10_dt = {'Top': list(range(1, 11)), 'Delito': top_10, 'Cantidad de Delitos': cantidad_del}
                    top10_dt = pd.DataFrame(top10_dt)
                    
                    self.dataGrid_Load(top10_dt)
                    self.Form.Nom_Delitos = top_10
                    self.Form.Cantidad_Del = cantidad_del
                    
                else:
                    top10_delitos = np.array(top10.iloc[0:,1])
                    top_10 = np.array(top10.iloc[0:,0])
                    cantidad_del = []
                             
                    for n in top10_delitos:
                        cantidad_del.append(int(n))
                    
                    tamano = np.arange(0,len(top10_delitos))
                    for n in tamano:
                        tamano[n] = n+1
                    
                    print(tamano)
                    top10_dt = {'Top': tamano, 'Delito': top_10, 'Cantidad de Delitos': cantidad_del}
                    top10_dt = pd.DataFrame(top10_dt)
                    
                    self.dataGrid_Load(top10_dt)
                    self.Form.Nom_Delitos = top_10
                    self.Form.Cantidad_Del = cantidad_del
                        
    def dataGrid_Load(self, dfFile: pd.DataFrame):
        dataGridView = dataFrameToList(dfFile)
        self.Form.datagrid_Datos.Columns.Clear()
        self.Form.datagrid_Datos.Rows.Clear()
        
        for n in dfFile.columns:
            self.Form.datagrid_Datos.Columns.Add(str(n),str(n))
          
        for fila in dataGridView:
            self.Form.datagrid_Datos.Rows.Add(fila)
            
            
    def ChartDias_Load(self,dfFiles: pd.DataFrame):
        total = select_Total(self.db,self.dateInit,self.dateEnd)
        self.Form.lblTotalDelitos.Text = str(total)
        self.Form.lblTotalExpedientes.Text = str(self.dfTop["total"].sum())

        self.Form.chart_Semaforo.Series.Clear()
        self.Form.series_ChartSemaforo.Points.Clear()
        
        if dfFiles.shape[0] == 1:
            pointA = int(int(dfFiles.iloc[0,1])*100/total)
            pointB = 0
            pointC = 0
            
        elif dfFiles.shape[0] == 2:
            pointA = int(int(dfFiles.iloc[0,1])*100/total)
            pointB = int(int(dfFiles.iloc[1,1])*100/total)
            pointC = 0
        
        else:
            pointA = int(int(dfFiles.iloc[0,1])*100/total)
            pointB = int(int(dfFiles.iloc[1,1])*100/total)
            pointC = int(int(dfFiles.iloc[2,1])*100/total)
            
        if self.Form.cbxSelect.Texts == "Semaforo":
            dataSemaforo = {
                'KEY':['Verde','Amarillo','Rojo'],
                'VALUES':[pointA,pointB,pointC]
            }
            self.Form.legend1 = "Verde"
            self.Form.color1 = "Green"
            self.Form.legend2 = "Amarillo"
            self.Form.color2 = "Yellow"
            self.Form.legend3 = "Rojo"
            self.Form.color3 = "Red"
        else:
            dataSemaforo = {
                'KEY':['S01','S02','S03'],
                'VALUES':[pointA,pointB,pointC]
            }
            self.Form.legend1 = "Cumplimenteada"
            self.Form.color1 = "Teal"
            self.Form.legend2 = "En tramite"
            self.Form.color2 = "Orange"
            self.Form.legend3 = "No cumplimentada"
            self.Form.color3 = "Tomato"
            
        
        self.Form.Point_S01=pointA
        self.Form.Point_S02=pointB
        self.Form.Point_S03=pointC    
        self.dfSemaforo = pd.DataFrame(dataSemaforo)
        
    #validacion
    def datePickers_ValueChanged(self,sender, e):
        self.dateInit = self.Form.dpInicio.Value.ToString("yyyy-MM-dd")
        self.dateEnd = self.Form.dpEnd.Value.ToString("yyyy-MM-dd")

        self.getStats()

        self.form_Graficas(self.db.select_Count("status_","status_","status_",self.dateInit,self.dateEnd), 
                           select_FechaDelitos(self.db,self.dateInit,self.dateEnd))

        
    def cbxSelect_OnSelectedIndexChanged(self,sender, e):
        if self.Form.cbxSelect.Texts == "Semaforo":
            self.form_Graficas(self.db.select_Count("semaforo","semaforo","semaforo",self.dateInit,self.dateEnd), 
                           select_FechaDelitos(self.db,self.dateInit,self.dateEnd))
            
        else:    
            self.form_Graficas(self.db.select_Count("status_","status_","status_",self.dateInit,self.dateEnd), 
                           select_FechaDelitos(self.db,self.dateInit,self.dateEnd))
            
