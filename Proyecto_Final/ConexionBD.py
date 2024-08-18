from tkinter import *
from tkinter import messagebox
import mysql.connector
try: 
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="camiones"
    )
    cursor = conexion.cursor(buffered=True)
except:
    messagebox.showinfo("Informacion",f"Error al conectar la base de datos mysql!")



