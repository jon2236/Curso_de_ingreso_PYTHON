import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_03
---
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

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        continuar = True
        contador_masculino_iot_ia = 0
        contador_ia = 0
        contador_rv_ra = 0
        contador_iot = 0
        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        contador_iot_edad = 0
        tecnologia_mas_votada = ""

        
        
        
        while(continuar == True):
            nombre = prompt("NOMBRE", "ingrese nombre")

            edad = prompt("EDAD", "ingrese edad")
            edad = int(edad)
            while(edad < 18):
                edad = prompt("ERROR", "REingrese edad")
                edad = int(edad)

            genero = prompt("GENERO", "ingrese genero")
            while(genero != "masculino" and genero != "femenino" and genero != "otro"):
                genero = prompt("ERROR", "REingrese genero")

            tecnologia = prompt("TECNOLOGIA", "ingrese tecnologia")
            while(tecnologia != "ia" and tecnologia != "rv/ra" and tecnologia != "iot"):
                tecnologia = prompt("ERROR", "REingrese tecnologia")

            
            if(genero == "masculino" and (tecnologia == "iot" or tecnologia == "ia") and edad >= 25 and edad <= 50):
                contador_masculino_iot_ia += 1





            '''if(tecnologia == "ia"):
                contador_ia += 1
            elif(tecnologia == "iot"):
                contador_iot +=1
            else:
                contador_rv_ra'''

            match tecnologia:
                case "ia":
                    contador_ia += 1
                case "iot":
                    contador_iot += 1
                    ##!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
                    if(edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42):
                        contador_iot_edad += 1
                case "rv/ra":
                    contador_rv_ra += 1





            match genero:
                case "masculino":
                    contador_masculino += 1
                case "femenino":
                    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    
                    contador_femenino += 1
                case "otro":
                    contador_otro += 1




            continuar = question("seguir", "desea continuar?")




#tecnologia mas votada
        if(contador_ia > contador_iot and contador_ia > contador_rv_ra):
            tecnologia_mas_votada = "ia"
        elif(contador_iot > contador_ia and contador_iot > contador_rv_ra):
            tecnologia_mas_votada = "iot"
        else:
            tecnologia_mas_votada = "rv/ra"

#porcentaje de empleados por cada genero
        total_empleados = contador_masculino + contador_femenino + contador_otro
        porcentaje_masculino = (contador_masculino *100) / total_empleados
        porcentaje_femenino = (contador_femenino *100) / total_empleados
        porcentaje_otro = (contador_otro * 100) / total_empleados


        porcentaje_iot_edad = (contador_iot_edad * 100) / total_empleados



        alert("resultados", "cantidad de masculinos en rango de edad 25-50 años {0}".format(contador_masculino_iot_ia))


                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()