import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:jonatan
apellido:quiroga
---
Ejercicio: if_10
---
Enunciado:
Al presionar el botón 'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nota = random.randint(1, 10)
        
        if (nota >= 6):

            alert("mensaje", "Promoción directa, la nota es {0}".format(nota))
        
        elif (nota == 4 or nota == 5):
            alert("mensaje", "Aprobado, la nota es {0}".format(nota))
        
        else:
            alert("mensaje", "Desaprobado, la nota es {0}".format(nota))
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()