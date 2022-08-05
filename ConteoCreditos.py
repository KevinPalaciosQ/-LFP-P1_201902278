import tkinter
from tkinter import *
from tkinter import ttk
def ConteoDeCreditos():
    #VENTANA
    ventanaConteo = tkinter.Tk()
    ventanaConteo.title("Conteo de Créditos")
    ventanaConteo.geometry("700x350")
    ventanaConteo.config(bg="aqua")
    ventanaConteo.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaConteo,text="Regresar",font="Cambria 22", fg="blue", bg="yellow green",relief="groove", bd=9)
    botonsregresar.place(x=520,y=260)
    #ETIQUETAS
    lblAprobados= Label(ventanaConteo,text="Créditos Aprobados:",font="Cambria 22", fg="blue violet", bg="aqua")
    lblAprobados.place(x=10,y=10)
    lblXX= Label(ventanaConteo,text="XX",font="Cambria 22", fg="blue violet", bg="aqua")
    lblXX.place(x=265,y=12)
    lblCreditosCursando= Label(ventanaConteo,text="Créditos Cursando:",font="Cambria 22", fg="blue violet", bg="aqua")
    lblCreditosCursando.place(x=10,y=45)
    lblXX1= Label(ventanaConteo,text="XX",font="Cambria 22", fg="blue violet", bg="aqua")
    lblXX1.place(x=250,y=47)
    lblCreditosPendientes= Label(ventanaConteo,text="Créditos Pendientes:",font="Cambria 22", fg="blue violet", bg="aqua")
    lblCreditosPendientes.place(x=10,y=80)
    lblXX2= Label(ventanaConteo,text="XX",font="Cambria 22", fg="blue violet", bg="aqua")
    lblXX2.place(x=265,y=82)
    lblobligatorios= Label(ventanaConteo,text="Créditos Obligatorios hasta semestre N:",font="Cambria 21", fg="blue violet", bg="aqua")
    lblobligatorios.place(x=10,y=115)
    Entrada=StringVar
    txtObligatorios=Entry(ventanaConteo,textvariable=Entrada,font="Cambria 22", fg="gray").place(x="500",y="120",width="60",height="30")
    lblsemestre= Label(ventanaConteo,text="Semestre",font="Cambria 22", fg="blue violet", bg="aqua")
    lblsemestre.place(x=70,y=150)
    conteo1 = ttk.Spinbox(from_=0, to=250)
    conteo1.place(x=190, y=163, width=50, height=20)
    #BOTON PARA CONTAR
    botoncontar = Button(ventanaConteo,text="Contar",font="Cambria 10", fg="blue", bg="yellow green",relief="groove")
    botoncontar.place(x=250,y=160)
    lblCreditosDelSemestre= Label(ventanaConteo,text="Créditos del Semestre:",font="Cambria 22", fg="blue violet", bg="aqua")
    lblCreditosDelSemestre.place(x=10,y=185)
    Entrada1=StringVar
    txtDelSemestre=Entry(ventanaConteo,textvariable=Entrada1,font="Cambria 22", fg="gray").place(x="300",y="190",width="60",height="30")
    lblsemestre1= Label(ventanaConteo,text="Semestre",font="Cambria 22", fg="blue violet", bg="aqua")
    lblsemestre1.place(x=70,y=220)
    conteo2 = ttk.Spinbox(from_=0, to=250)
    conteo2.place(x=190, y=235, width=50, height=20)
    #BOTON PARA CONTAR
    botoncontar2 = Button(ventanaConteo,text="Contar",font="Cambria 10", fg="blue", bg="yellow green",relief="groove")
    botoncontar2.place(x=250,y=235)
    ventanaConteo.mainloop()
ConteoDeCreditos()