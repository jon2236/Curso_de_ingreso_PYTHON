import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:jonatan
apellido:quiroga
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = True
        continuar = "s"
        edad = 0
        minoria_de_votos = 0
        mayoria_de_votos = 0
        contador = 0
        suma_total_edad = 0
        suma_total_votos = 0
        nombre_del_candidato_mas_votos = ""
        nombre_del_candidato_menos_votos = ""
        edad_del_candidato_menos_votos = 0
        promedio_edad = 0

        while(continuar == "s"):
            nombre = prompt("sus datos", "ingrese su nombre")
            
            edad = prompt("sus datos", "ingrese su edad")
            edad = int(edad)
            while(edad < 25):
                edad = prompt("sus datos", "REingrese sus datos")
                edad = int(edad)
            
            contador += 1
            suma_total_edad = edad + suma_total_edad

            cantidad_de_votos = prompt("sus datos", "ingrese sus votos")
            cantidad_de_votos = int(cantidad_de_votos)
            while(cantidad_de_votos < 0):
                cantidad_de_votos = prompt("error","REingrese su cantidad de votos")
                cantidad_de_votos = int(cantidad_de_votos)

            suma_total_votos = suma_total_votos + cantidad_de_votos

            if(cantidad_de_votos > mayoria_de_votos):
                mayoria_de_votos = cantidad_de_votos
                nombre_del_candidato_mas_votos = nombre

            if(cantidad_de_votos < minoria_de_votos or flag == True):
                minoria_de_votos = cantidad_de_votos
                nombre_del_candidato_menos_votos = nombre
                edad_del_candidato_menos_votos = edad
                flag = False
            continuar = prompt("continuar", "si desea continuar presione S, de lo contrario N")
        


        promedio_edad = suma_total_edad / contador


        alert("resultado",("nombre del candidato con más votos {0}\n nombre del candidato con menos votos {1} y su edad es {2}\n el promedio de edad es {3}\n la suma total de todos los votos es {4}").format(nombre_del_candidato_mas_votos, nombre_del_candidato_menos_votos, edad_del_candidato_menos_votos, promedio_edad, suma_total_votos))







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
