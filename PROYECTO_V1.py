from tkinter import *
import Alumnos as a 

class comunidad:  
    def __init__(self):
        self.alumno1=a.alumnos()
        self.root=Tk()
        self.root.title("Comunidad UNID")
        self.root.resizable(0,0)
        self.root.iconbitmap('logounid.ico')
        self.root.geometry("550x450")

        self.correo=StringVar()
        self.contraseña=StringVar()
        menubar=Menu(self.root)
        self.root.config(menu=menubar, background="lightgray")

        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label="iniciar")
        filemenu.add_command(label="guardar cambios")
        filemenu.add_separator()
        filemenu.add_command(label="cerrar")

        helpmenu=Menu(menubar, tearoff=0)
        helpmenu.add_command(label='ayuda')
        helpmenu.add_command(label='acerca de...')

        menubar.add_cascade(label="ARCHIVO", menu=filemenu)
        menubar.add_cascade(label="AYUDA", menu=helpmenu)

        Label(self.root,text='Correo' , background="lightgray", font=("Arial",12)).grid(row=0, column=0,padx=5,pady=5,sticky='w')
        Entry(self.root,justify='center', width=40,textvariable=self.correo).grid(row=0,column=1,padx=10,pady=10)

        Label(self.root,text='Contraseña',background='lightgray', font=('Arial',12)).grid(row=1, column=0,padx=5,pady=5,sticky='w')
        Entry(self.root,justify='center',show='*',width=34,textvariable=self.contraseña).grid(row=1,column=1,padx=10,pady=10)

        Button(self.root,command=self.guardar, text='Guardar',bg='lightblue',width=8,height=2,font=('Calibri',12)).grid(row=0,column=3,padx=15,pady=15)
        Button(self.root, command=self.salir ,text='Salir',bg='lightblue',width=8,height=2,font=('Calibri',12)).grid(row=1 ,column=3,padx=15,pady=15)
        Button(self.root, command=self.borrar ,text='Borrar',bg='lightblue',width=12,height=2,font=('Calibri',12)).grid(row=2 ,column=3,padx=15,pady=15)
        self.root.mainloop()

    def guardar(self):
        datos=(self.correo.get(),self.contraseña.get())
        self.alumno1.alta(datos)
        self.borrar()

    
    def borrar(self):
        self.correo.set("")
        self.contraseña.set("")

    def salir(self):
        self.root.quit()

        

aplicacion=comunidad()
