from ConexionBD import *
class Empleados:
    def __init__(self, nombre,apellido,puesto):
        self.nombre=nombre
        self.apellido=apellido
        self.puesto=puesto
    
    def Crear(self):
        try:
            sql="INSERT INTO empleados (nombre,apellido,puesto) VALUES (%s,%s,%s)"
            valor=(self.nombre,self.apellido,self.puesto)
            cursor.execute(sql,valor)
            conexion.commit() 
        except:
            messagebox.showinfo("Informacion",f"Error al agregar!")
    @staticmethod
    def Mostrar():
        try:
            cursor=conexion.cursor()
            sql="SELECT * FROM empleados"
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            messagebox.showinfo("Informacion",f"Error al realizar la consulta!")
            return []
    @staticmethod
    def Actualizar(id,nuevo_puesto):
        try:
            sql="UPDATE empleados SET puesto = %s  WHERE id_empleado = %s"
            cursor.execute(sql,(nuevo_puesto,id))
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al actualizar!")
    @staticmethod
    def Eliminar(id):
        try:
            sql="DELETE FROM empleados WHERE id_empleado = %s"
            cursor.execute(sql,id)
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al eliminar!")

    