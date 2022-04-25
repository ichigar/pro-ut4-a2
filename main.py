import tkinter as tk
from mostrar import *

class MainApplication():
    def __init__(self, parent):
        self.parent = parent

        self.parent.title("Gestión de recetas")
        self.parent.minsize(340,350)
        self.parent.resizable(width=False, height=False)

        self.lbl1 = tk.Label(self.parent, text="Gestión de recetas", font=("Arial Bold", 20))
        self.lbl1.grid(column=0, row=0, padx=25, pady=5)
        
        self.btn_0 = tk.Button(self.parent, text="Mostrar recetas", font=("Arial Bold", 12))
        self.btn_0.grid(column=0, row=2, padx=25, pady=5, sticky='ew')

        self.btn_1 = tk.Button(self.parent, text="Mostrar receta", font=("Arial Bold", 12), command = self.__btn_1_click)
        self.btn_1.grid(column=0, row=3, padx=25, pady=5, sticky='ew')
        
        self.btn_2 = tk.Button(self.parent, text="Mostrar recetas con ingredientes", font=("Arial Bold", 12))
        self.btn_2.grid(column=0, row=4, padx=25, pady=5, sticky='ew')
        
        self.btn_3 = tk.Button(self.parent, text="Nueva receta", font=("Arial Bold", 12))
        self.btn_3.grid(column=0, row=5, padx=25, pady=5, sticky='ew')
        
        self.btn_3 = tk.Button(self.parent, text="Añadir ingredientes", font=("Arial Bold", 12))
        self.btn_3.grid(column=0, row=6, padx=25, pady=5, sticky='ew')
        
        self.btn_4 = tk.Button(self.parent, text="Borrar receta", font=("Arial Bold", 12))
        self.btn_4.grid(column=0, row=7, padx=25, pady=5, sticky='ew')


    def __btn_1_click(self):
        op_mostrar_r = tk.Toplevel()
        MostrarReceta(op_mostrar_r)
        
if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()