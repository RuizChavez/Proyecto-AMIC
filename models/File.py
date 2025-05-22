from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey

Base = declarative_base()

class File():
    
    def __init__(self,base, ncontrol, fecha_recibido, fecha_emision, agencia, nuc, delito, clasificacion_hecho,
                 imputado, ofendido, status, no_oficio_cumplimiento, colaboracion, fecha_cumplimentacion, semaforo):
        self.base = base
        self.ncontrol = ncontrol
        self.fecha_recibido = fecha_recibido
        self.fecha_emision = fecha_emision
        self.agencia = agencia
        self.nuc = nuc
        self.delito = delito
        self.clasificacion_hecho = clasificacion_hecho
        self.imputado = imputado
        self.ofendido = ofendido
        self.status = status
        self.no_oficio_cumplimiento = no_oficio_cumplimiento
        self.colaboracion = colaboracion
        self.fecha_cumplimentacion = fecha_cumplimentacion
        self.semaforo = semaforo
        self.id = 0

    def getValues(self):
        return f'''(\'{self.base}\', \'{self.ncontrol}\', \'{self.fecha_recibido}\', \'{self.fecha_emision}\', 
            \'{self.agencia}\', \'{self.nuc}\', \'{self.delito}\', \'{self.clasificacion_hecho}\', \'{self.imputado}\',
            \'{self.ofendido}\', \'{self.status}\', \'{self.no_oficio_cumplimiento}\', \'{self.colaboracion}\', 
            \'{self.fecha_cumplimentacion}\', \'{self.semaforo}\')'''
    
    def getSet(self):
        return f'''base= \'{self.base}\', no_control= \'{self.ncontrol}\', fecha_recibido= \'{self.fecha_recibido}\',
            fecha_emitido= \'{self.fecha_emision}\', agencia= \'{self.agencia}\', nuc= \'{self.nuc}\', delitos= \'{self.delito}\',
            clasificacion_hecho= \'{self.clasificacion_hecho}\', imputados= \'{self.imputado}\', ofendidos=\'{self.ofendido}\',
            status_= \'{self.status}\', no_oficio_cumplimiento= \'{self.no_oficio_cumplimiento}\', colaboracion= \'{self.colaboracion}\', 
            fecha_cumplimentacion= \'{self.fecha_cumplimentacion}\', semaforo=\'{self.semaforo}\''''
