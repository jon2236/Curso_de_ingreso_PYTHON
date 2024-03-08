import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:
-Nombre
-Importe ganado (mayor o igual $1000)
-Género (“Femenino”, “Masculino”, “Otro”)
-Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:
A) Nombre y género de la persona que más ganó.
B) Promedio de dinero ganado en Ruleta.
C) Porcentaje de personas que jugaron en el Tragamonedas.
D) Cuál es el juego menos elegido por los ganadores.
E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
F) Porcentaje de dinero en función de cada juego.

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
        flag_persona_mas_gano = True
        monto_maximo_ganado = 0
        nombre_persona_mas_gano = ""
        genero_persona_mas_gano = ""

        contador_poker = 0
        contador_ruleta = 0
        contador_tragamonedas = 0
        total_jugadores_de_todos_los_juegos = 0

        cantidad_ganado_ruleta = 0
        cantidad_ganado_tragamonedas = 0

        contador_no_poker = 0
        acumulador_no_poker = 0

        while(continuar == True):
            
            nombre = prompt("NOMBRE", "ingrese su nombre")
            print(nombre)

            importe_ganado = prompt("IMPORTE GANADO", "ingrese el monto ganado")
            importe_ganado = float(importe_ganado)
            while(importe_ganado < 1000):
                importe_ganado = prompt("ERROR", "REingrese un importe mayor a 1000")
                importe_ganado = float(importe_ganado)
            print(importe_ganado)
        
            genero = prompt("GENERO", "ingrese su genero: masculino, femenino, otro")
            while(genero != "masculino" and genero != "femenino" and genero != "otro"):
                genero = prompt("ERROR", "REingrese un genero valido: masculino, femenino, otro")
            print(genero)

            juego = prompt("JUEGO", "ingrese un juego: ruleta, poker, tragamonedas")
            while(juego != "ruleta" and juego != "poker" and juego != "tragamonedas"):
                juego = prompt("ERROR", "REingrese un juego valido: poker, ruleta, tragamonedas")
            print(juego)




            #A) Nombre y género de la persona que más ganó.
            if(importe_ganado > monto_maximo_ganado or flag_persona_mas_gano == True):
                monto_maximo_ganado = importe_ganado
                nombre_persona_mas_gano = nombre
                genero_persona_mas_gano = genero
                flag_persona_mas_gano = False

            
            #B) Promedio de dinero ganado en Ruleta.
            #tambien el C) usando contadores
            match(juego):
                case "poker":
                    contador_poker += 1
                case "ruleta":
                    contador_ruleta += 1
                    cantidad_ganado_ruleta += importe_ganado
                case "tragamonedas":
                    contador_tragamonedas += 1
                    cantidad_ganado_tragamonedas += importe_ganado

            

            #E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
            if(importe_ganado > 15000 and juego != "poker"):
                contador_no_poker += 1
                acumulador_no_poker += importe_ganado


            #F) Porcentaje de dinero en función de cada juego
            






            continuar = question("continuar", "continuar")

        
        
        
        if(contador_ruleta > 0):#B) Promedio de dinero ganado en Ruleta.
            promedio_ganado_ruleta = cantidad_ganado_ruleta / contador_ruleta



        #C) Porcentaje de personas que jugaron en el Tragamonedas.
            total_jugadores_de_todos_los_juegos = contador_poker + contador_ruleta + contador_tragamonedas
            porcentaje_tragamonedas = (contador_tragamonedas * 100) / total_jugadores_de_todos_los_juegos

        
        #D) Cuál es el juego menos elegido por los ganadores
        if(contador_poker < contador_tragamonedas and contador_poker < contador_ruleta):
                juego_menos_ganador = "poker"
        elif(contador_tragamonedas < contador_ruleta):
                juego_menos_ganador = "tragamonedas"
        else:
                juego_menos_ganador = "ruleta"

        

        
        promedio_no_poker = acumulador_no_poker / contador_no_poker



        print(nombre_persona_mas_gano, genero_persona_mas_gano)

        print("cantidad ganado en ruleta", promedio_ganado_ruleta)

        print("Porcentaje de personas que jugaron en el Tragamonedas", porcentaje_tragamonedas)

        print("juego menos ganador", juego_menos_ganador)

        print("Promedio de importe ganado de las personas que NO jugaron Poker", promedio_no_poker)








if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
