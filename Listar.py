import tkinter
from tkinter import *
from tkinter import ttk
#VENTANA
def Listar():
    ventanaListar = tkinter.Tk()
    ventanaListar.title("Listar Cursos")
    ventanaListar.geometry("900x600")
    ventanaListar.config(bg="sky blue")
    ventanaListar.resizable(0,0)
    tv = ttk.Treeview(ventanaListar,columns=("col1","col2","col3","col4","col5","col6"))
    tv.column("#0",width=80)
    tv.column("col1",width=80, anchor=CENTER)
    tv.column("col2",width=80, anchor=CENTER)
    tv.column("col3",width=80, anchor=CENTER)
    tv.column("col4",width=80, anchor=CENTER)
    tv.column("col5",width=80, anchor=CENTER)
    tv.column("col6",width=80, anchor=CENTER)
    tv.heading("#0", text="Código", anchor=CENTER)
    tv.heading("col1", text="Nombre", anchor=CENTER)
    tv.heading("col2", text="Pre requisitos", anchor=CENTER)
    tv.heading("col3", text="Opcionalidad", anchor=CENTER)
    tv.heading("col4", text="Semestre", anchor=CENTER)
    tv.heading("col5", text="Créditos", anchor=CENTER)
    tv.heading("col6", text="Estado", anchor=CENTER)
    
    tv.pack()
    ##BOTON PARA REGRESAR
    botonregresar = Button(ventanaListar,text="Regresar", font="Cambria 22", bg="yellow green",fg="blue",relief="groove", bd=9)
    botonregresar.place(x=660,y=520)
    ventanaListar.mainloop()
Listar()