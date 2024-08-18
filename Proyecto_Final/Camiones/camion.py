from ConexionBD import *

class Camiones:
    def __init__(self, tipo_camion,color,conductor):
        self.tipo_camion=tipo_camion
        self.color=color
        self.conductor=conductor

    def Crear(self):
        try:
                sql="INSERT INTO camiones (tipo_camion,color,conductor) VALUES (%s,%s,%s)"
                valor=(self.tipo_camion,self.color,self.conductor)
                cursor.execute(sql,valor)
                conexion.commit()
                return True
        except:
            messagebox.showinfo("Informacion",f"Error al agregar!")
            return False
    
    @staticmethod
    def Mostrar():
        try:
            sql="SELECT * FROM camiones"
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            messagebox.showinfo("Informacion",f"Error al realizar la consulta!")
            return[]
    @staticmethod
    def Actualizar(id,nuevo_conductor):
        try:
                sql="UPDATE camiones SET conductor = %s WHERE id_camion = %s"
                cursor.execute(sql,(nuevo_conductor,id))
                conexion.commit()
                return True
        except:
            messagebox.showinfo("Informacion",f"Error al actualizar!")
            return False
    @staticmethod
    def Eliminar(id):
        try:
            sql="DELETE FROM camiones WHERE id_camion = %s"
            cursor.execute(sql,id)
            conexion.commit()
            return True
        except:
            messagebox.showinfo("Informacion",f"Error al eliminar!")
            return False
    
  