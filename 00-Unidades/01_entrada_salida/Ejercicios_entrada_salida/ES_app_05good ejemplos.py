import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_05
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
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        continuar = True
        bandera_primer_ingreso = True

        contador_femenino = 0
        acumulador_femenino = 0

        votante_mayor_edad = 0
        nombre_mayor_edad = ""
        votante_menor_edad = 0
        nombre_menor_edad_gianni = ""

        contador_giovanni = 0
        contador_gianni = 0
        contador_esteban = 0
        suma_todos_los_participantes = 0




        while(continuar == True):
            nombre = prompt("NOMBRE", "ingrese su nombre")
            print(nombre)

            edad = prompt("EDAD", "ingrese su edad")
            edad = int(edad)
            while(edad < 13):
                edad = prompt("ERROR", "REingrese una edad valida")
                edad = int(edad)
            print(edad)
        
            genero = prompt("GENERO", "ingrese su genero: m, f, otro")
            while(genero != "m" and genero != "f" and genero != "otro"):
                genero = prompt("ERROR", "REingrese un genero valido: M, F. otro")
            print(genero)

            participantes = prompt("vote por un participante", "ingrese su voto por: giovanni, gianni y esteban")
            while(participantes != "giovanni" and participantes != "gianni" and participantes != "esteban"):
                participantes = prompt("ERROR", "REingrese un participante valido: giovanni, gianni y esteban")
            print(participantes)




            #1 PROMEDIO
            if(genero == "f"):
                contador_femenino += 1
                acumulador_femenino += edad

            

            # MAXIMO
            if(edad > maximo_votante_de_mayor_edad or flag_nombre_votante_mayor_edad == True):
                maximo_votante_de_mayor_edad = edad
                nombre_votante_mayor_edad = nombre
                flag_nombre_votante_mayor_edad = False





            #4 PORCENTAJES
            if(edad > votante_mayor_edad or bandera_primer_ingreso == True):
                votante_mayor_edad = edad
                nombre_mayor_edad = nombre
                bandera_primer_ingreso = False






            match(nombre):
                case "giovanni":
                    contador_giovanni += 1
                case "gianni":
                    contador_gianni += 1
                    if(edad < votante_menor_edad or contador_gianni == 1): #3
                        votante_menor_edad = edad
                        nombre_menor_edad_gianni = nombre
                case "esteban":
                    contador_esteban += 1






            continuar = question("continuar","continuar?")



#PROMEDIO
        if(contador_femenino > 0):# este if evita q el programa rompa si ingresan el numero 0
            promedio_femenino = acumulador_femenino / contador_femenino #cuando pide PROMEDIO es cuando uso ACUMULADORES y NO igualo ==, sino q sumo +=. hago contador, acumulador, y luego divido acumulador / contador






#PORCENTAJES        
        suma_todos_los_participantes = contador_giovanni + contador_gianni + contador_esteban #creo los contadores, creo una variable q sea suma de todo, creo las variables del porcenatje pedido como abajo porcentaje gianni. aplico formula

        porcentaje_giovanni = (contador_giovanni * 100) / suma_todos_los_participantes  
        porcentaje_gianni = (contador_gianni * 100) / suma_todos_los_participantes
        porcentaje_esteban = (contador_esteban * 100) / suma_todos_los_participantes

        
        print("el votante de mayor edad es ", nombre_votante_mayor_edad)
        print(porcentaje_esteban)
        print(porcentaje_gianni)
        print(porcentaje_giovanni)
        print(promedio_femenino)
        print(nombre_mayor_edad)
        print(nombre_menor_edad_gianni)



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()