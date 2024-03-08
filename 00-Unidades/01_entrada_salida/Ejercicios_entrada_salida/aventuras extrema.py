import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Jonatan Oscar
apellido: Quiroga
Turno: Mañana
-----------------------------------------------------------------------------------------------------------------------------------

En el parque de diversiones "Aventuras Extremas", un grupo de 10 amigos ha
decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un
restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden
crear un programa para calcular y dividir los gastos de manera equitativa.
Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo (pedir por prompt)

Nombre del amigo,
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
Cantidad de platos principales pedidos (debe ser al menos 1).
Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 1).


Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $3000.

El precio unitario de cada bebida es de $1000.


Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por print):

Informar cual fue el tipo de bebida más vendida.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas,
30% hamburguesas]
Informar la cantidad total de bebidas que fueron “Refresco”.
El promedio gastado en platos principales de tipo “Pizza” sobre el grupo de amigos en general.
El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”

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

        flag_primer_ingreso_hamburguesa = True



        precio_plato_principal = 3000
        precio_bebida = 1000

        contador_refresco = 0
        contador_agua = 0
        contador_jugo = 0

        contador_pizza = 0
        contador_hamburguesa = 0
        contador_ensalada = 0
        total_platos_principales = 0

        cantidad_pizza = 0
        cantidad_hamburguesa = 0
        cantidad_ensalada = 0

        acumulador_refresco = 0
        acumulador_agua = 0
        acumulador_jugo = 0

        gasto_total_pizza = 0

        nombre_menor_cantidad_hamburgesa = ""
        cantidad_minima_hamburguesa = 0

        while(continuar == True):

            nombre = prompt("NOMBRE", "ingrese su nombre")
            print(nombre)

            plato_principal = prompt("PLATO PRINCIPAL", "ingrese un plato principal; pizza, hamburguesa, ensalada")
            while(plato_principal != "pizza" and plato_principal != "hamburguesa" and plato_principal != "ensalada"):
                plato_principal = prompt("ERROR", "REingrese un plato principal valido; pizza, hamburguesa, ensalada")
            print(plato_principal)
            
            cantidad_plato_principal = prompt("CANTIDAD", "elija la cantidad a llevar de su plato principal")
            cantidad_plato_principal = int(cantidad_plato_principal)
            while(cantidad_plato_principal < 1):
                cantidad_plato_principal = prompt("ERROR", "REingrese una cantidad valida")
                cantidad_plato_principal = int(cantidad_plato_principal)
            print(cantidad_plato_principal)
            
            bebida = prompt("BEBIDA", "ingrese su bebida; refresco, agua, jugo")
            while(bebida != "refresco" and bebida != "agua" and bebida != "jugo"):
                bebida = prompt("ERROR", "REingrese una bebida valida; refresco, agua, jugo")
            print(bebida)

            cantidad_bebida = prompt("CANTIDAD", "elija la cantidad a llevar de bebidas")
            cantidad_bebida = int(cantidad_bebida)
            while(cantidad_bebida < 1):
                cantidad_bebida = prompt("ERROR", "REingrese una cantidad valida")
                cantidad_bebida = int(cantidad_bebida)
            print(cantidad_bebida)







            match(bebida):
                case "refresco":
                    contador_refresco += 1
                    acumulador_refresco += cantidad_bebida
                case "agua":
                    contador_agua += 1
                    acumulador_agua += cantidad_bebida
                case "jugo":
                    contador_jugo += 1
                    acumulador_jugo += cantidad_bebida



            

            match(plato_principal):
                case "pizza":
                    contador_pizza += cantidad_plato_principal
                case "hamburguesa":
                    contador_hamburguesa += cantidad_plato_principal
                    if(cantidad_hamburguesa < cantidad_minima_hamburguesa or flag_primer_ingreso_hamburguesa == True): #El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”
                        nombre_menor_cantidad_hamburgesa = nombre
                        flag_primer_ingreso_hamburguesa = False
                case "ensalada":
                    contador_ensalada += cantidad_plato_principal







            continuar = question("continuar", "desea continuar?")



        if(acumulador_refresco > acumulador_agua and acumulador_refresco > acumulador_jugo):
            bebida_mas_vendida = "refresco"
        elif(acumulador_agua > acumulador_jugo):
            bebida_mas_vendida = "agua"
        else:
            bebida_mas_vendida = "jugo"
        






        total_platos_principales = contador_pizza + contador_hamburguesa + contador_ensalada

        porcentaje_pizza = (contador_pizza * 100) / total_platos_principales
        porcentaje_hamburguesa = (contador_hamburguesa * 100) / total_platos_principales
        porcentaje_ensalada = (contador_ensalada * 100) / total_platos_principales





        promedio_gastado_pizza = (contador_pizza * precio_plato_principal) / 10

        
        print("los porcentajes de cada plato es: pizza {0} hamburguesa {1} ensalda {2}".format(porcentaje_pizza, porcentaje_hamburguesa, porcentaje_ensalada))
        print("cantidad de refrescos vendidos ", acumulador_refresco)
        print("nombre de la persona q menos hamburguesas pidio", nombre_menor_cantidad_hamburgesa)
        print("promedio gastado en el total de pizzas", promedio_gastado_pizza)
        print("la bebida mas vendida fue ", bebida_mas_vendida)
        


        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()