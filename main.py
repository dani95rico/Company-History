##################################################################################################
# IMPORTER LIBRARIES && CLASSES
##################################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pandas import ExcelWriter
from openpyxl import Workbook
import os
from datetime import date
from datetime import datetime


##################################################################################################
# MENU OPTIONS
##################################################################################################

#  1 - LISTA LOS ATRIBUTOS DE LAS EMPRESAS
def listar_empresas():
    nombres = pd.read_excel("C:/Users/danir/PycharmProjects/Bolsa/datos/nombres.xlsx")
    print(nombres["nombres"])


#  2 - LISTA LAS EMPRESAS REGISTRADAS
def listar_atributos():
    atributos = pd.read_excel("C:/Users/danir/PycharmProjects/Bolsa/datos/nombres.xlsx")
    print(atributos["atributos"])


#  3 - AÑADE UNA EMPRESA NUEVA
def añadir_empresa():
    try:
        nombre = input("Introduzca nombre de la empresa: ")
        atributos = ["FECHA", "ACCIONESEMPLEADOS", "DINERO", "PORTCENTAJE", "DIVISAS"]

        data = pd.DataFrame(columns=atributos)
        data.to_excel("datos/" + nombre + ".xlsx", sheet_name="hoja1")
    except:
        print("Alo ha salido mal 1")
    finally:
        print("Finaliza el try")


#  4 - MUESTRA LOS DATOS DE UN ATRIBUTO ELEGIDO DE UNA EMPRESA REGISTRADA
def mostrar_datos_atributo_empresa():
    try:
        nombre = input("Introduzca nombre de la empresa a buscar: ")
        if encontrar_empresa(nombre):
            try:
                df = pd.read_excel("datos/" + nombre + ".xlsx")
                atributo = input("Introduzca atributo de la empresa " + nombre + ":")
                print(df[atributo])
            except:
                print("No existe tal atributo")
    except:
        print("Alo ha salido mal")
    finally:
        print("Finaliza el try")


#  5 - MUESTRA TODOS LOS DATOS DE UNA EMPRESA REGISTRADA
def listar_datos_empresa():
    try:
        nombre = input("Introduzca nombre de la empresa a buscar: ")

        if encontrar_empresa(nombre):
            df = pd.read_excel("datos/" + nombre + ".xlsx")
            print(df)
    except:
        print("Alo ha salido mal")
    finally:
        print("Finaliza el try")


#  6 - MUESTRA LOS ATRIBUTOS DE UNA EMPRESA REGISTRADA
def mostrar_atributos():
    try:
        nombre = input("Introduzca nombre de la empresa a buscar: ")
        if encontrar_empresa(nombre):
            df = pd.read_excel("datos/" + nombre + ".xlsx")
            print(df.keys())
    except:
        print("Alo ha salido mal")
    finally:
        print("Finaliza el try")


#  7 - MUESTRA DATOS DE UN ATRIBUTO DESDE UNA FECHA ELEGIDA
def datos_atributo_fecha():
    print()


#  8 - MUESTRA DATOS DE UN ATRIBUTO ENTRE RANGO DE FECHAS
def datos_atributo_rango_fechas():
    print()


#  9 - MUESTRA GRÁFICA DE DATOS DE UN ATRIBUTO EN EL TIEMPO
def grafica_datos_t():
    print()


# 10 - ESCRIBE DATOS A UNA EMPRESA
def escribir_datos(datos):
    nombre = input("Introduzca nombre de la empresa a buscar: ")
    if encontrar_empresa(nombre):
        atributo = input("Introduzca atributo de la empresa: ")
        if encontrar_atributo(nombre, atributo):
            df = pd.read_excel("datos/" + nombre + ".xlsx")
            df_total = pd.concat(df[atributo], datos)


##################################################################################################
# BASIC FUNCTIONS
##################################################################################################

# ENCUENTRA UNA EMPRESA QUE EXISTA (REGISTRADA)
def encontrar_empresa(nombre):
    try:
        correcto = True
        df = pd.read_excel("datos/" + nombre + ".xlsx")
        return correcto
    except:
        print("No se ha encontrado la empresa llamada: " + nombre)
        correcto = False
        return correcto
    finally:
        print("Finaliza el try")


# ENCUENTRA UN ATRIBUTO DE UNA EMPRESA QUE EXISTA (REGISTRADA)
def encontrar_atributo(nombre, atributo):
    try:
        correcto = False
        df = pd.read_excel("datos/" + nombre + ".xlsx")
        if nombre[atributo]:
            correcto = True
        return correcto
    except:
        print("No se ha encontrado el atributo de la empresa : " + nombre)
    finally:
        print("Finaliza el try")


# DEVUELVE EL MOMENTO ACTUAL
def now():
    try:
        now = datetime.now()
        return now
    except:
        print("Alo ha salido mal")
    finally:
        print("Finaliza el try")


# CREA EL DRIVE DEL NAVEGADOR
def crear_driver():
    try:
        print()
    # driver = webdriver.Chrome(executable_path="C:\Users\danir\OneDrive\Escritorio\ESCRITORIO\PROGRAMACIÓN\Chrome_WebDriver")
    except:
        print("Alo ha salido mal")
    finally:
        print("Finaliza el try")


# MENU
def menu():
    out = False
    clear = lambda: os.system("cls")
    menu = """
                                                      *****************************
                                                    *********************************
                                                  ***************************+*********
                                                *****************************************

                                                                  MENU
                        1- Listar empresas                                        8- mostrar datos atributo con rango de fechas
                        2- Listar nombres de atributos                            9- Mostrar gráfica datos de un atributo (t)
                        3- Añadir empresa
                        4- Mostras datos de un atributo de una empresa
                        5- Listar todos los datos de una empresa
                        6- Mostrar atributos de una empresa
                        7- Mostrar datos atributos desde fecha 

                                                               20- SALIR
                                                ******************************************
                                                  *************************************
                                                    ***************************+*****
                                                      *****************************

            """
    while (not out):
        print(menu)
        try:
            election = int(input("Eliga una opción: "))
        except:
            election = 0
        clear()
        if election == 1:
            listar_empresas()
        elif election == 2:
            listar_atributos()
        elif election == 3:
            añadir_empresa()
        elif election == 4:
            mostrar_datos_atributo_empresa()
        elif election == 5:
            listar_datos_empresa()
        elif election == 6:
            mostrar_atributos()
        elif election == 7:
            datos_atributo_fecha()
        elif election == 8:
            datos_atributo_rango_fechas()
        elif election == 9:
            grafica_datos_t()



        elif election == 20:
            print("PROGRAMA FINALIZADO: UN SALUDO")
            out = True
        else:
            print("ERROR: no existe esa opción")

        input("FUNCIÓN FINALIZADA: PRESIONE ENTER PARA CONTINUAR")
        clear()


##################################################################################################
# MAIN
##################################################################################################
if __name__ == "__main__":
    menu()
