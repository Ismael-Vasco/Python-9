import time
import os
from datetime import datetime
import re
import math
from pathlib import Path as path
#inicio
inicio_cod = time.time()

# listas que almacenen el contenido que se necesita
cod_find = []
archivo_cod_encontrado = []
sub_folder = []

# ruta del folder
#ruta = "C:\\PYTHON_TOTAL\\EJERCICIO_DIA_9\\proyecto_dia_9\\Mi_Gran_Directorio"
ruta = "C:\\Users\\Lenovo\\Desktop\Cursos_ISMA\\PYTHON_TOTAL\\EJERCICIO_DIA_9\\proyecto_dia_9"

# Patron -> [N] + [tres carateres de texto] + [-] + [5 números]
patron = r'N\D{3}-\d{5}'

# fecha de hoy en formato dd/mm/aa
hoy = datetime.today()
hoy_formato = f"{hoy.day}/{hoy.month}/{hoy.year}"


# función que busque el ptron dado
def buscador_de_similitudes(archivo, patron):
     doc = open(archivo, "r")
     texto = doc.read()
     if re.search(patron, texto):
          return re.search(patron, texto)
     else:
          return ''


# listas llenas
def listador_finded():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscador_de_similitudes(path(carpeta,a), patron)
            if resultado != '':
                cod_find.append((resultado.group()))
                archivo_cod_encontrado.append(a.title())
     

# función que inicie el programa y entregre el doc organizado
def inicio():
    contador = 0
    print("-"*50)
    print(f"Fecha de búsqueda: [{hoy_formato}]")
    print("\n")
    print("ARCHIVO \t\t NRO. SERIE")
    print("------- \t\t ----------")

    for i in cod_find:
        print(f"{archivo_cod_encontrado[contador]} \t\t {i}")
        contador += 1

    fin = time.time()
    duración = fin - inicio_cod
    print("\n")
    print(f"Número encontrados: {len(cod_find)}")
    print(f"duración de la busqueda: {math.ceil(duración)}")
    print("-"*50)
    








listador_finded()
inicio()

print(cod_find)
print(archivo_cod_encontrado)





