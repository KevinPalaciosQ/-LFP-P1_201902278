import tkinter
from tkinter import *
def Gestionar():
    #VENTANA
    ventanacurso = tkinter.Tk()
    ventanacurso.title("Gestionar")
    ventanacurso.geometry("900x600")
    ventanacurso.config(bg="aqua")
    ventanacurso.resizable(0,0)
    #BOTONES----------------------------------------
    #BOTON PARA LISTAR CURSOS  
    botonlistar= Button(ventanacurso,text="Listar",fon="arial 20", fg="blue", bg="yellow green")
    botonlistar.place(x=300,y=50)
    #BOTON PARA AGREGAR CURSO
    botonagregar= Button(ventanacurso,text="Agregar Curso",fon="arial 20", fg="blue", bg="yellow green",anchor="center")
    botonagregar.place(x=300,y=110)
    #BOTON PARA EDITAR CURSO
    botoneditar= Button(ventanacurso,text="Editar Curso",fon="arial 20", fg="blue", bg="yellow green")
    botoneditar.place(x=300,y=170)
    #BOTON PARA ELIMINAR CURSO
    botoneliminar= Button(ventanacurso,text="Eliminar Curso",fon="arial 20", fg="blue", bg="yellow green")
    botoneliminar.place(x=300,y=230)
    #BOTON PARA REGRESAR
    botonregresar= Button(ventanacurso,text="Regresar",fon="arial 20", fg="blue", bg="yellow green")
    botonregresar.place(x=300,y=290)
    ventanacurso.mainloop()