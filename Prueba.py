from ast import Lambda
from optparse import Option
from re import A
import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import filedialog
from types import NoneType
def Mostrar():
    global ventanacurso
    global ventanaeditar
    #ventanacurso.destroy()
    #VENTANA
    ventanaeditar = tkinter.Tk()
    ventanaeditar.title("Mostrar Curso en Específico")
    ventanaeditar.geometry("900x450")
    ventanaeditar.config(bg="sky blue")
    ventanaeditar.iconbitmap("favicon.ico")
    ventanaeditar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonback = Button(ventanaeditar,text="Regresar",fon="arial 20" ,fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonback.place(x=720,y=350)
    #BOTON PARA AGREGAR
    botonshow = Button(ventanaeditar,text="Mostrar",fon="arial 20", fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonshow.place(x=560,y=350)
    #ETIQUETAS
    lblcodigo= Label(ventanaeditar,text="Código",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcodigo.place(x=10,y=10)
    lblnombre= Label(ventanaeditar,text="Nombre",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombre.place(x=10,y=45)
    lblprerequisito= Label(ventanaeditar,text="Pre Requisito",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblprerequisito.place(x=10,y=80)
    lblsemestre= Label(ventanaeditar,text="Semestre",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblsemestre.place(x=10,y=115)
    lblopcionalidad= Label(ventanaeditar,text="Opcionalidad",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblopcionalidad.place(x=10,y=150)
    lblcreditos= Label(ventanaeditar,text="Créditos",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcreditos.place(x=10,y=185)
    lblestado= Label(ventanaeditar,text="Estado",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblestado.place(x=10,y=220)
    #ESPACIOS PARA ESCRIBIR
    txtmostrarcodigo=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostrarcodigo.place(x="185",y="20",width="600",height="30")
    txtmostrarnombre=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostrarnombre.place(x="185",y="55",width="600",height="30")
    txtmostrarprerrequisito=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostrarprerrequisito.place(x="185",y="90",width="600",height="30")
    txtmostrarsemestre=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostrarsemestre.place(x="185",y="125",width="600",height="30")
    txtmostraropcionalidad=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostraropcionalidad.place(x="185",y="160",width="600",height="30")
    txtmostrarcreeditos=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostrarcreeditos.place(x="185",y="195",width="600",height="30")
    txtmostrarestado=ttk.Entry(ventanaeditar,font="Cambria 22")
    txtmostrarestado.place(x="185",y="230",width="600",height="30")
    ventanaeditar.mainloop()
Mostrar()