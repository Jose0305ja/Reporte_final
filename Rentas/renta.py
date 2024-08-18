from ConexionBD import *
class Rentas:
    def __init__(self, servicio,fecha,hora,fechadev,cliente,empleado,camion):
        self.servicio=servicio
        self.fecha=fecha
        self.hora=hora
        self.fechadev=fechadev
        self.cliente=cliente
        self.empleado=empleado
        self.camion=camion
    
    def Crear(self):
        try:
            sql="INSERT INTO rentas (servicio,fecha,hora,fechadevolucion,cliente,empleado,camion) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            valor=(self.servicio,self.fecha,self.hora,self.fechadev,self.cliente,self.empleado,self.camion)
            cursor.execute(sql,valor)
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al agregar!")
    @staticmethod
    def Mostrar():
        try:
            cursor=conexion.cursor()
            sql="SELECT * FROM rentas"
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            messagebox.showinfo("Informacion",f"Error al realizar la consulta!")
            return []
    @staticmethod
    def Actualizar(id,nuevo_fecha):
        try:
            sql="UPDATE rentas SET fechadevolucion = %s  WHERE id_renta = %s"
            cursor.execute(sql,(nuevo_fecha,id))
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al actualizar!")
    @staticmethod
    def Eliminar(id):
        try:
            sql="DELETE FROM rentas WHERE id_renta = %s"
            cursor.execute(sql,id)
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al eliminar!")
    
    