import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

    El promedio de edad de las votantes de género Femenino 

    Del votante más viejo, su nombre.

    Nombre del votante más joven qué votó a Gianni.

    Nombre de cada participante y porcentaje de los votos qué recibió.

    El nombre del participante que debe dejar la casa (El que tiene más votos)

'''



class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        continuar = True




        while(continuar == True):
            nombre = prompt("NOMBRE", "ingrese su nombre")

            edad = prompt("EDAD", "ingrese su edad")
            edad = int(edad)
            while(edad < 13):
                edad = prompt("ERROR", "REingrese su edad")
                edad = int(edad)
            
            genero = prompt("GENERO", "ingrese su genero: m, f, otro")
            while(genero != "m" and genero != "f" and genero != "otro"):
                genero = prompt("ERROR", "REingrese un genero valido: m, f, otro")

            nombre_partcipante = prompt("PARTICIPANTE", "ingrese su voto al nombre del participante a salir de la casa: giovanni, gianni y esteban")
            while(nombre_partcipante != "giovanni" and nombre_partcipante != "gianni" and nombre_partcipante != "esteban"):
                nombre_partcipante = prompt("ERROR", "REingrese su voto al nombre del participante a salir de la casa: giovanni, gianni y esteban")















            continuar = question("continuar", "continuar?")



        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
