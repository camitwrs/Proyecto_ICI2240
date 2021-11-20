from tkinter import *
from tkinter import messagebox

def ingresar():
    # Asume que el que entra es un EMPLEADO. Funciona con user: 20603557 y pass: 2310
    if usuario.get() == "20603557" and contra.get() == "2310": 
        abrir_ventana2()
    # Asume que el que entra es un ADMIN LOCAL. Funciona con user: 11111111 y pass: 2310
    elif usuario.get() == "11111111" and contra.get() == "2310":
        abrir_ventana4()
    # Asume que el que entra es un ADMIN GLOBAL. Funciona con user: 22222222 y pass: 2310
    elif usuario.get() == "22222222" and contra.get() == "2310":
        abrir_ventana6()
    else:   
        messagebox.showinfo("LOGIN", "Error. Inténtelo nuevamente")

def abrir_ventana2(): # MENÚ EMPLEADO
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("EMPLEADO")
    ventana2.geometry("400x200")
    ventana2.configure(bg="#8d4c5c")
    label1 = Label(ventana2, text="MENÚ EMPLEADO:")
    label1.configure(bg="#8d4c5c", fg="#ffffff")
    label1.pack(padx=10, pady=10)
    boton1 = Button(ventana2, text="Realizar venta", command=lambda:abrir_ventana3(ventana2))
    boton1.configure(bg="#f49e96")
    boton1.pack(padx=5, pady=5)
    boton2 = Button(ventana2, text="Marcar asistencia", command=marcar_asistencia)
    boton2.configure(bg="#f49e96")
    boton2.pack(padx=5, pady=5)
    boton3 = Button(ventana2, text="Informe de ventas", command=informe_ventas)
    boton3.configure(bg="#f49e96")
    boton3.pack(padx=5, pady=5)
    boton4 = Button(ventana2, text="Ver horario", command=mostrar_horario)
    boton4.configure(bg="#f49e96")
    boton4.pack(padx=5, pady=5)

def abrir_ventana3(ventana): # SUBMENÚ EMPLEADO - REALIZAR VENTA
    root.withdraw()
    ventana.withdraw()
    ventana3 = Toplevel()
    ventana3.title("EMPLEADO")
    ventana3.geometry("400x200")
    ventana3.configure(bg="#8d4c5c")
    label1 = Label(ventana3, text="SUBMENÚ REALIZAR VENTA:")
    label1.configure(bg="#8d4c5c", fg="#ffffff")
    label1.pack(padx=10, pady=10)
    boton1 = Button(ventana3, text="Vender entrada", command=venta_entrada)
    boton1.configure(bg="#f49e96")
    boton1.pack(padx=5, pady=5)
    boton2 = Button(ventana3, text=" Aplicar descuento", command=aplicar_descuento)
    boton2.configure(bg="#f49e96")
    boton2.pack(padx=5, pady=5)
    boton3 = Button(ventana3, text="Concretar venta", command=concretar_venta)
    boton3.configure(bg="#f49e96")
    boton3.pack(padx=5, pady=5)
    boton4 = Button(ventana3, text="Cancelar venta", command=cancelar_venta)
    boton4.configure(bg="#f49e96")
    boton4.pack(padx=5, pady=5)      

def marcar_asistencia():
    pass

def informe_ventas():
    pass

def mostrar_horario():
    pass
    
def venta_entrada(): # Hay que agrandar la ventana
    pass

def aplicar_descuento():
    pass

def concretar_venta():
    pass

def cancelar_venta():
    pass

def abrir_ventana4(): # MENÚ ADMIN LOCAL
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("ADMIN LOCAL")
    ventana2.geometry("400x200")
    ventana2.configure(bg="#8d4c5c")
    label1 = Label(ventana2, text="MENÚ ADMINISTRADOR LOCAL:")
    label1.configure(bg="#8d4c5c", fg="#ffffff")
    label1.pack(padx=10, pady=10)
    boton1 = Button(ventana2, text="Resumen general", command=resumen_general)
    boton1.configure(bg="#f49e96")
    boton1.pack(padx=5, pady=5)
    boton2 = Button(ventana2, text="Modificar cartelera", command=lambda:abrir_ventana5(ventana2))
    boton2.configure(bg="#f49e96")
    boton2.pack(padx=5, pady=5)
    boton3 = Button(ventana2, text="Informe de ventas", command=informe_ventas)
    boton3.configure(bg="#f49e96")
    boton3.pack(padx=5, pady=5)
    boton4 = Button(ventana2, text="Ver horario", command=mostrar_horario)
    boton4.configure(bg="#f49e96")
    boton4.pack(padx=5, pady=5)
    
def resumen_general():
    pass

def abrir_ventana5(ventana): # SUBMENÚ ADMIN LOCAL - MODIFICAR CARTELERA
    root.withdraw()
    ventana.withdraw()
    ventana3 = Toplevel()
    ventana3.title("ADMIN LOCAL")
    ventana3.geometry("400x200")
    ventana3.configure(bg="#8d4c5c")
    label1 = Label(ventana3, text="SUBMENÚ MODIFICAR CARTELERA:")
    label1.configure(bg="#8d4c5c", fg="#ffffff")
    label1.pack(padx=10, pady=10)
    boton1 = Button(ventana3, text="Añadir película", command=anadir_pelicula)
    boton1.configure(bg="#f49e96")
    boton1.pack(padx=5, pady=5)
    boton2 = Button(ventana3, text="Añadir funciones", command=anadir_funciones)
    boton2.configure(bg="#f49e96")
    boton2.pack(padx=5, pady=5)
    boton3 = Button(ventana3, text="Cancelar funciones", command=cancelar_funciones)
    boton3.configure(bg="#f49e96")
    boton3.pack(padx=5, pady=5)
    boton4 = Button(ventana3, text="Modificar precio funciones", command=modificar_precios)
    boton4.configure(bg="#f49e96")
    boton4.pack(padx=5, pady=5)   

def anadir_pelicula():
    pass

def anadir_funciones():
    pass

def cancelar_funciones():
    pass

def modificar_precios():
    pass

def abrir_ventana6(): # MENÚ ADMINISTRADOR GLOBAL
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("ADMIN GLOBAL")
    ventana2.geometry("400x280")
    ventana2.configure(bg="#8d4c5c")
    label1 = Label(ventana2, text="MENÚ ADMINISTRADOR GLOBAL:")
    label1.configure(bg="#8d4c5c", fg="#ffffff")
    label1.pack(padx=10, pady=10)
    boton1 = Button(ventana2, text="Modificar administradores", command=lambda:abrir_ventana7(ventana2))
    boton1.configure(bg="#f49e96")
    boton1.pack(padx=5, pady=5)
    boton2 = Button(ventana2, text="Modificar cine", command=modificar_cine)
    boton2.configure(bg="#f49e96")
    boton2.pack(padx=5, pady=5)
    boton3 = Button(ventana2, text="Ver información cine", command=mostrar_info_cine)
    boton3.configure(bg="#f49e96")
    boton3.pack(padx=5, pady=5)
    boton4 = Button(ventana2, text="Modificar precios películas", command=modificar_precios_totales)
    boton4.configure(bg="#f49e96")
    boton4.pack(padx=5, pady=5)
    boton5 = Button(ventana2, text="Generar cupones de descuento", command=generar_cupones)
    boton5.configure(bg="#f49e96")
    boton5.pack(padx=5, pady=5)
    boton6 = Button(ventana2, text="Realizar reporte", command=realizar_reporte)
    boton6.configure(bg="#f49e96")
    boton6.pack(padx=5, pady=5)
    
def abrir_ventana7(ventana): # SUBMENÚ ADMIN GLOBAL - MODIFICAR ADMINS
    root.withdraw()
    ventana.withdraw()
    ventana3 = Toplevel()
    ventana3.title("ADMIN GLOBAL")
    ventana3.geometry("400x130")
    ventana3.configure(bg="#8d4c5c")
    label1 = Label(ventana3, text="SUBMENÚ MODIFICAR ADMINISTRADORES:")
    label1.configure(bg="#8d4c5c", fg="#ffffff")
    label1.pack(padx=10, pady=10)
    boton1 = Button(ventana3, text="Agregar administrador local", command=agregar_adminlocal)
    boton1.configure(bg="#f49e96")
    boton1.pack(padx=5, pady=5)
    boton2 = Button(ventana3, text="Eliminar administrador local", command=eliminar_adminlocal)
    boton2.configure(bg="#f49e96")
    boton2.pack(padx=5, pady=5) 

def agregar_adminlocal():
    pass

def eliminar_adminlocal():
    pass

def modificar_cine():
    pass

def mostrar_info_cine():
    pass

def modificar_precios_totales():
    pass

def generar_cupones():
    pass

def realizar_reporte():
    pass

################################ MENÚ PRINCIPAL - LOGIN #############################################

root = Tk()
root.title("CINE4U")
root.iconbitmap(r'Programa Python\icon.ico')
root.geometry("400x130")
root.configure(bg="#8d4c5c")
root.resizable(width=False, height=False)

label_usuario = Label(root, text="Ingresar Usuario:")
label_usuario.configure(bg="#8d4c5c", fg="#ffffff")
label_usuario.pack()
usuario = StringVar()
entry_usuario = Entry(root, width=30, textvariable=usuario)
entry_usuario.configure(bg="#c37177")
entry_usuario.pack()

label_pass = Label(root, text="Contraseña:")
label_pass.configure(bg="#8d4c5c", fg="#ffffff")
label_pass.pack()
contra = StringVar()
entry_pass = Entry(root, width=30, show="*", textvariable=contra)
entry_pass.configure(bg="#c37177")
entry_pass.pack()

boton_principal = Button(root, text="Entrar", command=ingresar)
boton_principal.configure(bg="#f49e96")
boton_principal.pack(padx=10, pady=10)

root.mainloop()