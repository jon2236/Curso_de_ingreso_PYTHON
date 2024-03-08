import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
DNI: 32484284
Nombre: Jonatan Oscar
apellido: Quiroga
Turno: Mañana
-----------------------------------------------------------------------------------------------------------------------------------

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

-Nombre
-Edad (debe ser mayor a 12)
-Altura (no debe ser negativa)
-Días que asiste a la semana (1, 3, 5)
-Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
A) El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
B) El porcentaje de clientes que asiste solo 1 día a la semana.
C) Nombre y edad del cliente con más altura.
D) Determinar si los clientes eligen más ir 1, 3 o 5 días
E) Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.


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
        flag_cliente_mas_alto = True

        contador_1_dia = 0
        contador_3_dia = 0
        contador_5_dia = 0

        acumulador_kilos_personas_q_van_3_dias = 0

        total_asistencia_semanal = 0

        cliente_mas_alto_nombre_y_edad = 0

        persona_mas_joven = 0
        flag_persona_mas_joven = True
        nombre_persona_mas_joven = ""
        cantidad_kilos_mas_joven = ""




        while(continuar == True):

            nombre = prompt("NOMBRE", "ingrese su nombre")
            print(nombre)

            edad = prompt("EDAD", "ingrese su edad")
            edad = int(edad)
            while(edad < 12):
                edad = prompt("ERROR", "REingrese su edad")
                edad = int(edad)
            print(edad)

            altura = prompt("ALTURA", "ingrese su altura")
            altura = float(altura)
            while(altura < 0):
                altura = prompt("ERROR", "REingrese su altura")
                altura = float(altura)
            print(altura)
            
            dias_de_asistencia = prompt("ASISTENCIA", "ingrese cantidad de dias de asistencia: 1, 3, 5")
            while(dias_de_asistencia != "1" and dias_de_asistencia != "3" and dias_de_asistencia != "5"):
                dias_de_asistencia = prompt("ERROR", "REingrese una cantidad de dias correcta: 1, 3, 5")
            print(dias_de_asistencia)

            kilos_peso_muerto = prompt("KILOS PESO MUERTO", "ingrese kilos q levanta en peso muerto")
            kilos_peso_muerto = int(kilos_peso_muerto)
            while(kilos_peso_muerto < 1):
                kilos_peso_muerto = prompt("ERROR", "REingrese sus kilos q levanta en peso muerto")
                kilos_peso_muerto = int(kilos_peso_muerto)
            print(kilos_peso_muerto)




            match(dias_de_asistencia):
                case "1":
                    contador_1_dia += 1
                case "3":
                    contador_3_dia += 1
                    acumulador_kilos_personas_q_van_3_dias += kilos_peso_muerto #1
                case "5":
                    contador_5_dia += 1
                    if(edad < persona_mas_joven or flag_persona_mas_joven == True):#Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
                        persona_mas_joven = edad
                        nombre_persona_mas_joven = nombre
                        cantidad_kilos_mas_joven = kilos_peso_muerto
                        flag_persona_mas_joven = False




                        
            #3 Nombre y edad del cliente con más altura.
            if(altura > cliente_mas_alto_nombre_y_edad or flag_cliente_mas_alto == True):
                cliente_mas_alto_nombre = nombre
                cliente_mas_alto_edad = edad
                flag_cliente_mas_alto = False



            continuar = question("continuar", "continuar?")



        

        if(contador_3_dia > 0):
            promedio_kilos_levantas_3_dias_semanales = acumulador_kilos_personas_q_van_3_dias / contador_3_dia #1
            print("promedio_kilos_levantas_3_dias_semanales", promedio_kilos_levantas_3_dias_semanales)




        #2El porcentaje de clientes que asiste solo 1 día a la semana.
        total_asistencia_semanal = contador_1_dia + contador_3_dia + contador_5_dia

        porcentaje_personas_1_dia = (contador_1_dia * 100) / total_asistencia_semanal
        print("porcentaje_personas_1_dia", porcentaje_personas_1_dia)

        print("cliente_mas_alto_nombre_y_edad", cliente_mas_alto_nombre, cliente_mas_alto_edad)




        #4
        if(contador_1_dia > contador_3_dia and contador_1_dia > contador_5_dia):
            dia_mas_concurrido = "1 dia semanal"
        elif(contador_3_dia > contador_5_dia):
            dia_mas_concurrido = "3 dias semanales"
        else:
            dia_mas_concurrido = "5 dias semanales"
        print("asistencia preferida", dia_mas_concurrido)




        #5Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
        print("persona mas joven ", nombre_persona_mas_joven)
        print("kilos peso muerto del mas joven", cantidad_kilos_mas_joven)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()