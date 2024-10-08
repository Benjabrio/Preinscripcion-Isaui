from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import ttk

def abrir_ventana_form1():
    form = Toplevel()
    form.title("Formulario de preinscripción")
    form.geometry("1920x1080")
    form.configure(bg="#1F6680")
    
    def activar_pantalla_completa(event=None):
        form.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        form.attributes("-fullscreen", False)

    form.attributes("-fullscreen", True) #Activa la pantalla completa al prender el programa
    form.bind("<Escape>", desactivar_pantalla_completa) #Se usa el escape para salir de la pantalla completa
    form.bind("<F11>", activar_pantalla_completa) # Se usa el f11 para entrar en el modo pantalla completa
    
    #titulo
    label_texto = Label(form, text="FORMULARIO\nPreinscripción",fg="White",font=("Arial",58))
    label_texto.configure(bg="#274357")
    label_texto.place(x=650, y=5)
    #datos personales
    label_datos = Label(form, text="DATOS PERSONALES:", fg ="White", font=("Arial", 24))
    label_datos.configure(bg="#274357")
    label_datos.place(x=70,y=200)

    #LABELS CON RESPECTIVOS ENTRYS
    #primera fila:
    label_nombre = Label(form, text="Nombre:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_nombre.place(x=100, y=250)
    entry_nombre = Entry(form, font=("Arial", 16))
    entry_nombre.place(x=100,y=280,width=500)
    label_apellido = Label(form, text="Apellido:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_apellido.place(x=680, y=250)
    entry_apellido = Entry(form, font=("Arial", 16))
    entry_apellido.place(x=680,y=280,width=500)
    label_dni = Label(form, text="DNI:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_dni.place(x=1260, y=250)
    entry_dni = Entry(form, font=("Arial", 16))
    entry_dni.place(x=1260,y=280,width=500)
    #Segunda Fila:
    label_cuil = Label(form, text="CUIL/CUIT:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_cuil.place(x=100, y=350)
    entry_cuil = Entry(form, font=("Arial", 16))
    entry_cuil.place(x=100,y=380,width=500)
    label_domicilio = Label(form, text="Domicilio:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_domicilio.place(x=680, y=350)
    entry_domicilio = Entry(form, font=("Arial", 16))
    entry_domicilio.place(x=680,y=380,width=500)
    label_provincia = Label(form, text="Provincia:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_provincia.place(x=1260, y=350)
    entry_provincia = Entry(form, font=("Arial", 16))
    entry_provincia.place(x=1260,y=380,width=500)
    #Tercera fila:
    label_Barrio = Label(form, text="Barrio:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_Barrio.place(x=100, y=450)
    entry_Barrio = Entry(form, font=("Arial", 16))
    entry_Barrio.place(x=100,y=480,width=500)
    label_cod_postal = Label(form, text="Código postal:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_cod_postal.place(x=680, y=450)
    entry_cod_postal = Entry(form, font=("Arial", 16))
    entry_cod_postal.place(x=680,y=480,width=150)
    label_telefono = Label(form, text="Teléfono:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_telefono.place(x=900, y=450)
    entry_telefono = Entry(form, font=("Arial", 16))
    entry_telefono.place(x=900,y=480,width=250)
    label_email = Label(form, text="Email:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_email.place(x=1260, y=450)
    entry_email = Entry(form, font=("Arial", 16))
    entry_email.place(x=1260,y=480,width=500)
    #4ta fila
    label_fecha = Label(form, text="Fecha de nacimiento:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_fecha.place(x=100, y=550)
    fecha_entry = DateEntry(form, font=("Arial", 16), borderwidth=2, state='readonly')
    fecha_entry.place(x=100,y=580,width=500)

    sexo = {
        1: "Masculino",
        2: "Femenino",
        3: "Indefinido",
    }
    lista_sexo = list(sexo.values())
    combobox_sexo = ttk.Combobox(form, values=lista_sexo,font=("Arial",16),state='readonly')
    combobox_sexo.set("...")
    label_sexo = Label(form, text="Sexo:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_sexo.place(x=680, y=550)
    combobox_sexo.place(x=680,y=580,width=150)

    #lugar de nacimiento
    label_nacimiento = Label(form, text="LUGAR DE NACIMIENTO:", fg ="White", font=("Arial", 24))
    label_nacimiento.configure(bg="#274357")
    label_nacimiento.place(x=70,y=700)
    
    #Labels con entry 
    label_pais = Label(form, text="País:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_pais.place(x=100, y=750)
    entry_pais = Entry(form, font=("Arial", 16))
    entry_pais.place(x=100,y=780,width=500)
    label_prov = Label(form, text="Provincia:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov.place(x=680, y=750)
    entry_prov = Entry(form, font=("Arial", 16))
    entry_prov.place(x=680,y=780,width=500)
    label_ciudad = Label(form, text="Ciudad:",bg="#1F6680", fg="White", font=("Arial", 14))
    label_ciudad.place(x=1260, y=750)
    entry_ciudad = Entry(form, font=("Arial", 16))
    entry_ciudad.place(x=1260,y=780,width=500)

    #boton para volver atras
    imagen_flecha = Image.open("C:/Users/benja/OneDrive/Desktop/Tkinter isaui/atras.png")
    flecha_atras = ImageTk.PhotoImage(imagen_flecha)
    boton_atras = Button(form, image=flecha_atras, bg="#274357",width=48, height=48,borderwidth=2,command=form.destroy)
    boton_atras.place(x=20,y=20)
    boton_atras.image = flecha_atras #Mantiene una referencia, porque sino no salia en el botón, se lo llevaba el recolecto de basura de python. Por eso se le asigna la imagen a un atributo del boton

    #Boton siguiente
    boton_siguiente = Button(form,text="Siguiente",bg="White",fg="Black",font=("Arial",12),borderwidth=2)
    boton_siguiente.place(x=1700,y=950,width=120,height=64)