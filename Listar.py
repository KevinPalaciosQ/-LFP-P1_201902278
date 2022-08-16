import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk

#VENTANA
def Listar():
    ventanaListar = tkinter.Tk()
    ventanaListar.title("Listar Cursos")
    ventanaListar.geometry("900x600")
    ventanaListar.config(bg="sky blue")
    ventanaListar.iconbitmap("favicon.ico")
    ventanaListar.resizable(0,0)
    tv = ttk.Treeview(ventanaListar,columns=("col0","col1","col2","col3","col4","col5","col6"))
    tv.column("#0",width=0)
    tv.column("col0",width=80, anchor=CENTER)
    tv.column("col1",width=250, anchor=CENTER)
    tv.column("col2",width=80, anchor=CENTER)
    tv.column("col3",width=80, anchor=CENTER)
    tv.column("col4",width=80, anchor=CENTER)
    tv.column("col5",width=80, anchor=CENTER)
    tv.column("col6",width=80, anchor=CENTER)
    tv.heading("col0", text="Código", anchor=CENTER)
    tv.heading("col1", text="Nombre", anchor=CENTER)
    tv.heading("col2", text="Pre requisitos", anchor=CENTER)
    tv.heading("col3", text="Opcionalidad", anchor=CENTER)
    tv.heading("col4", text="Semestre", anchor=CENTER)
    tv.heading("col5", text="Créditos", anchor=CENTER)
    tv.heading("col6", text="Estado", anchor=CENTER)
    arreglo=[]
    arreglo.append(("1","Social Humanistica 1", "150","1","1","4","1"))
    for a in arreglo:
        tv.insert("",tk.END,values=a)
    tv.pack()
    tv.place(x=80,y=30)
    ##BOTON PARA REGRESAR
    botonregresar = Button(ventanaListar,text="Regresar", font="Cambria 22", bg="yellow green",fg="blue",relief="groove", bd=9)
    botonregresar.place(x=660,y=520)
    ventanaListar.mainloop()
Listar()