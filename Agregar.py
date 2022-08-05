import tkinter
from tkinter import *
def Agregar():
    #VENTANA
    ventanaAgregar = tkinter.Tk()
    ventanaAgregar.title("Agregar Curso")
    ventanaAgregar.geometry("900x400")
    ventanaAgregar.config(bg="sky blue")
    ventanaAgregar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaAgregar,text="Regresar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonsregresar.place(x=720,y=310)
    #BOTON PARA AGREGAR
    botonagregar = Button(ventanaAgregar,text="Agregar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9)
    botonagregar.place(x=560,y=310)
    #ETIQUETAS
    lblcodigo= Label(ventanaAgregar,text="Código",font="Cambria 22",fg="#9625b7", bg="sky blue")
    lblcodigo.place(x=10,y=10)
    lblnombre= Label(ventanaAgregar,text="Nombre",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombre.place(x=10,y=45)
    lblprerequisito= Label(ventanaAgregar,text="Pre Requisito",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblprerequisito.place(x=10,y=80)
    lblsemestre= Label(ventanaAgregar,text="Semestre",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblsemestre.place(x=10,y=115)
    lblopcionalidad= Label(ventanaAgregar,text="Opcionalidad",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblopcionalidad.place(x=10,y=150)
    lblcreditos= Label(ventanaAgregar,text="Créditos",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcreditos.place(x=10,y=185)
    lblestado= Label(ventanaAgregar,text="Estado",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblestado.place(x=10,y=220)
    #ESPACIOS PARA ESCRIBIR
    codigo=StringVar
    txtcodigo=Entry(ventanaAgregar,textvariable=codigo,font="Cambria 22", fg="gray").place(x="185",y="20",width="600",height="30")
    nombre=StringVar
    txtnombre=Entry(ventanaAgregar,textvariable=nombre,font="Cambria 22", fg="gray").place(x="185",y="55",width="600",height="30")
    pre=StringVar
    txtpre=Entry(ventanaAgregar,textvariable=pre,font="Cambria 22", fg="gray").place(x="185",y="90",width="600",height="30")
    semestre=StringVar
    txtsem=Entry(ventanaAgregar,textvariable=semestre,font="Cambria 22", fg="gray").place(x="185",y="125",width="600",height="30")
    opcionalidad=StringVar
    txtop=Entry(ventanaAgregar,textvariable=opcionalidad,font="Cambria 22", fg="gray").place(x="185",y="160",width="600",height="30")
    creditos=StringVar
    txtcred=Entry(ventanaAgregar,textvariable=creditos,font="Cambria 22", fg="gray").place(x="185",y="195",width="600",height="30")
    estado=StringVar
    txtestado=Entry(ventanaAgregar,textvariable=estado,font="Cambria 22", fg="gray").place(x="185",y="230",width="600",height="30")

    ventanaAgregar.mainloop()
Agregar()