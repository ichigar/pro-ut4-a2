from tkinter import *
from tkinter import messagebox

from receta import *

class MostrarReceta:
    def __init__(self):
        self._iniciar()
        
    def _iniciar(self):
        self.mostrar_w = Tk()
        self.mostrar_w.title("Mostrar Receta")
        self.mostrar_w.minsize(400, 150)
        self.mostrar_w.resizable(width=False, height=False)
        
        self.lbl = Label(self.mostrar_w, text="Mostrar Receta", font=("Arial Bold", 20))
        self.lbl.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        
        self.lbl_n = Label(self.mostrar_w, text="Nombre de la receta:", font=("Arial", 12))    
        self.lbl_n.grid(column=0, row=1, padx=10, pady=5, sticky = "w")
        
        self.txt_n = Entry(self.mostrar_w, width=25)
        self.txt_n.grid(column=1, row=1, padx=5, pady=5)
        self.txt_n.focus_set()           # Asignamos foco a este campo
        
        self.btn = Button(self.mostrar_w, text="Enviar", font=("Arial", 12), command = self._form1_enviar)
        self.btn.grid(column=1, row=3, sticky='ew', padx=5, pady=5)
        
        # Al pulsar Enter ejecutar método
        self.mostrar_w.bind('<Return>', self._form1_enviar)
        
        self.mostrar_w.mainloop()
        
    def _form1_enviar(self, event = ""):        # bind pasa evento como parámetro
        nombre = self.txt_n.get()
        if nombre == "":
            messagebox.showerror("error", "No se ha introducido ningún valor")
            # Ponemos la ventana de mostrar receta encima
            self.mostrar_w.attributes('-topmost', True)
            self.mostrar_w.update()
        else:
            receta = Receta()
            text_receta = receta.mostrar_receta(nombre)
            if not text_receta:

                self.mostrar_w.destroy()
                messagebox.showerror("error", "La receta no existe")
                
            else:
                self.mostrar_w.destroy()
                messagebox.showinfo(nombre, text_receta)