from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from confirmacion import mostrar_confirmacion

def abrir_ventana_form2(form):
    form2 = Toplevel()
    form2.title("Formulario de preinscripción")
    form2.geometry("1366x768")
    form2.configure(bg="#1F6680")

    def activar_pantalla_completa(event=None):
        form2.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        form2.attributes("-fullscreen", False)

    form2.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    form2.bind("<Escape>", desactivar_pantalla_completa)
    form2.bind("<F11>", activar_pantalla_completa)

    # Estudios
    label_estudios = Label(form2, text="ESTUDIOS:", fg="White", font=("Arial", 24))
    label_estudios.configure(bg="#274357")
    label_estudios.place(x=20, y=80)

    label_nivel = Label(form2, text="NIVEL MEDIO:", fg="White", font=("Arial", 14))
    label_nivel.configure(bg="#1F6680")
    label_nivel.place(x=20, y=140)
    label_nivel = Label(form2, text="NIVEL SUPERIOR:", fg="White", font=("Arial", 14))
    label_nivel.configure(bg="#1F6680")
    label_nivel.place(x=20, y=250)
    #CheckButtons
    check_si = Checkbutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357")
    check_si.place(x=170, y=140)
    check_no = Checkbutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357")
    check_no.place(x=220, y=140)
    check_si = Checkbutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357")
    check_si.place(x=200, y=250)
    check_no = Checkbutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357")
    check_no.place(x=250, y=250)
    #Primera fila
    label_año_ingreso = Label(form2, text="Año ingreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_ingreso.place(x=20, y=180)
    entry_año_ingreso = Entry(form2, font=("Arial", 16))
    entry_año_ingreso.place(x=20, y=210, width=150)
    label_año_egreso = Label(form2, text="Año egreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_egreso.place(x=190, y=180)
    entry_año_egreso = Entry(form2, font=("Arial", 16))
    entry_año_egreso.place(x=190, y=210, width=150)
    label_prov = Label(form2, text="Provincia:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov.place(x=370, y=180)
    entry_prov = Entry(form2, font=("Arial", 16))
    entry_prov.place(x=370, y=210, width=400)
    label_titulo = Label(form2, text="Título:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_titulo.place(x=800, y=180)
    entry_titulo = Entry(form2, font=("Arial", 16))
    entry_titulo.place(x=800, y=210, width=400)

    #Siguiente fila de nivel superior
    label_carrera = Label(form2, text="Carrera:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_carrera.place(x=20, y=280)
    entry_carrera = Entry(form2, font=("Arial", 16))
    entry_carrera.place(x=20, y=310, width=400)

    label_institucion = Label(form2, text="Institución:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_institucion.place(x=450, y=280)
    entry_institucion = Entry(form2, font=("Arial", 16))
    entry_institucion.place(x=450, y=310, width=400)

    label_prov_ins = Label(form2, text="Provincia:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov_ins.place(x=880, y=280)
    entry_prov_ins = Entry(form2, font=("Arial", 16))
    entry_prov_ins.place(x=880, y=310, width=400)

    #siguiente fila
    label_año_ingreso = Label(form2, text="Año ingreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_ingreso.place(x=20, y=350)
    entry_año_ingreso = Entry(form2, font=("Arial", 16))
    entry_año_ingreso.place(x=20, y=380, width=150)

    label_año_egreso = Label(form2, text="Año egreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_egreso.place(x=190, y=350)
    entry_año_egreso = Entry(form2, font=("Arial", 16))
    entry_año_egreso.place(x=190, y=380, width=150)

    #LABEL SITUACION LABORAL Y RESPONSABILIDADES
    label_sit_laboral = Label(form2, text="SITUACIÓN LABORAL:", fg="White", font=("Arial", 24))
    label_sit_laboral.configure(bg="#274357")
    label_sit_laboral.place(x=20, y=430)
    label_responsabilidades = Label(form2, text="RESPONSABILIDADES:", fg="White", font=("Arial", 24))
    label_responsabilidades.configure(bg="#274357")
    label_responsabilidades.place(x=650, y=430)

    label_trabajo = Label(form2, text="¿TRABAJA?:", fg="White", font=("Arial", 14))
    label_trabajo.configure(bg="#1F6680")
    label_trabajo.place(x=20, y=490)
    label_cargo = Label(form2, text="¿TIENE PERSONAS A CARGO?:", fg="White", font=("Arial", 14))
    label_cargo.configure(bg="#1F6680")
    label_cargo.place(x=650, y=490)

    check_si = Checkbutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357")
    check_si.place(x=170, y=490)
    check_no = Checkbutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357")
    check_no.place(x=220, y=490)

    #check responsabilidades
    check_si = Checkbutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357")
    check_si.place(x=950, y=490)
    check_no = Checkbutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357")
    check_no.place(x=1000, y=490)

    #entrys situacion laboral
    label_horas = Label(form2, text="Horas diarias:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_horas.place(x=20, y=530)
    entry_horas = Entry(form2, font=("Arial", 16))
    entry_horas.place(x=20, y=560, width=150)
    label_descrip = Label(form2, text="Breve descripción del trabajo:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_descrip.place(x=20, y=590)
    texto_descrip = Text(form2, width=50, height=5, font=("Arial", 16))
    texto_descrip.place(x=20, y=620)

    #Boton Finalizar
    def finalizar():
        form2.destroy()
        mostrar_confirmacion()
    
    boton_siguiente = Button(form2, text="Finalizar", bg="White", fg="Black", font=("Arial", 12), borderwidth=2,command=finalizar)
    boton_siguiente.place(x=1240, y=700, width=120, height=64)

    # Botón para volver atrás

    def volver():
        form2.destroy()
        form.deiconify()

    
    imagen_flecha = Image.open("C:/Users/benja/OneDrive/Desktop/Tkinter isaui/Preinscripcion-Isaui/atras.png")
    flecha_atras = ImageTk.PhotoImage(imagen_flecha)
    boton_atras = Button(form2, image=flecha_atras, bg="#274357", width=48, height=48, borderwidth=2, command=volver)
    boton_atras.place(x=20, y=20)
    boton_atras.image = flecha_atras  # Mantiene una referencia a la imagen

    form2.mainloop()