#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from mostrar import *

class Main:
    
    def __init__(self):
        self.__iniciar()
    
    def __iniciar(self):
        self.main_w = Tk()
        self.main_w.title("Gestión de recetas")
        #self.main_w.columnconfigure(0, minsize=250)
        #self.main_w.rowconfigure([0, 1, 2], minsize=100)
        self.main_w.minsize(200,320)

        self.lbl1 = Label(self.main_w, text="Gestión de recetas", font=("Arial Bold", 20))
        self.lbl1.grid(column=0, row=0, padx=25, pady=5)
        
        self.btn_0 = Button(self.main_w, text="Mostrar recetas", font=("Arial Bold", 12))
        self.btn_0.grid(column=0, row=2, padx=25, pady=5, sticky='ew')

        self.btn_1 = Button(self.main_w, text="Mostrar receta", font=("Arial Bold", 12), command = self.__btn_1_click)
        self.btn_1.grid(column=0, row=3, padx=25, pady=5, sticky='ew')
        
        self.btn_2 = Button(self.main_w, text="Mostrar recetas con ingredientes", font=("Arial Bold", 12))
        self.btn_2.grid(column=0, row=4, padx=25, pady=5, sticky='ew')
        
        self.btn_3 = Button(self.main_w, text="Nueva receta", font=("Arial Bold", 12))
        self.btn_3.grid(column=0, row=5, padx=25, pady=5, sticky='ew')
        
        self.btn_3 = Button(self.main_w, text="Añadir ingredientes", font=("Arial Bold", 12))
        self.btn_3.grid(column=0, row=6, padx=25, pady=5, sticky='ew')
        
        self.btn_4 = Button(self.main_w, text="Borrar receta", font=("Arial Bold", 12))
        self.btn_4.grid(column=0, row=7, padx=25, pady=5, sticky='ew')

        self.main_w.mainloop()
        
    def __btn_1_click(self):
        mostrar = MostrarReceta()
    

        
if __name__ == '__main__':
    main = Main()