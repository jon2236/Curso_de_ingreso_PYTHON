import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: jopnatan
apellido: quiroga
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        continuar = "s"

        while(continuar == "s"):
            apellido = prompt("sus datos", "ingrese su apellido")
            if(apellido == None):
                break

            edad = prompt("sus datos", "ingrese edad entre 18 y 90 años inclusive")
            if(edad == None):
                break
            edad = int(edad)
            while(edad < 18 or edad > 90):
                edad = prompt("edad incorrecta", "reingrese una edad valida")
                edad = int(edad)
            
            estado_civil = prompt("sus datos", "ingrese su estado civil: Soltero/a, Casado/a, Divorciado/a, Viudo/a")
            if(estado_civil == None):
                break
            #estado_civil = prompt("sus datos", "ingrese su estado civil: Soltero, Casado, Divorciado, Viudo")
            #while(estado_civil != "Soltero" and estado_civil != "Casado" and estado_civil != "Divorciado" and estado_civil != "Viudo"):
            #        estado_civil = prompt("ingreso de datos", "REingrese su estado civil: Soltero, Casado, Divorciado, Viudo")
            
            while(estado_civil not in self.combobox_tipo._values):
                estado_civil = prompt("error", "reingrese estado civil")

            numero_legajo = prompt("sus datos", " ingrese su numero de 4 cifras, sin ceros a la izquierda")
            if(numero_legajo == None):
                break
            numero_legajo = int(numero_legajo)
            while(numero_legajo <= 1000 or numero_legajo >= 9999):
                numero_legajo = prompt("sus datos", "reingrese un numero valido")
                numero_legajo = int(numero_legajo)
            
            continuar = prompt("datos ingresados", "para comenzar con otro ingreso presione la letra S de lo contrario presione la letra N")

        self.txt_apellido.delete(0, "end")
        self.txt_apellido.insert(0, apellido)
        
        self.txt_edad.delete(0, "end")
        self.txt_edad.insert(0, edad)

        self.combobox_tipo.set(estado_civil)

        self.txt_legajo.delete(0, "end")
        self.txt_legajo.insert(0, numero_legajo)

            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

#while True:
            #apellido = prompt("mensaje","Ingrese su apellido: ")
            #if apellido == None:
             #   break
            #edad = int(edad)