import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su 
proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 
    años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o 
    entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        continuar = True
        nombre = ""
        edad = 0
        genero = ""
        tecnologia = ""

        contador_masculino_iot_ia = 0
        contador_rv_ra = 0
        contador_ia = 0
        contador_iot = 0
        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0

        tecnologia_mas_votada = ""





        while(continuar == True):
            nombre = prompt("NOMBRE", "Ingrese su nombre")

            edad = prompt("EDAD", "Ingrese su edad")
            edad = int(edad)
            while(edad < 18):
                edad = prompt("ERROR", "REingrese su edad")
                edad = int(edad)
            
            genero = prompt("GENERO", "Ingrese un genero: masculino, femenino, otro")
            while(genero != "masculino" and genero != "femenino" and genero != "otro"):
                genero = prompt("ERROR", "REingrese un genero valido: masculino, femenino, otro")

            tecnologia = prompt("TECNOLOGIA","Vote por iot, rv/ra, ia")
            while(tecnologia != "iot" and tecnologia != "rv/ra" and tecnologia != "ia"):
                tecnologia = prompt("ERROR", "REingrese una tecnologia valida: iot, rv/ra, ia")







            if(genero == "masculino" and (tecnologia == "iot" or tecnologia == "ia") and edad >= 25 and edad <= 50):
                contador_masculino_iot_ia += 1

            match(tecnologia):
                case "ia":
                    contador_ia += 1
                case "rv/ra":
                    contador_rv_ra += 1
                case "iot":
                    contador_iot += 1


            match(genero):
                case "masculino":
                    contador_masculino += 1
                case "femenino":
                    contador_femenino += 1
                case "otro":
                    contador_otro += 1








            continuar = question("continuar","Desea continuar? S o N")




        if(contador_ia > contador_iot and contador_ia > contador_rv_ra):
            tecnologia_mas_votada = "ia"
        elif(contador_rv_ra > contador_ia and contador_rv_ra > contador_iot):
            tecnologia_mas_votada = "rv/ra"
        else:
            tecnologia_mas_votada = "iot"


        el_total_todos_los_generos = contador_femenino + contador_masculino + contador_otro
        porcentaje_masculino = (contador_masculino * el_total_todos_los_generos) / 100
        porcentaje_femenino = (contador_femenino * el_total_todos_los_generos) / 100
        porcentaje_otro = (contador_otro * el_total_todos_los_generos) / 100







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()