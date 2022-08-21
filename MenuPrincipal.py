import tkinter
import sys
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter import Button, filedialog, messagebox
from tkinter import filedialog
from types import NoneType
from Credito import Creditos
ventana=None
VentanaP=None
ventanacurso=None
ventanaConteo=None
ventanaListar=None
ventanadelete=None
ventanaAgregar=None
ventanaeditar=None
ventaamostrar=None
txtcode=None
txtname=None
txtprerequest=None
txtsemester=None
txtcredits=None
txtestate=None
txtoption=None
txtmostrarcodigo=None
txtmostrarnombre=None
txtmostrarprerrequisito=None
txtmostrarsemestre=None
txtmostraropcionalidad=None
txtmostrarcreeditos=None
txtmostrarestado=None
txtEliminar=None
global botongestion
lblXX=None
lblXX1=None
lblXX2=None
creditos = []
arreglo=[]
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
def RetornarMostrar():

    global ventaamostrar
    ventaamostrar.destroy()
    Gestionar1()
#METODO PARA OBTENER LA RUTA DEL ARCHIVO 
def obtenerruta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.lfp*"), ("all files", "*.*")))
    return ruta
def CargardeArchivo():
    #VENTANA
    global VentanaP
    global ventana
    global txtRuta
    global lblespacio
    VentanaP.destroy()
    ventana = tkinter.Tk()
    ventana.title("Seleccionar Archivo")
    ventana.geometry("600x200")
    ventana.config(bg="sky blue")
    #ventana.iconbitmap("favicon.ico")
    ventana.resizable(0,0)
    #ETIQUETAS
    lblruta = Label(ventana,text="Ruta:",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblruta.place(x=10,y=10)
    lblespacio = Label(ventana,text="",font="Cambria 12", fg="black", bg="gray")
    lblespacio.place(x=80,y=20)
    #ESPACIOS PARA ESCRIBIR
    #BOTONES
    botonselec = Button(ventana,text="Seleccionar",fon="arial 20", fg="gray", bg="#e4ade4", relief="groove", bd=9, command=leerArchivo)
    botonselec.place(x=200,y=80)
    botonregreso = Button(ventana,text="Regresar",fon="arial 20", fg="gray", bg="#e4ade4", command=RetornarPrincipal, relief="groove", bd=9)
    botonregreso.place(x=400,y=80)
    ventana.mainloop()
#METODO PARA LEER EL CONTENIDO DEL ARCHIVO CARGADO
def leerArchivo():
    global contenido
    global lblespacio 
    global creditos
    global credito
    global data
    ruta = obtenerruta()
    if ruta != "":
        archivo = open(ruta,"r",encoding="utf8")   
        contenido = archivo.read()
        lblespacio.configure(text=""+ruta)
        contenido = contenido.split('\n')
        for contenidoo in contenido:
            if (contenidoo !=""):
                data= contenidoo.split(",")
                if ExisteCurso(data[0])==False:
                    credito= Creditos(data[0], data[1],  data[3], data[4],data[5],data[6].rstrip("\n"))
                    agregarprerre(data[2], credito)
                    creditos.append(credito)
                    print (data)
        messagebox.showinfo("Success","Archivo cargado")
        return creditos
    else:
        messagebox.showinfo("Warning","No se cargó ningun archivo")
def EliminarLinea():
    global creditos
    pass
#METODO PARA SEPARAR PRERREQUISITO
def agregarprerre(prerre, cursoo):
    if (prerre!= ""):
        press = prerre.split(",")
        for pe in press:
            cursoo.prerrequisitos.append(pe)
#METODO PARA VALIDAR QUE NO SE REPITA UN CURSO
def ExisteCurso(codigo):
    global creditos
    for iterador in creditos:
        if iterador.codigo==codigo:
            return True
    return False
def Gestionar():
    global VentanaP
    global ventanacurso
    
    VentanaP.destroy()
    
    #VENTANA
    ventanacurso = tkinter.Tk()
    ventanacurso.title("Gestionar")
    ventanacurso.geometry("900x600")
    ventanacurso.config(bg="sky blue")
    #ventanacurso.iconbitmap("favicon.ico")
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
    botonregresar.place(x=335,y=450)
    #BOTON PARA MOSTRAR CURSO EN ESPECIFICO
    botonmostrarespecifico= Button(ventanacurso,text="Mostrar",font="Cambria 22", fg="gray", bg="#e4ade4",command=Mostrar,relief="groove",bd=9, width="11")
    botonmostrarespecifico.place(x=335,y=370)
    ventanacurso.mainloop()
def Gestionar1():
    global VentanaP
    global ventanacurso
    
    #VentanaP.destroy()
    
    #VENTANA
    ventanacurso = tkinter.Tk()
    ventanacurso.title("Gestionar")
    ventanacurso.geometry("900x600")
    ventanacurso.config(bg="sky blue")
    #ventanacurso.iconbitmap("favicon.ico")
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
    botonregresar.place(x=335,y=450)
    #BOTON PARA MOSTRAR CURSO EN ESPECIFICO
    botonmostrarespecifico= Button(ventanacurso,text="Mostrar",font="Cambria 22", fg="gray", bg="#e4ade4",command=Mostrar,relief="groove",bd=9, width="11")
    botonmostrarespecifico.place(x=335,y=370)
    ventanacurso.mainloop()
def ConteoDeCreditos():

    global VentanaP
    global ventanaConteo
    global lblXX, lblXX1,lblXX2,conteo1,conteo2,txtObligatorios,txtDelSemestre
    VentanaP.destroy()
    #VENTANA
    ventanaConteo = tkinter.Tk()
    ventanaConteo.title("Conteo de Créditos")
    ventanaConteo.geometry("700x350")
    ventanaConteo.config(bg="sky blue")
    #ventanaConteo.iconbitmap("favicon.ico")
    ventanaConteo.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaConteo,text="Regresar",font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarConteoPrincipal)
    botonsregresar.place(x=520,y=260)
    #ETIQUETAS
    lblAprobados= Label(ventanaConteo,text="Créditos Aprobados:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblAprobados.place(x=10,y=10)
    lblXX= Label(ventanaConteo,text="",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblXX.place(x=265,y=12)
    lblCreditosCursando= Label(ventanaConteo,text="Créditos Cursando:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblCreditosCursando.place(x=10,y=45)
    lblXX1= Label(ventanaConteo,text="",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblXX1.place(x=250,y=47)
    lblCreditosPendientes= Label(ventanaConteo,text="Créditos Pendientes:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblCreditosPendientes.place(x=10,y=80)
    lblXX2= Label(ventanaConteo,text="",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblXX2.place(x=265,y=82)
    lblobligatorios= Label(ventanaConteo,text="Créditos Obligatorios hasta semestre N:",font="Cambria 21", fg="blue violet", bg="sky blue")
    lblobligatorios.place(x=10,y=115)
    txtObligatorios=Entry(ventanaConteo,font="Cambria 22")
    txtObligatorios.place(x="500",y="120",width="60",height="30")
    lblsemestre= Label(ventanaConteo,text="Semestre",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblsemestre.place(x=70,y=150)
    conteo1 = ttk.Spinbox(from_=0, to=10, )
    conteo1.place(x=190, y=163, width=50, height=20)
    #BOTON PARA CONTAR
    botoncontar = Button(ventanaConteo,text="Contar",font="Cambria 10", fg="gray", bg="#e4ade4",relief="groove",command=ConteoN)
    botoncontar.place(x=250,y=160)
    lblCreditosDelSemestre= Label(ventanaConteo,text="Créditos del Semestre:",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblCreditosDelSemestre.place(x=10,y=185)
    txtDelSemestre=ttk.Entry(ventanaConteo,font="Cambria 22")
    txtDelSemestre.place(x="300",y="190",width="60",height="30")
    lblsemestre1= Label(ventanaConteo,text="Semestre",font="Cambria 22", fg="blue violet", bg="sky blue")
    lblsemestre1.place(x=70,y=220)
    conteo2 = ttk.Spinbox(from_=0, to=10)
    conteo2.place(x=190, y=235, width=50, height=20)
    #BOTON PARA CONTAR
    botoncontar2 = Button(ventanaConteo,text="Contar",font="Cambria 10", fg="gray", bg="#e4ade4",relief="groove",command=CreditosSemestre)
    botoncontar2.place(x=250,y=235)
    botonEstado= Button(ventanaConteo,text=" Estado",font="Cambria 18", fg="gray", bg="#e4ade4",relief="groove",bd=9, command=ConteoGeneral)
    botonEstado.place(x=520,y=20)
    ventanaConteo.mainloop()
#Método Para Contar Hasta Semestre N
def ConteoN():
    global conteo1
    obligatorios=0
    global creditos
    conteo1.get()
    print(conteo1.get())
    for iterador  in range(len(creditos)):
        if int(creditos[iterador].semestre)<=int(conteo1.get()) and creditos[iterador].obligatorio=="1":
            obligatorios +=int(creditos[iterador].creditos)
    txtObligatorios.insert(tk.INSERT, obligatorios)
    txtObligatorios.config(state="disabled")
#Método Para Contar Creditos del Semestre
def CreditosSemestre():
    global conteo2
    semestre=0
    conteo2.get()
    print(conteo2.get())
    for iterador  in range(len(creditos)):
        if int(creditos[iterador].semestre)==int(conteo2.get()) and (creditos[iterador].estado=="1" or creditos[iterador].estado=="0" or creditos[iterador].estado=="-1"):
            semestre +=int(creditos[iterador].creditos)
    txtDelSemestre.insert(tk.INSERT, semestre)
    txtDelSemestre.config(state="disabled")

#Método para Contar Aprobado, Cursado y Pendiente
def ConteoGeneral():
    #Contadores Inicializados en 0
    global creditos
    global lblXX,lblXX1,lblXX2
    aprobados=0
    cursando=0
    pendiente=0
    for iterador  in range(len(creditos)):
        if creditos[iterador].estado=="0":
            aprobados +=int(creditos[iterador].creditos)
        if creditos[iterador].estado=="1":
            cursando +=int(creditos[iterador].creditos)
        if creditos[iterador].estado=="-1" and creditos[iterador].obligatorio=="1":
            pendiente +=int(creditos[iterador].creditos)
    print(aprobados)
    print(cursando)
    print(pendiente)
    estado_aprobado=(str(aprobados))
    estado_cursado=(str(cursando))
    estado_pendiente=(str(pendiente))
    lblXX.configure(text=""+estado_aprobado)
    lblXX1.configure(text=""+estado_cursado)
    lblXX2.configure(text=""+estado_pendiente)
def Listar():
    global ventanacurso
    global ventanaListar
    global arreglo
    ventanacurso.destroy()
    ventanaListar = tkinter.Tk()
    ventanaListar.title("Listar Cursos")
    ventanaListar.geometry("1050x600")
    ventanaListar.config(bg="sky blue")
    #ventanaListar.iconbitmap("favicon.ico")
    ventanaListar.resizable(0,0)
    tv = ttk.Treeview(ventanaListar,columns=("col0","col1","col2","col3","col4","col5","col6"))
    tv.column("#0",width=0)
    tv.column("col0",width=80, anchor=CENTER)
    tv.column("col1",width=350, anchor=CENTER)
    tv.column("col2",width=160, anchor=CENTER)
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
    for aa in creditos:
        var =""
        for prerre in aa.prerrequisitos:
            var +=prerre + "" 
        arreglo.append((aa.codigo,aa.nombre,aa.prerrequisitos,aa.obligatorio,aa.semestre,aa.creditos,aa.estado))
    for aaa in arreglo:
        tv.insert("",tk.END,values=aaa)
    tv.pack()
    tv.place(x=80,y=40)
    ##BOTON PARA REGRESAR
    botonregresar = Button(ventanaListar,text="Regresar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9,command=RetornarGestionListar)
    botonregresar.place(x=660,y=520)
    ventanaListar.mainloop()
def Eliminar():
    global ventanacurso
    global ventanadelete
    global txtEliminar
    ventanacurso.destroy()
    #VENTANA
    ventanadelete = tkinter.Tk()
    ventanadelete.title("Eliminar Curso")
    ventanadelete.geometry("600x200")
    ventanadelete.config(bg="sky blue")
    #ventanadelete.iconbitmap("favicon.ico")
    ventanadelete.resizable(0,0)
    #ETIQUETA
    lblCodigoCurso= Label(ventanadelete,text="Código de Curso",font="Cambria 22",fg="#9625b7", bg="sky blue")
    lblCodigoCurso.place(x=10,y=10)
    #ESPACIOS PARA ESCRIBIR
    txtEliminar=ttk.Entry(ventanadelete,font="Cambria 22")
    txtEliminar.place(x="230",y="20",width="100",height="30")
    #BOTONES
    botoneliminar = Button(ventanadelete,text="Eliminar", font="Cambria 22",  fg="gray", bg="#e4ade4",relief="groove", bd=9, command=DeletCourse)
    botoneliminar.place(x=200,y=80)
    botonregresoeliminar = Button(ventanadelete,text="Regresar", font="Cambria 22",  fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarEliminar)
    botonregresoeliminar.place(x=400,y=80)
    ventanadelete.mainloop()
#METODO UTILIZADO PARA ELIMINAR CURSO
def DeletCourse():
    global txtEliminar
    global creditos
    variable =True
    for i in range( len(creditos)):
        if (creditos[i].codigo)==txtEliminar.get():
            creditos.pop(i)
            variable==False
            messagebox.showinfo("Success","Se Eliminó con Éxito el curso")
            return creditos
    else:
        pass
    if variable==True and txtEliminar.get()!="":
        messagebox.showinfo("Warning","No Se Encontró el curso ")
    elif txtEliminar.get()=="":
        messagebox.showinfo("Warning","Por favor llene el campo")
def Mostrar():
    global ventanacurso
    global ventaamostrar
    global txtmostrarcodigo
    global txtmostrarnombre
    global txtmostrarprerrequisito
    global txtmostrarsemestre
    global txtmostraropcionalidad
    global txtmostrarcreeditos
    global txtmostrarestado
    ventanacurso.destroy()
    #VENTANA
    ventaamostrar = tkinter.Tk()
    ventaamostrar.title("Mostrar Curso en Específico")
    ventaamostrar.geometry("900x450")
    ventaamostrar.config(bg="sky blue")
    #ventaamostrar.iconbitmap("favicon.ico")
    ventaamostrar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonback = Button(ventaamostrar,text="Regresar",fon="arial 20" ,fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarMostrar)
    botonback.place(x=720,y=350)
    #BOTON PARA AGREGAR
    botonshow = Button(ventaamostrar,text="Mostrar",fon="arial 20", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=ShowCourse)
    botonshow.place(x=560,y=350)
    #ETIQUETAS
    lblcodigo= Label(ventaamostrar,text="Código",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcodigo.place(x=10,y=10)
    lblnombre= Label(ventaamostrar,text="Nombre",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombre.place(x=10,y=45)
    lblprerequisito= Label(ventaamostrar,text="Pre Requisito",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblprerequisito.place(x=10,y=80)
    lblsemestre= Label(ventaamostrar,text="Semestre",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblsemestre.place(x=10,y=115)
    lblopcionalidad= Label(ventaamostrar,text="Opcionalidad",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblopcionalidad.place(x=10,y=150)
    lblcreditos= Label(ventaamostrar,text="Créditos",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcreditos.place(x=10,y=185)
    lblestado= Label(ventaamostrar,text="Estado",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblestado.place(x=10,y=220)
    #ESPACIOS PARA ESCRIBIR
    txtmostrarcodigo=ttk.Entry(ventaamostrar,font="Cambria 22")
    txtmostrarcodigo.place(x="185",y="20",width="600",height="30")
    txtmostrarnombre=ttk.Entry(ventaamostrar,font="Cambria 18")
    txtmostrarnombre.place(x="185",y="55",width="600",height="30")
    #txtmostrarnombre.config(state="disabled")
    txtmostrarprerrequisito=ttk.Entry(ventaamostrar,font="Cambria 18")
    txtmostrarprerrequisito.place(x="185",y="90",width="600",height="30")
    txtmostrarsemestre=ttk.Entry(ventaamostrar,font="Cambria 22")
    txtmostrarsemestre.place(x="185",y="125",width="600",height="30")
    txtmostraropcionalidad=ttk.Entry(ventaamostrar,font="Cambria 22")
    txtmostraropcionalidad.place(x="185",y="160",width="600",height="30")
    txtmostrarcreeditos=ttk.Entry(ventaamostrar,font="Cambria 22")
    txtmostrarcreeditos.place(x="185",y="195",width="600",height="30")
    txtmostrarestado=ttk.Entry(ventaamostrar,font="Cambria 22")
    txtmostrarestado.place(x="185",y="230",width="600",height="30")
    ventaamostrar.mainloop()
def ShowCourse():
    global txtmostrarcodigo
    global txtmostrarnombre
    global txtmostrarprerrequisito
    global txtmostrarsemestre
    global txtmostraropcionalidad
    global txtmostrarcreeditos
    global txtmostrarestado
    global creditos
    bandera =True
    for i in range( len(creditos)):
        if (creditos[i].codigo)==txtmostrarcodigo.get():
            txtmostrarnombre.insert(tk.INSERT, creditos[i].nombre)
            txtmostrarnombre.config(state="disabled")
            txtmostrarprerrequisito.insert(tk.INSERT, creditos[i].prerrequisitos)
            txtmostrarprerrequisito.config(state="disabled")
            txtmostrarsemestre.insert(tk.INSERT, creditos[i].semestre)
            txtmostrarsemestre.config(state="disabled")
            txtmostraropcionalidad.insert(tk.INSERT, creditos[i].obligatorio)
            txtmostraropcionalidad.config(state="disabled")
            txtmostrarcreeditos.insert(tk.INSERT, creditos[i].creditos)
            txtmostrarcreeditos.config(state="disabled")
            txtmostrarestado.insert(tk.INSERT, creditos[i].estado)
            txtmostrarestado.config(state="disabled")
            bandera==False
            messagebox.showinfo("Success","Se encontró el curso")
            return creditos
        else:
            pass
    if bandera==True and txtmostrarcodigo.get()!="":
        messagebox.showinfo("Warning","No Se Encontró el curso")
    elif txtmostrarcodigo.get()=="":
        messagebox.showinfo("Warning","Por favor llene el campo")

def AgregaCurso():
    global txtcode
    global txtname
    global txtprerequest
    global txtsemester
    global txtoption
    global txtcredits
    global txtestate
    global arreglo
    global data
    print(txtcode.get())
    print(txtname.get())
    print(txtprerequest.get())
    print(txtsemester.get())
    print(txtoption.get())
    print(txtcredits.get())
    print(txtestate.get())
    for i in range( len(creditos)):
        if (creditos[i].codigo)==txtcode.get():
            messagebox.showinfo("Success","Este curso ya existe")
            return creditos
    if (txtcode.get()!= "" and txtname.get()!="" and txtprerequest.get()!="" and txtsemester.get()!="" and txtoption.get()!="" and txtcredits.get()!="" and txtestate.get()!=""):
        niu=Creditos(txtcode.get(),txtname.get(),txtsemester.get(),txtoption.get(),txtcredits.get(),txtestate.get())
        agregarprerre(txtprerequest.get(), niu)
        creditos.append(niu) 
        messagebox.showinfo("Success","Se agregó el Curso")
        return creditos
    elif (txtcode.get()== "" and txtname.get()=="" and txtprerequest.get()=="" and txtsemester.get()=="" and txtoption.get()=="" and txtcredits.get()=="" and txtestate.get()==""):
        messagebox.showinfo("Warning","Por favor llene los campos")

def Agregar():
    global ventanacurso
    global ventanaAgregar
    global txtcode
    global txtname
    global txtprerequest
    global txtsemester
    global txtoption
    global txtcredits
    global txtestate
    ventanacurso.destroy()
    #VENTANA
    ventanaAgregar = tkinter.Tk()
    ventanaAgregar.title("Agregar Curso")
    ventanaAgregar.geometry("900x400")
    ventanaAgregar.config(bg="sky blue")
    #ventanaAgregar.iconbitmap("favicon.ico")
    ventanaAgregar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaAgregar,text="Regresar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarAgregar)
    botonsregresar.place(x=720,y=310)

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
    txtcode=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtcode.place(x="185",y="20",width="600",height="30")
    txtname=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtname.place(x="185",y="55",width="600",height="30")
    txtprerequest=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtprerequest.place(x="185",y="90",width="600",height="30")
    txtsemester=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtsemester.place(x="185",y="125",width="600",height="30")
    txtoption=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtoption.place(x="185",y="160",width="600",height="30")
    txtcredits=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtcredits.place(x="185",y="195",width="600",height="30")
    txtestate=ttk.Entry(ventanaAgregar,font="Cambria 22")
    txtestate.place(x="185",y="230",width="600",height="30")
    #BOTON PARA AGREGAR
    botonagregar = Button(ventanaAgregar,text="Agregar", font="Cambria 22", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=AgregaCurso)
    botonagregar.place(x=560,y=310)
    ventanaAgregar.mainloop()
def Editar():
    global ventanacurso
    global ventanaeditar
    global txteditarcodigo
    global txteditarnombre
    global txteditarprerrequisito
    global txteditarsemestre
    global txteditaropcionalidad
    global txteditarcreeditos
    global txteditarestado
    ventanacurso.destroy()
    #VENTANA
    ventanaeditar = tkinter.Tk()
    ventanaeditar.title("Editar Curso")
    ventanaeditar.geometry("900x450")
    ventanaeditar.config(bg="sky blue")
    #ventanaeditar.iconbitmap("favicon.ico")
    ventanaeditar.resizable(0,0)
    #BOTON PARA REGRESAR
    botonsregresar = Button(ventanaeditar,text="Regresar",fon="arial 20" ,fg="gray", bg="#e4ade4",relief="groove", bd=9, command=RetornarEditar)
    botonsregresar.place(x=720,y=350)
    #BOTON PARA AGREGAR
    botonagregar = Button(ventanaeditar,text="Editar",fon="arial 20", fg="gray", bg="#e4ade4",relief="groove", bd=9, command=Edicion)
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
    txteditarcodigo=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditarcodigo.place(x="185",y="20",width="600",height="30")
    txteditarnombre=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditarnombre.place(x="185",y="55",width="600",height="30")
    txteditarprerrequisito=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditarprerrequisito.place(x="185",y="90",width="600",height="30")
    txteditarsemestre=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditarsemestre.place(x="185",y="125",width="600",height="30")
    txteditaropcionalidad=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditaropcionalidad.place(x="185",y="160",width="600",height="30")
    txteditarcreeditos=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditarcreeditos.place(x="185",y="195",width="600",height="30")
    txteditarestado=ttk.Entry(ventanaeditar,font="Cambria 22")
    txteditarestado.place(x="185",y="230",width="600",height="30")

    ventanaeditar.mainloop()
def Edicion():
    global txteditarcodigo
    global txteditarnombre
    global txteditarprerrequisito
    global txteditarsemestre
    global txteditaropcionalidad
    global txteditarcreeditos
    global txteditarestado
    global creditos
    Bandera=True
    for i in range( len(creditos)):
        if (creditos[i].codigo)==txteditarcodigo.get():
            variable1=Busqueda(txteditarcodigo.get())
            if variable1 !=None:
                variable1.nombre=txteditarnombre.get()
                variable1.prerrequisitos=txteditarprerrequisito.get()
                variable1.obligatorio=txteditaropcionalidad.get()
                variable1.semestre=txteditarsemestre.get()
                variable1.creditos=txteditarcreeditos.get()
                variable1.estado=txteditarestado.get()
                messagebox.showinfo("Success","Se Editó el Curso")
                Bandera=False
                return creditos
    if Bandera==True and  (txteditarcodigo.get()!= "" and txteditarnombre.get()!="" and txteditarprerrequisito.get()!="" and txteditarsemestre.get()!="" and txteditaropcionalidad.get()!="" and txteditarcreeditos.get()!="" and txteditarestado.get()!=""):
        messagebox.showinfo("Warning ","No se encontró el curso, intente con otro código")
    elif (txteditarcodigo.get()== "" and txteditarnombre.get()=="" and txteditarprerrequisito.get()=="" and txteditarsemestre.get()=="" and txteditaropcionalidad.get()=="" and txteditarcreeditos.get()=="" and txteditarestado.get()==""):
        messagebox.showinfo("Warning ","Por favor llene los campos")
def Salirxd():
    global VentanaP
    VentanaP.destroy()
def Busqueda(uno):

    global txteditarcodigo
    global txteditarnombre
    global txteditarprerrequisito
    global txteditarsemestre
    global txteditaropcionalidad
    global txteditarcreeditos
    global txteditarestado
    global creditos
    for hola in creditos:
        if uno == hola.codigo:
            return hola
    return None
def Principal():
    global VentanaP
    global botongestion
    #VENTANA
    VentanaP = tkinter.Tk()
    VentanaP.title("Practica 1")
    VentanaP.geometry("970x600")
    VentanaP.config(bg="sky blue")
    #VentanaP.iconbitmap("favicon.ico")
    VentanaP.resizable(0,0)
    #ETIQUETAS
    lblnombrecurso = Label(VentanaP,text="Nombre del Curso: Lab. Lenguajes Formales y de Programación",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombrecurso.place(x=10,y=10)
    lblnombreestudiante = Label(VentanaP,text="Nombre del Estudiante: Kevin Estuardo Palacios Quiñonez",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblnombreestudiante.place(x=10,y=75)
    lblcarneestudiante = Label(VentanaP,text="Carné del Estudiante: 201902278",font="Cambria 22", fg="#9625b7", bg="sky blue")
    lblcarneestudiante.place(x=10,y=135)
    lblseccion = Label(VentanaP,text="Sección: B+",font="Cambria 22", fg="black", bg="sky blue")
    lblseccion.place(x=805,y=10)
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
    botonsalir = Button(VentanaP,text="Salir",font="Cambria 22", fg="gray", bg="#e4ade4", command=Salirxd, relief="groove", bd=9,width="15")
    botonsalir.place(x=320,y=430)
    VentanaP.mainloop()
if __name__ == "__main__":
    Principal()

