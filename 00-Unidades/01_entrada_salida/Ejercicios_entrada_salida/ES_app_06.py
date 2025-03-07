import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_06
---
Enunciado:
Al presionar el botón  'Sumar', se deberán obtener los valores contenidos en las cajas de texto (txt_operador_A y txt_operador_B), transformarlos en números enteros, realizar la suma y luego mostrar el resultado de la operación utilizando el Dialog Alert. 
Ej: "El resultado de la sumas es: 755" 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_sumar_on_click(self):
        #numero_a = int(prompt("numero A", "ingrese un numero"))
        #numero_b = int(prompt("numero B", "ingrese un numero"))

        #self.txt_operador_a.delete(0, "end")
        #self.txt_operador_a.insert(0, numero_a)
        #self.txt_operador_b.delete(0, "end")
        #self.txt_operador_b.insert(0, numero_b)

        #resultado = numero_a + numero_b
        #alert("resultado", "el total es " + str(resultado))

        numero_1 = int(self.txt_operador_a.get())
        numero_2 = int(self.txt_operador_b.get())

        resultado = numero_1 + numero_2
        alert("resultado", "el total es " + str(resultado))
     
        
if __name__ == "__main__":
    app = App()
    app.geometry("600x600")
    app.mainloop()