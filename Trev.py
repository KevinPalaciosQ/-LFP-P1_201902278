from tkinter import *

from tkinter import ttk
ventana = Tk()
ventana.title('Ejemplo de TreeView')
ventana.geometry('600x300')
ventana['bg']='#fb0'

tv = ttk.Treeview(ventana, columns=("col1","col2","col3","col4","col5","col6"))

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



#tv.insert("",END,text="Azucar", values=("28","2"))
#tv.insert("",END,text="Refresco", values=("16","3"))
#tv.insert("",END,text="AQceite", values=("34","1"))
tv.pack()

ventana.mainloop()