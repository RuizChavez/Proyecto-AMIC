import pyodbc
import sqlalchemy
import pandas as pd 
import pprint as pp


from modules.Database import Database

def select_Where(db: Database, fecha: str):
    cursor = db.conexion.cursor()
    query_tablas = f"SELECT {fecha} FROM Expedientes"
    print(query_tablas)
    cursor.execute(query_tablas)
    db.conexion.commit()
    dfEst = pd.read_sql(query_tablas, db.conexion)
    print(dfEst)
    cursor.close()

def select_GraficaDias(db: Database, seleccion:str, contar: str, fecha: str, fecha_inicial: str):
    cursor = db.conexion.cursor()
    query_tablas = f"SELECT {seleccion}, COUNT({contar}) FROM Expedientes WHERE {fecha} = '{fecha_inicial}' GROUP BY {contar}"  
    dfFiles = pd.read_sql(query_tablas, db.conexion)
    cursor.close()
    return dfFiles

def select_Total(db: Database, init,end):
    cursor = db.conexion.cursor()
    query_tablas = f"SELECT COUNT(id) AS total FROM Expedientes WHERE  fecha_emitido BETWEEN '{init}' and '{end}' GROUP BY fecha_emitido"
    dfFiles = pd.read_sql(query_tablas, db.conexion)
    cursor.close()
    return int(dfFiles.iloc[:,0].sum())


def select_GroupBy(db: Database, seleccion: str, agrupar: str):
    cursor = db.conexion.cursor()
    query_tablas = f"SELECT {seleccion} FROM Expedientes GROUP BY {agrupar}"
    print(query_tablas)
    cursor.execute(query_tablas)
    db.conexion.commit()
    dfEst = pd.read_sql(query_tablas, db.conexion)
    cursor.close()
    

def select_Date(db: Database, seleccion: str,contar: str,fecha: str, fecha_inicial: str, fecha_final: str, agrupar: str):
    cursor = db.conexion.cursor()
    
    if(contar != ""):
        query_tablas = f"SELECT {seleccion},COUNT({contar}) FROM Expedientes WHERE {fecha} BETWEEN {fecha_inicial} and {fecha_final} GROUP BY {seleccion}"
    
    if (fecha_final == ""):
        query_tablas = f"SELECT {seleccion} FROM Expedientes WHERE {fecha} = {fecha_inicial}"
    else: 
        query_tablas = f"SELECT {seleccion} FROM Expedientes WHERE {fecha} BETWEEN {fecha_inicial} and {fecha_final}"
    
    dfFiles = pd.read_sql(query_tablas, db.conexion)
    cursor.close()
    return dfFiles

dic = {}
def count_delitos(x:str):
    if x.__contains__(','):
        x = x.split(',')
    else:
        x = [x]

    for y in x:
        if dic.keys().__contains__(y):
            dic[y] += 1
        else:
            dic.setdefault(y,1)
    return x


def select_FechaDelitos(db: Database, fecha_inicial: str, fecha_final: str):
    query_tablas = f"SELECT fecha_emitido ,COUNT(fecha_emitido) AS Num_delitoss FROM Expedientes WHERE fecha_emitido BETWEEN '{fecha_inicial}' and '{fecha_final}' GROUP BY fecha_emitido"
    cursor = db.conexion.cursor()
    dfFiles = pd.read_sql(query_tablas, db.conexion)
    cursor.close()
    print(query_tablas)
    return dfFiles


def select_CountDelitos(db: Database, init: str, end: str):
    query_tablas = f"SELECT delitos FROM Expedientes WHERE fecha_emitido BETWEEN '{init}' and '{end}'"
    cursor = db.conexion.cursor()
    dfFiles = pd.read_sql(query_tablas, db.conexion)
    cursor.close()
    dic.clear()
    pd.Series(dfFiles['delitos']).map(count_delitos)
    return dic


def dataFrameToList(df: pd.DataFrame):
    dataList = []

    columns = df.columns

    for i, row in df.iterrows():
        rowList = []
        for column in columns:
            rowList.append(row[column])
        dataList.append(rowList)
    
    return dataList