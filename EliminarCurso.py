from cgitb import text
import tkinter
from tkinter import *
from tkinter import scrolledtext
from turtle import width
def Eliminar():
    #VENTANA
    ventanadelete = tkinter.Tk()
    ventanadelete.title("Eliminar Curso")
    ventanadelete.geometry("600x200")
    ventanadelete.config(bg="sky blue")
    ventanadelete.resizable(0,0)
    #ETIQUETA
    lblCodigoCurso= Label(ventanadelete,text="Código de Curso",font="Cambria 22",fg="#9625b7", bg="sky blue")
    lblCodigoCurso.place(x=10,y=10)
    #ESPACIOS PARA ESCRIBIR
    Entrada=StringVar
    txtRuta=Entry(ventanadelete,textvariable=Entrada,font="Cambria 22", fg="gray").place(x="230",y="20",width="350",height="30")

    #BOTONES
    botoneliminar = Button(ventanadelete,text="Eliminar", font="Cambria 22",  fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botoneliminar.place(x=200,y=80)
    botonregresoeliminar = Button(ventanadelete,text="Regresar", font="Cambria 22",  fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonregresoeliminar.place(x=400,y=80)
    ventanadelete.mainloop()
Eliminar()