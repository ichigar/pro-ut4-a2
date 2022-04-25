import tkinter as tk
from tkinter import messagebox

from receta import *

class MostrarReceta():
    def __init__(self, parent):
        
        self.parent = parent  
        
        self.parent.title("Mostrar Receta")
        self.parent.minsize(400, 150)
        self.parent.resizable(width=False, height=False)
        
        self.lbl = tk.Label(self.parent, text="Mostrar Receta", font=("Arial Bold", 20))
        self.lbl.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        
        self.lbl_n = tk.Label(self.parent, text="Nombre de la receta:", font=("Arial", 12))    
        self.lbl_n.grid(column=0, row=1, padx=10, pady=5, sticky = "w")
        
        self.txt_n = tk.Entry(self.parent, width=25)
        self.txt_n.grid(column=1, row=1, padx=5, pady=5)
        self.txt_n.focus_set()           # Asignamos foco a este campo
        
        self.btn = tk.Button(self.parent, text="Enviar", font=("Arial", 12), command = self._form1_enviar)
        self.btn.grid(column=1, row=3, sticky='ew', padx=5, pady=5)
        
        # Al pulsar Enter ejecutar método
        self.parent.bind('<Return>', self._form1_enviar)
        
        
    def _form1_enviar(self, event = ""):        # bind pasa evento como parámetro
        nombre = self.txt_n.get()
        if nombre == "":
            # Ponemos atributo parent para que el mensaje se muestre encima de la ventana padre
            messagebox.showerror("error", "No se ha introducido ningún valor", parent = self.parent)
            
        else:
            receta = Receta()
            text_receta = receta.mostrar_receta(nombre)   # Obtenemos información de la receta
            if not text_receta:
                messagebox.showerror("error", "La receta no existe", parent = self.parent)
                
            else:
                self.parent.destroy()
                messagebox.showinfo(nombre, text_receta)