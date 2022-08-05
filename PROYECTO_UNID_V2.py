
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import Alumnos as a

class Comunidad:
    def __init__(self):
        self.alumno1=a.alumnos()
        self.root=tk.Tk()
        self.root.title("SISTEMA DE REGISTRO DE ALUMNOS UNID") 
        self.root.resizable(0,0)
        self.root.iconbitmap('logounid.ico')
        self.correo=tk.StringVar()
        self.contraseña=tk.StringVar()
        self.nombre=tk.StringVar()
        self.apellido=tk.StringVar()
        self.edad=tk.StringVar()
        self.consultas=tk.IntVar()
        self.bajas=tk.IntVar()
        self.cuaderno1 = ttk.Notebook(self.root) 
       

      
        

        self.INICIO()
        self.editar()
        
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.root.mainloop()

    def INICIO(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="REGISTRO")
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="Inicio")
        self.labelframe1.grid(column=0, row=0 ,pady=5, padx=10)

        self.label1=ttk.Label(self.labelframe1,text='Correo' , font=("Arial",12))
        self.label1.grid(row=0, column=0,padx=5,pady=5,sticky='w')
        self.entry1=ttk.Entry(self.labelframe1,justify='center', width=40,textvariable=self.correo)
        self.entry1.grid(row=0,column=1,padx=10,pady=10)

        self.label2=ttk.Label(self.labelframe1,text='Contraseña', font=('Arial',12))
        self.label2.grid(row=1, column=0,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe1,justify='center',show='*',width=34,textvariable=self.contraseña)
        self.entry2.grid(row=1,column=1,padx=10,pady=10)

        self.label2=ttk.Label(self.labelframe1,text='Nombre', font=('Arial',12))
        self.label2.grid(row=2, column=0,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe1,justify='center',width=34,textvariable=self.nombre)
        self.entry2.grid(row=2,column=1,padx=10,pady=10)
        
        self.label2=ttk.Label(self.labelframe1,text='Apellido', font=('Arial',12))
        self.label2.grid(row=3, column=0,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe1,justify='center',width=34,textvariable=self.apellido)
        self.entry2.grid(row=3,column=1,padx=10,pady=10)
        
        self.label2=ttk.Label(self.labelframe1,text='Edad', font=('Arial',12))
        self.label2.grid(row=4, column=0,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe1,justify='center',width=34,textvariable=self.edad)
        self.entry2.grid(row=4,column=1,padx=10,pady=10)

      
        self.boton1=ttk.Button(self.labelframe1, text='Guardar',command=self.guardar)
        self.boton1.grid(row=5,column=0,padx=14,pady=14)
        self.boton2=ttk.Button(self.labelframe1, text='Salir',command=self.salir)
        self.boton2.grid(row=5 ,column=1,padx=15,pady=15)
        self.boton3=ttk.Button(self.labelframe1,text='Borrar',command=self.borrar)
        self.boton3.grid(row=5 ,column=2,padx=15,pady=15)    
        

        

    def guardar(self):
        datos=(self.correo.get(),self.contraseña.get(),self.nombre.get(),self.apellido.get(),self.edad.get())
        respuesta=self.alumno1.alta(datos)
        if respuesta=="error":
            messagebox.showinfo("Información", "Ya existe el registro")
        else:
            messagebox.showinfo("Información", "Registro guardado")
            self.borrar()

    def consulta(self):
        datos=(self.correo.get())
        respuesta=self.alumno1.consultasql(datos)
        if len(respuesta)>0:
            self.contraseña.set(respuesta[0][2])
            self.nombre.set(respuesta[0][3])
            self.apellido.set(respuesta[0][4])
            self.edad.set(respuesta[0][5])
        else:
            self.borrar()
            messagebox.showinfo("Información", "No existe el registro")
    
    def eliminarR(self):
        datos=(self.correo.get())
        respuesta=self.alumno1.borrar(datos)
        if respuesta=="error":
            messagebox.showinfo("Información", "No existe el registro")
        else:
            self.borrar()
            messagebox.showinfo("Información", "Registro eliminado")
   

    def borrar(self):
        self.correo.set("")
        self.contraseña.set("")
        self.nombre.set("")
        self.apellido.set("")
        self.edad.set("")

    def salir(self):
        self.root.quit()

   
    def editar(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Modificar")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Editar base de datos")
        self.labelframe2.grid(column=0, row=0, padx=2, pady=2)

        self.label2=ttk.Label(self.labelframe2,text='Correo', font=('Arial',12))
        self.label2.grid(row=0, column=1,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe2,justify='center',width=34,textvariable=self.correo)
        self.entry2.grid(row=0,column=2,padx=10,pady=10)

        self.label2=ttk.Label(self.labelframe2,text='Contraseña', font=('Arial',12))
        self.label2.grid(row=1, column=1,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe2,justify='center',width=34,textvariable=self.contraseña,state="disable")
        self.entry2.grid(row=1,column=2,padx=10,pady=10)

        self.label2=ttk.Label(self.labelframe2,text='Nombre', font=('Arial',12))
        self.label2.grid(row=2, column=1,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe2,justify='center',width=34,textvariable=self.nombre,state="disable")
        self.entry2.grid(row=2,column=2,padx=10,pady=10)
        
        self.label2=ttk.Label(self.labelframe2,text='Apellido', font=('Arial',12))
        self.label2.grid(row=3, column=1,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe2,justify='center',width=34,textvariable=self.apellido,state="disable")
        self.entry2.grid(row=3,column=2,padx=10,pady=10)
        
        self.label2=ttk.Label(self.labelframe2,text='Edad', font=('Arial',12))
        self.label2.grid(row=4, column=1,padx=5,pady=5,sticky='w')
        self.entry2=ttk.Entry(self.labelframe2,justify='center',width=34,textvariable=self.edad,state="disable")
        self.entry2.grid(row=4,column=2,padx=10,pady=10)


        self.boton10=ttk.Button(self.labelframe2, text='Buscar',command=self.consulta)
        self.boton10.grid(row=7,column=0,padx=14,pady=14)
        self.boton20=ttk.Button(self.labelframe2, text='Borrar',command=self.eliminarR)
        self.boton20.grid(row=7 ,column=1,padx=15,pady=15)

    

            
   
aplicacion1=Comunidad()