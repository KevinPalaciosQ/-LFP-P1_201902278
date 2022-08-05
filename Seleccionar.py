import tkinter
from tkinter import *
#from Principal import *
def CargardeArchivo():
#VENTANA
    ventana = tkinter.Tk()
    ventana.title("Seleccionar Archivo")
    ventana.geometry("600x200")
    ventana.config(bg="aqua")
    ventana.resizable(0,0)
    #ETIQUETA
    lblruta = Label(ventana,text="Ruta:",font="arial 20", fg="black", bg="aqua")
    lblruta.place(x=10,y=10)
    #ESPACIOS PARA ESCRIBIR
    Entrada=StringVar
    txtRuta=Entry(ventana,textvariable=Entrada,font="arial 20").place(x="110",y="20",width="450",height="30")

    #BOTONES
    botonselec = Button(ventana,text="Seleccionar",fon="arial 20", fg="blue", bg="yellow green")
    botonselec.place(x=200,y=80)
    botonregreso = Button(ventana,text="Regresar",fon="arial 20", fg="blue", bg="yellow green")
    botonregreso.place(x=400,y=80)
    ventana.mainloop()