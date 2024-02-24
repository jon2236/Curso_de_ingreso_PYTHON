import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: jonatan
apellido: quiroga
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_cero = 0

        while(True):
            numero_ingresado = prompt("ingresos", "ingrese un numero")
            if(numero_ingresado == None):
                break
            numero_ingresado = int(numero_ingresado)

            if(numero_ingresado < 0 ):
                suma_negativos = suma_negativos + numero_ingresado
                contador_negativos += 1
            elif(numero_ingresado > 0 ):
                suma_positivos = suma_positivos + numero_ingresado
                contador_positivos += 1
            else:
                contador_cero +=1
            print(suma_negativos, suma_positivos)

        diferencia = contador_positivos - contador_negativos

        alert("resultado", "suma acumulada negativos {0}\n suma acumulada positivos {1}\n cantidad numeros negativos {2}\n cantidad numeros positivos {3}\n diferencia entre positivos y negativos {4}\n cantidad de 0 {5}".format(suma_negativos, suma_positivos, contador_negativos, contador_positivos, diferencia, contador_cero)) 

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
