import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio_lampara = 800

        descuento_del_50 = (precio_lampara * 50) / 100
        resultado_descuento_50 = precio_lampara - descuento_del_50

        descuento_del_40 = (precio_lampara * 40) / 100
        resultado_descuento_40 = precio_lampara - descuento_del_40
        
        descuento_del_30 = (precio_lampara * 30) / 100
        resultado_descuento_30 = precio_lampara - descuento_del_30
        
        descuento_del_25 = (precio_lampara * 25) / 100
        resultado_descuento_25 = precio_lampara - descuento_del_25
        
        descuento_del_20 = (precio_lampara * 20) / 100
        resultado_descuento_20 = precio_lampara - descuento_del_20
        
        descuento_del_15 = (precio_lampara * 15) / 100
        resultado_descuento_15 = precio_lampara - descuento_del_15

        descuento_del_10 = (precio_lampara * 10) / 100
        resultado_descuento_10 = precio_lampara - descuento_del_10

        descuento_del_5 = (precio_lampara * 5) / 100
        resultado_descuento_5 = precio_lampara - descuento_del_5

        if (cantidad >= 6):
            alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 50%".format(resultado_descuento_50))

        elif (cantidad == 5 and marca == "ArgentinaLuz"):
            alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 40%".format(resultado_descuento_40))
            if (cantidad == 5 and marca != "ArgentinaLuz"):
                alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 30%".format(resultado_descuento_30))

        elif (cantidad == 4 and marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
            alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 25%".format(resultado_descuento_25))
            if (cantidad == 4 and marca != "ArgentinaLuz" or marca != "FelipeLamparas"):
                 alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 20%".format(resultado_descuento_20))

        elif(cantidad == 3 and marca == "ArgentinaLuz"):
            alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 15%".format(resultado_descuento_15))
            if(cantidad == 3 and marca == "FelipeLamparas"):
                alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 10%".format(resultado_descuento_10))
            else:
                alert("precio de cada lampara", "su pedido tiene un precio por lampara de {0} aplicando un descuento del 5%".format(resultado_descuento_5))
        
        


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()