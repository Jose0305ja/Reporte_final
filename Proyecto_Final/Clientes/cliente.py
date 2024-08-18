from ConexionBD import *
class Clientes:
    def __init__(self,nombre,apellido,direccion,telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.telefono=telefono

    def Crear(self):
        try:
            sql="INSERT INTO clientes (nombre,apellido,direccion,telefono) VALUES (%s,%s,%s,%s)"
            valor=(self.nombre,self.apellido,self.direccion,self.telefono)
            cursor.execute(sql,valor)
            conexion.commit()
            return True
        except:
            messagebox.showinfo("Informacion",f"Error al agregar!")
            return False
        
    @staticmethod
    def Mostrar():
        try:
                cursor=conexion.cursor()
                sql="SELECT * FROM clientes"
                cursor.execute(sql)
                return cursor.fetchall()
        except:
            messagebox.showinfo("Informacion",f"Error al realizar la consulta!")
            return []
        
    @staticmethod
    def Actualizar(id,nuevo_direccion,nuevo_tel):
        try:
            sql="UPDATE clientes SET direccion = %s ,telefono=%s WHERE id_cliente = %s"
            cursor.execute(sql,(nuevo_direccion,nuevo_tel,id))
            conexion.commit()
            
        except:
            messagebox.showinfo("Informacion",f"Error al actualizar!")
    @staticmethod
    def Eliminar(id):
        try:
            sql="DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(sql,id)
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al eliminar!")
    
    