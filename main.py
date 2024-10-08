import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from form1 import abrir_ventana_form1


#para poner la pantalla completa
def activar_pantalla_completa(event=None):
    ventana.attributes("-fullscreen", True)

def desactivar_pantalla_completa(event=None):
    ventana.attributes("-fullscreen", False)

ventana = tk.Tk()
ventana.title("PREINSCRIPCIÓN ISAUI")
ventana.geometry("1920x1080")
ventana.configure(bg="#1F6680")
ventana.attributes("-fullscreen", True) #Activa la pantalla completa al prender el programa
ventana.bind("<Escape>", desactivar_pantalla_completa) #Se usa el escape para salir de la pantalla completa
ventana.bind("<F11>", activar_pantalla_completa) # Se usa el f11 para entrar en el modo pantalla completa

#frames
frame1 = tk.Frame(ventana,bg="#274357",width=75, height=1080)
frame1.place(x=44,y=0)
frame2 = tk.Frame(ventana,bg="#274357",width=75, height=1080)
frame2.place(x=1799,y=0)

#Logo Isaui
imagen = Image.open("C:/Users/benja/OneDrive/Desktop/Tkinter isaui/isaui.png")
imagen_redimensionada = imagen.resize((900,600))
imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
label_imagen = tk.Label(ventana,image=imagen_logo)
label_imagen.configure(bg="#1F6680")
label_imagen.place(x=502,y=-100)

#Frame cuadrado con carreras
frame_cuadrado = tk.Frame(ventana,bg="#274357",width=827, height=411)
frame_cuadrado.place(x=530, y=351)
label_texto = tk.Label(ventana, text="Bienvenido a la preinscripción 2025\nElija la carrera a la cual ingresar",fg="White",font=("Arial",38))
label_texto.configure(bg="#274357")
label_texto.place(x=536, y=351)

#ComboBox de carreras
carreras = {
    1: "Software",
    2: "Enfermería",
    3: "Diseño de Espacios",
    4: "Guía de Trekking",
    5: "Guía de Turismo",
    6: "Turismo y Hotelería"
}
lista_carreras = list(carreras.values())
combobox_carreras = ttk.Combobox(ventana, values=lista_carreras,font=("Arial",20),state='readonly')
combobox_carreras.set("Seleccione un carrera...")
combobox_carreras.place(x=704,y=540,width=513,height=70)

#Botones
boton_admin = tk.Button(ventana,text="Ingreso Admin", width= 12,fg="White",font=("Arial",12))
boton_admin.place(x=1630,y=20,width=120,height=64)
boton_admin.configure(bg="#274357")
boton_avanzar = tk.Button(ventana,text="Avanzar",bg="White",fg="Black",font=("Arial",20), command= abrir_ventana_form1)
boton_avanzar.place(x=768,y=649,width=353,height=64)

ventana.mainloop()
