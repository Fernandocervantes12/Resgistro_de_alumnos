import sqlite3

from colorama import Cursor

class alumnos:
  def abrir(self):
        conexion=sqlite3.connect("COMUNIDAD_UNID.db")
        return conexion

  def alta(self,datos):
    try:
      cone=self.abrir()
      print("hasta aqui bien")
      cursor=cone.cursor()
      print("hasta aqui bien")
      sql="INSERT INTO alumno (correo,contraseña,nombre,apellido,edad) values (?,?,?,?,?)"
      cursor.execute(sql,datos)
    except:
      return "error"
    finally:
      cone.commit()
      cone.close()
    
  def consultasql(self,datos):
      try:
        cone=self.abrir()
        print("hasta aqui todo bien")
        cursor=cone.cursor()
        print("aqui estoy amigo")
        sql="SELECT * FROM alumno WHERE correo = ?"
        cursor.execute(sql,[datos])
        return cursor.fetchall()
      finally:
       cone.close()
  
  def borrar(self,datos):
    try:
      cone=self.abrir()
      print("vamos bien")
      cursor=cone.cursor()
      sql="DELETE FROM alumno WHERE correo = ?"
      cursor.execute(sql,[datos])
      return cursor.fetchall()
    except: 
      return "error"
    finally:
        cone.commit()
        cone.close()




      