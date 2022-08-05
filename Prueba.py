import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
ventana=None
VentanaP=None
ventanacurso=None
ventanaConteo=None
ventanaListar=None
ventanadelete=None
ventanaAgregar=None
ventanaeditar=None
def RetornarPrincipal():
    global ventana
    ventana.destroy()
    Principal()
def RetornarGestionaPrincipal():
    global ventanacurso
    ventanacurso.destroy()
    Principal()
def RetornarConteoPrincipal():
    global ventanaConteo
    ventanaConteo.destroy()
    Principal()
def RetornarGestionListar():
    global ventanaListar
    ventanaListar.destroy()
    Gestionar1()
def RetornarEliminar():
    global ventanadelete
    ventanadelete.destroy()
    Gestionar1()
def RetornarAgregar():
    global ventanaAgregar
    ventanaAgregar.destroy()
    Gestionar1()
def RetornarEditar():
    global ventanaeditar
    ventanaeditar.destroy()
    Gestionar1()
def CargardeArchivo():
    #VENTANA
    global VentanaP
    global ventana
    VentanaP.destroy()
    ventana = tkinter.Tk()
    ventana.title("Seleccionar Archivo")
    ventana.geometry("600x200")
    ventana.config(bg="sky blue")
    ventana.resizable(0,0)
    #ETIQUETA
    lblruta = Label(ventana,text="Ruta:",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblruta.place(x=10,y=10)
    #ESPACIOS PARA ESCRIBIR
    Entrada=StringVar
    txtRuta=Entry(ventana,textvariable=Entrada,font="Cambria 22",fg="gray").place(x="110",y="20",width="450",height="30")
    #BOTONES
    botonselec = Button(ventana,text="Seleccionar",fon="arial 20", fg="gray", bg="#e4ade4", relief="groove", bd=9)
    botonselec.place(x=200,y=80)
    botonregreso = Button(ventana,text="Regresar",fon="arial 20", fg="gray", bg="#e4ade4", command=RetornarPrincipal, relief="groove", bd=9)
    botonregreso.place(x=400,y=80)
    ventana.mainloop()
    
def Gestionar():
    global VentanaP
    global ventanacurso
    VentanaP.destroy()
    #VENTANA
    ventanacurso = tkinter.Tk()
    ventanacurso.title("Gestionar")
    ventanacurso.geometry("900x600")
    ventanacurso.config(bg="sky blue")
    ventanacurso.resizable(0,0)
    #BOTONES----------------------------------------
    #BOTON PARA LISTAR CURSOS  
    botonlistar= Button(ventanacurso,text="Listar",font="Cambria 22", fg="gray", bg="#e4ade4", relief="groove",bd=9, width="11", command=Listar)
    botonlistar.place(x=335,y=50)
    #BOTON PARA AGREGAR CURSO
    botonagregar= Button(ventanacurso,text="Agregar Curso",font="Cambria 22", fg="gray", bg="#e4ade4",anchor="center", relief="groove",bd=9, width="11", command=Agregar)
    botonagregar.place(x=335,y=130)
    #BOTON PARA EDITAR CURSO
    botoneditar= Button(ventanacurso,text="Editar Curso",font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove",bd=9, width="11", command=Editar)
    botoneditar.place(x=335,y=210)
    #BOTON PARA ELIMINAR CURSO
    botoneliminar= Button(ventanacurso,text="Eliminar Curso",font="Cambria 22", fg="gray", bg="#e4ade4", relief="groove",bd=9, width="11", command=Eliminar)
    botoneliminar.place(x=335,y=290)
    #BOTON PARA REGRESAR
    botonregresar= Button(ventanacurso,text="Regresar",font="Cambria 22", fg="gray", bg="#e4ade4",command=RetornarGestionaPrincipal, relief="groove",bd=9, width="11")
    botonregresar.place(x=335,y=370)
    ventanacurso.mainloop()
def Gestionar1():
    global VentanaP
    global ventanacurso
    #VENTANA
    ventanacurso = tkinter.Tk()
    ventanacurso.title("Gestionar")
    ventanacurso.geometry("900x600")
    ventanacurso.config(bg="sky blue")
    ventanacurso.resizable(0,0)
    #BOTONES----------------------------------------
    #BOTON PARA LISTAR CURSOS  
    botonlistar= Button(ventanacurso,text="Listar",font="Cambria 22", fg="gray", bg="#e4ade4", relief="groove",bd=9, width="11", command=Listar)
    botonlistar.place(x=335,y=50)
    #BOTON PARA AGREGAR CURSO
    botonagregar= Button(ventanacurso,text="Agregar Curso",font="Cambria 22", fg="gray", bg="#e4ade4",anchor="center", relief="groove",bd=9, width="11",command=Agregar)
    botonagregar.place(x=335,y=130)
    #BOTON PARA EDITAR CURSO
    botoneditar= Button(ventanacurso,text="Editar Curso",font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove",bd=9, width="11", command=Editar)
    botoneditar.place(x=335,y=210)
    #BOTON PARA ELIMINAR CURSO
    botoneliminar= Button(ventanacurso,text="Eliminar Curso",font="Cambria 22", fg="gray", bg="#e4ade4", relief="groove",bd=9, width="11", command=Eliminar)
    botoneliminar.place(x=335,y=290)
    #BOTON PARA REGRESAR
    botonregresar= Button(ventanacurso,text="Regresar",font="Cambria 22", fg="gray", bg="#e4ade4",command=RetornarGestionaPrincipal, relief="groove",bd=9, width="11")
    botonregresar.place(x=335,y=370)
    ventanacurso.mainloop()
def ConteoDeCreditos():
    global VentanaP
    global ventanaConteo
    VentanaP.destroy()
    #VENTANA
    ventanaConteo = tkinter.Tk()
    ventanaConteo.title("Conteo de Créditos")
    ventanaConteo.geometry("700x350")
    ventanaConteo.config(bg="sky blue")
    ventanaConteo.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaConteo,text="Regresar",font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarConteoPrincipal)
    botonsregresar.place(x=520,y=260)
    #ETIQUETAS
    lblAprobados= Label(ventanaConteo,text="Créditos Aprobados:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblAprobados.place(x=10,y=10)
    lblXX= Label(ventanaConteo,text="XX",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblXX.place(x=265,y=12)
    lblCreditosCursando= Label(ventanaConteo,text="Créditos Cursando:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblCreditosCursando.place(x=10,y=45)
    lblXX1= Label(ventanaConteo,text="XX",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblXX1.place(x=250,y=47)
    lblCreditosPendientes= Label(ventanaConteo,text="Créditos Pendientes:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblCreditosPendientes.place(x=10,y=80)
    lblXX2= Label(ventanaConteo,text="XX",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblXX2.place(x=265,y=82)
    lblobligatorios= Label(ventanaConteo,text="Créditos Obligatorios hasta semestre N:",font="Cambria 21", fg="blue violet", bg="sky blue")
    lblobligatorios.place(x=10,y=115)
    Entrada=StringVar
    txtObligatorios=Entry(ventanaConteo,textvariable=Entrada,font="Cambria 22", fg="gray").place(x="500",y="120",width="60",height="30")
    lblsemestre= Label(ventanaConteo,text="Semestre",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblsemestre.place(x=70,y=150)
    conteo1 = ttk.Spinbox(from_=0, to=250)
    conteo1.place(x=190, y=163, width=50, height=20)
    #BOTON PARA CONTAR
    botoncontar = Button(ventanaConteo,text="Contar",font="Cambria 10", fg="gray", bg="#e4ade4",relief="groove")
    botoncontar.place(x=250,y=160)
    lblCreditosDelSemestre= Label(ventanaConteo,text="Créditos del Semestre:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblCreditosDelSemestre.place(x=10,y=185)
    Entrada1=StringVar
    txtDelSemestre=Entry(ventanaConteo,textvariable=Entrada1,font="Cambria 22", fg="gray").place(x="300",y="190",width="60",height="30")
    lblsemestre1= Label(ventanaConteo,text="Semestre",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblsemestre1.place(x=70,y=220)
    conteo2 = ttk.Spinbox(from_=0, to=250)
    conteo2.place(x=190, y=235, width=50, height=20)
    #BOTON PARA CONTAR
    botoncontar2 = Button(ventanaConteo,text="Contar",font="Cambria 10", fg="gray", bg="#e4ade4",relief="groove")
    botoncontar2.place(x=250,y=235)
    ventanaConteo.mainloop()

def Listar():
    global ventanacurso
    global ventanaListar
    ventanacurso.destroy()
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
    botonregresar = Button(ventanaListar,text="Regresar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9,command=RetornarGestionListar)
    botonregresar.place(x=660,y=520)
    ventanaListar.mainloop()
def Eliminar():
    global ventanacurso
    global ventanadelete
    ventanacurso.destroy()
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
    botonregresoeliminar = Button(ventanadelete,text="Regresar", font="Cambria 22",  fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarEliminar)
    botonregresoeliminar.place(x=400,y=80)
    ventanadelete.mainloop()
def Agregar():
    global ventanacurso
    global ventanaAgregar
    ventanacurso.destroy()
    #VENTANA
    ventanaAgregar = tkinter.Tk()
    ventanaAgregar.title("Agregar Curso")
    ventanaAgregar.geometry("900x400")
    ventanaAgregar.config(bg="sky blue")
    ventanaAgregar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaAgregar,text="Regresar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarAgregar)
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
def Editar():
    global ventanacurso
    global ventanaeditar
    ventanacurso.destroy()
    #VENTANA
    ventanaeditar = tkinter.Tk()
    ventanaeditar.title("Editar Curso")
    ventanaeditar.geometry("900x450")
    ventanaeditar.config(bg="sky blue")
    ventanaeditar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaeditar,text="Regresar",fon="arial 20" ,fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarEditar)
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
def Principal():
    global VentanaP
    #VENTANA
    VentanaP = tkinter.Tk()
    VentanaP.title("Practica 1")
    VentanaP.geometry("900x600")
    VentanaP.config(bg="sky blue")
    VentanaP.resizable(0,0)
    #ETIQUETAS
    lblnombrecurso = Label(VentanaP,text="Nombre del Curso: Lab. Lenguajes Formales y de Programación",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombrecurso.place(x=10,y=10)
    lblnombreestudiante = Label(VentanaP,text="Nombre del Estudiante: Kevin Estuardo Palacios Quiñonez",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombreestudiante.place(x=10,y=75)
    lblcarneestudiante = Label(VentanaP,text="Carné del Estudiante: 201902278",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcarneestudiante.place(x=10,y=135)
    #BOTON PARA LA CARGA DEL ARCHIVO 
    botoncarga = Button(VentanaP,text="Cargar Archivo",font="Cambria 22", fg="gray", bg="#e4ade4", command=CargardeArchivo, relief="groove", bd=9, width=15)
    botoncarga.place(x=320,y=185)
    #BOTON PARA GESTIONAR CURSOS 
    botongestion = Button(VentanaP,text="Gestionar Cursos",font="Cambria 22", fg="gray", bg="#e4ade4", command=Gestionar, relief="groove", bd=9, width="15")
    botongestion.place(x=320,y=265)
    #BOTON PARA CONTEO DE CRÉDITOS
    botonconteo = Button(VentanaP,text="Conteo de Créditos",font="Cambria 22", fg="gray", bg="#e4ade4", relief="groove", bd=9,width="15", command=ConteoDeCreditos)
    botonconteo.place(x=320,y=345)
    #BOTON PARA SALIR
    botonsalir = Button(VentanaP,text="Salir",font="Cambria 22", fg="gray", bg="#e4ade4", command=exit, relief="groove", bd=9,width="15")
    botonsalir.place(x=320,y=430)
    VentanaP.mainloop()
    #ventana.destroy()
Principal()

