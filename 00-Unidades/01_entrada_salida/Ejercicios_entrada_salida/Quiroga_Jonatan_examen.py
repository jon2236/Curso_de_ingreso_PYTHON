import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Examen Ingreso UTN 2024
DNI: 32484284
Nombre: Jonatan Oscar
apellido: Quiroga
Turno: Mañana
-----------------------------------------------------------------------------------------------------------------------------------
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo mas ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre de la mascota más pesada
Informe D- El sexo y nombre del gato más viejo
Informe E- El promedio de edad de todas las mascotas


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
        flag_mascota_mas_pesada = True
        flag_gato_mas_viejo = True

        contador_masculino = 0
        contador_femenino = 0

        contador_perro = 0
        contador_gato = 0
        contador_exotico = 0

        total_tipo_mascota = 0

        maximo_peso_mascota = 0

        edad_gato_mas_viejo = 0

        cantidad_edad_perro = 0
        cantidad_edad_gato = 0
        cantidad_edad_exotico = 0
        contador_total_mascotas = 0
        edad_todas_las_mascotas = 0

        





        while(continuar == True):

            nombre = prompt("NOMBRE", "ingrese su nombre")
            print(nombre)

            tipo = prompt("TIPO", "ingrese su tipo: gato, perro, exotico")
            while(tipo != "gato" and tipo != "perro" and tipo != "exotico"):
                tipo = prompt("ERROR", "REingrese un tipo valido: gato, perro, exotico")
            print(tipo)

            peso = prompt("PESO", "ingrese su peso")
            peso = float(peso)
            while(peso < 10 and peso > 80):
                peso = prompt("ERROR", "REingrese un peso valido, entre 10 y 80 kg")
                peso = float(peso)
            print(peso)

            edad = prompt("EDAD", "ingrese su edad")
            edad = int(edad)
            while(edad < 1):
                edad = prompt("ERROR", "REingrese una edad valida edad")
                edad = int(edad)
            print(edad)
            
            sexo = prompt("SEXO", "ingrese el sexo: masculino, femenino")
            while(sexo != "masculino" and sexo != "femenino"):
                sexo = prompt("ERROR", "REingrese un sexo valido: masculino, femenino")
            print(sexo)



            #1
            match(sexo):
                case "masculino":
                    contador_masculino += 1
                case "femenino":
                    contador_femenino += 1






            #2
            match(tipo):
                case "perro":
                    contador_perro += 1
                    cantidad_edad_perro += edad
                case "gato":
                    contador_gato += 1
                    cantidad_edad_gato += edad
                case "exotico":
                    contador_exotico += 1
                    cantidad_edad_exotico += edad




            #3
            if(peso > maximo_peso_mascota or flag_mascota_mas_pesada == True):
                maximo_peso_mascota = peso
                nombre_mascota_mas_pesada = nombre
                flag_mascota_mas_pesada = False




            #4
            if(tipo == "gato" and (edad > edad_gato_mas_viejo or flag_gato_mas_viejo == True)):
                edad_gato_mas_viejo = edad
                nombre_gato_mas_viejo = nombre
                sexo_gato_mas_viejo = sexo
                flag_gato_mas_viejo = False




            #5Informe E- El promedio de edad de todas las mascotas



            continuar = question("continuar", "continuar?")



        if(contador_masculino > contador_femenino):
            genero_mas_ingresado = "genero masculino"
        else:
            genero_mas_ingresado = "genero femenino"






        total_tipo_mascota = contador_perro + contador_gato + contador_exotico
        
        porcentaje_perro = (contador_perro * 100) / total_tipo_mascota
        porcentaje_gato = (contador_gato * 100) / total_tipo_mascota
        porcentaje_exotico = (contador_exotico * 100) / total_tipo_mascota





        edad_todas_las_mascotas = cantidad_edad_perro + cantidad_edad_gato + cantidad_edad_exotico
        contador_total_mascotas = contador_perro + contador_gato + contador_exotico
        promedio_total_edad_mascotas = edad_todas_las_mascotas / contador_total_mascotas



        

        print("genero mas ingresado ", genero_mas_ingresado)

        print("la cantidad de promedio de perros es ", porcentaje_perro)
        print("la cantidad de promedio de gatos es", porcentaje_gato)
        print("la cantidad de promedio de exoticos es ", porcentaje_exotico)

        print("el nombre de la mascota mas pesada es ", nombre_mascota_mas_pesada)

        print("El sexo y nombre del gato más viejo", sexo_gato_mas_viejo, nombre_gato_mas_viejo)

        print("El promedio de edad de todas las mascotas", promedio_total_edad_mascotas)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
