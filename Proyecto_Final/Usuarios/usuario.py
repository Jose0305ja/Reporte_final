from ConexionBD import *
import hashlib
class Usuarios:
    def __init__(self,nombre,apellido,usuario,contraseña,rol,empleado):
        self.nombre=nombre
        self.apellido=apellido
        self.usuario=usuario
        self.contraseña=contraseña
        self.rol=rol
        self.empleado=empleado

    def Crear(self):
        try:
            contraseña=self.contraseña
            # Encriptar la contraseña usando SHA-256
            hashed_password = hashlib.sha256(contraseña.encode('utf-8')).hexdigest()
            cursor=conexion.cursor()
            sql="INSERT INTO usuarios (nombre,apellido,usuario,password,rol,empleado) VALUES (%s,%s,%s,%s,%s,%s)"
            valor=(self.nombre,self.apellido,self.usuario,hashed_password,self.rol,self.empleado)
            cursor.execute(sql,valor)
            conexion.commit()
        except:
            messagebox.showinfo("Informacion",f"Error al registrar usuario... Intentelo mas tarde...")

    @staticmethod
    def Iniciar(usuario,password):
        try:
            cursor=conexion.cursor()
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND password = %s", (usuario,hashed_password))
            resultados=cursor.fetchone()
            if resultados:
                return resultados
            else:
                return []
        except:
            messagebox.showinfo("Informacion",f"Error al iniciar sesion... Intentelo mas tarde...")