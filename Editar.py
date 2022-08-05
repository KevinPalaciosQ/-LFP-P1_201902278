import tkinter
from tkinter import *
def Editar():
    #VENTANA
    ventanaeditar = tkinter.Tk()
    ventanaeditar.title("Editar Curso")
    ventanaeditar.geometry("900x450")
    ventanaeditar.config(bg="sky blue")
    ventanaeditar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaeditar,text="Regresar",fon="arial 20" ,fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonsregresar.place(x=720,y=350)
    #BOTON PARA AGREGAR
    botonagregar = Button(ventanaeditar,text="Editar",fon="arial 20", fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonagregar.place(x=560,y=350)
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
    codigoeditar=StringVar
    txtcodigo=Entry(ventanaeditar,textvariable=codigoeditar,font="Cambria 22", fg="gray").place(x="185",y="20",width="600",height="30")
    nombreeditar=StringVar
    txtnombre=Entry(ventanaeditar,textvariable=nombreeditar,font="Cambria 22", fg="gray").place(x="185",y="55",width="600",height="30")
    preeditar=StringVar
    txtpre=Entry(ventanaeditar,textvariable=preeditar,font="Cambria 22", fg="gray").place(x="185",y="90",width="600",height="30")
    semestreeditar=StringVar
    txtsem=Entry(ventanaeditar,textvariable=semestreeditar,font="Cambria 22", fg="gray").place(x="185",y="125",width="600",height="30")
    opcionalidadeditar=StringVar
    txtop=Entry(ventanaeditar,textvariable=opcionalidadeditar,font="Cambria 22", fg="gray").place(x="185",y="160",width="600",height="30")
    creditoseditar=StringVar
    txtcred=Entry(ventanaeditar,textvariable=creditoseditar,font="Cambria 22", fg="gray").place(x="185",y="195",width="600",height="30")
    estadoeditar=StringVar
    txtestado=Entry(ventanaeditar,textvariable=estadoeditar,font="Cambria 22", fg="gray").place(x="185",y="230",width="600",height="30")

    ventanaeditar.mainloop()
Editar()