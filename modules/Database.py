import clr

clr.AddReference('AMIC')
from System.Windows.Forms import *
from AMIC import RJMessageBox

import pyodbc
import sqlalchemy
import pandas as pd 
from models.User import User
from models.File import File

class Database:
    def __init__(self):
        self.conexion: pyodbc.Connection
        self.server = "DESKTOP-TO46N55"
        self.bd = "AMIC"
        self.user = "AMIC"
        self.password = "AMIC123"
        self.IsOn = False
        self.dfUsers: pd.DataFrame
        self.dfFiles: pd.DataFrame

        try:
            self.conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.bd+';UID='+self.user+';PWD='+self.password
            )
            print('Conexion exitosa')

            cursor = self.conexion.cursor()
            self.conexion.commit()

            self.dfUsers = pd.read_sql("SELECT * FROM Usuarios", self.conexion)
            cursor.close()        
            self.IsOn = True
        except:
            RJMessageBox.Show("Verifica si:\n 1. Tienes conexion con la base de datos\n 2. Tienes instalado el controlador ODBC Driver 17 for SQL Server",
                        "Error al conectar con la base de datos",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error)

    
    def create_Database(self):
        cursor = self.conexion.cursor()
        

    def User_Read(self):
        cursor = self.conexion.cursor()
        dfUsers = pd.read_sql("SELECT * FROM Usuarios", self.conexion)
        self.conexion.commit()
        cursor.close()
        return dfUsers

    def User_Count(self):
        cursor = self.conexion.cursor()
        query_tablas = f"SELECT COUNT(id) AS total FROM Usuarios GROUP BY username"
        dfFiles = pd.read_sql(query_tablas, self.conexion)
        self.conexion.commit()
        cursor.close()
        return int(dfFiles.iloc[:,0].sum())


    def File_Read(self):
        cursor = self.conexion.cursor()
        dfFiles = pd.read_sql("SELECT * FROM Expedientes", self.conexion)
        cursor.close()
        return dfFiles

    def User_Create(self, data: User):
        cursor = self.conexion.cursor()
        query = f"Insert INTO Usuarios VALUES {data.getValues()}"
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def File_Create(self, data: File):
        cursor = self.conexion.cursor()
        query = f"Insert INTO Expedientes VALUES {data.getValues()}"
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def User_Update(self, data: User,id: int):
        cursor = self.conexion.cursor()
        query = f"UPDATE Usuarios SET {data.getSet()} WHERE id= {id}" 
        print(query)
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def File_Update(self, data: File):
        cursor = self.conexion.cursor()
        query = f"UPDATE Expedientes SET {data.getSet()} WHERE id= {data.id}" 
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def User_Delete(self, id):
        cursor = self.conexion.cursor()
        query = f"DELETE FROM Usuarios WHERE id={id}" 
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def File_Delete(self, id):
        cursor = self.conexion.cursor()
        query = f"DELETE FROM Expedientes WHERE id={id}" 
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def File_SelectFilter(self, agencia, base, delitos,status):
        cursor = self.conexion.cursor()
        query_tablas = f"SELECT * FROM Expedientes WHERE agencia="+agencia+" AND base="+base+" AND delitos LIKE "+delitos+" AND status_="+status 
        dfUsers = pd.read_sql(query_tablas, self.conexion)
        self.conexion.commit()
        cursor.close()
        return dfUsers

    def File_SelectByDate(self,init: str, end: str):
        if init == end:
            query = f"SELECT * FROM Expedientes WHERE fecha_emitido = '{init}'" 
        elif init > end:
            query = f"SELECT * FROM Expedientes WHERE fecha_emitido BETWEEN '{end}' and '{init}'" 
        else:
            query = f"SELECT * FROM Expedientes WHERE fecha_emitido BETWEEN '{init}' and '{end}'" 

        cursor = self.conexion.cursor()
        dfFiles = pd.read_sql(query, self.conexion)
        self.conexion.commit()
        cursor.close()

        return dfFiles

        
    def select_Count(self,seleccion: str,contar: str, agrupar: str,init: str , end: str):
        cursor = self.conexion.cursor()
        query_tablas = f"SELECT {seleccion}, COUNT({contar}) AS count_{contar} FROM Expedientes WHERE fecha_emitido BETWEEN '{init}' and '{end}' GROUP BY {agrupar} "
        
        dfFiles = pd.read_sql(query_tablas, self.conexion)
        self.conexion.commit()
        cursor.close()
        return dfFiles

    def select_UsuarioPassword(self,user: str,contrasena: str):
        cursor = self.conexion.cursor()
        query_tablas = f"SELECT  * FROM Usuarios WHERE username = '{user}' and password = '{contrasena}'"
        
        dfFiles = pd.read_sql(query_tablas, self.conexion)
        self.conexion.commit()
        cursor.close()
        return dfFiles

    def select_Usuario(self,user: str):
        cursor = self.conexion.cursor()
        query_tablas = f"SELECT username FROM Usuarios WHERE username = '{user}'"
        dfFiles = pd.read_sql(query_tablas, self.conexion)
        self.conexion.commit()
        cursor.close()
        return dfFiles

    def Close(self):
        self.conexion.close()