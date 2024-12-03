"""
Prueba sencilla para conectar con una BD de SQLite3
"""

import sqlite3 as db
from os.path import isfile
import pandas as pd


def listarTablaPandas(path, nombreTabla):
    if isfile(path):
        # El fichero de la BD existe
        
        # Abrir una conexion:
        con = db.connect(path)
        sql = f"select * from {nombreTabla}"

        df = pd.read_sql(sql, con)
        print(df.head())
        df.to_json("empleados.json", orient="records")
        con.close()

    else:
        print("El fichero no existe")


def listarTabla(path, nombreTabla):
    """
    Lista el contenido de una tabla de la BD
    """
    if isfile(path):
        # El fichero de la BD existe
        
        # Abrir una conexion:
        con = db.connect(path)
        cur = con.cursor()
        sql = f"select * from {nombreTabla}"
        cur.execute(sql)

        for fila in cur.fetchall():
            print(fila)

        cur.close()
        con.close()

    else:
        print("El fichero no existe")


listarTablaPandas("empresa3.db", "empleados")
