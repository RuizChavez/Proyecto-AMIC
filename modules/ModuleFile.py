from models.File import File
from modules.Database import Database

def Create(bd: Database, data):
    file = File(data["base"],data["no_control"],data["fecha_recibido"],
                data["fecha_emitido"],data["agencia"], data["nuc"], data["delitos"], 
                data["clasificacion_hecho"],data["imputados"],data["ofendidos"], 
                data["status_"],data["no_oficio_cumplimiento"],data["colaboracion"], 
                data["fecha_cumplimentacion"], data["semaforo"])
    
    bd.File_Create(file)

def Update(bd: Database, id, file):
    file.id = id    
    bd.File_Update(file)