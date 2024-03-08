import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: jonatan
apellido: quiroga
dni 32484284
---
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

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        continuar = True

        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        acumulador_femenino = 0

        contador_giovanni = 0
        contador_gianni = 0
        contador_esteban = 0



        while(continuar == True):
            nombre = prompt("NOMBRE", "ingrese su nombre")
            print(nombre)

            edad = prompt("EDAD", "ingrese su edad")
            edad = int(edad)
            while(edad < 13):
                edad = prompt("ERROR", "REingrese una edad valida")
                edad = int(edad)
            print(edad)
        
            genero = prompt("GENERO", "ingrese su genero: masculino, femenino, otro")
            while(genero != "masculino" and genero != "femenino" and genero != "otro"):
                genero = prompt("ERROR", "REingrese un genero valido: masculino, femenino, otro")
            print(genero)

            participantes = prompt("vote por un participante", "ingrese su voto por: giovanni, gianni y esteban")
            while(participantes != "giovanni" and participantes != "gianni" and participantes != "esteban"):
                participantes = prompt("ERROR", "REingrese un participante valido: giovanni, gianni y esteban")
            print(participantes)







            match(genero):
                case "masculino":
                    contador_masculino += 1
                case "femenino":
                    contador_femenino += 1
                    acumulador_femenino += edad
                case "otro":
                    contador_otro += 1
            

            
            


            continuar = question("continuar", "continuar?")


        

        promedio_votos_femenino = acumulador_femenino / contador_femenino
        print(promedio_votos_femenino)




        suma_todos_los_participantes = contador_giovanni + contador_gianni + contador_esteban

        porcentaje_giovanni = (contador_giovanni * 100) / suma_todos_los_participantes
        porcentaje_gianni = (contador_gianni * 100) / suma_todos_los_participantes
        porcentaje_esteban = (contador_esteban * 100) / suma_todos_los_participantes




        if(contador_giovanni > contador_gianni and contador_giovanni > contador_esteban):
            participante_mas_votado = "giovanni"
        elif(contador_gianni > contador_esteban):
            participante_mas_votado = "gianni"
        else:
            participante_mas_votado = "esteban"
        print(participante_mas_votado)


        alert("resultado", "El promedio de edad de las votantes de género Femenino {0}\n Nombre de cada participante y porcentaje de los votos qué recibió. giovanni {1} gianni {2} esteban {3} \n quien fue mas votado y deja la casa es {4}".format(promedio_votos_femenino, porcentaje_giovanni, porcentaje_gianni ,porcentaje_esteban ,participante_mas_votado))










        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()