"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapstructure as mp
import time
import tracemalloc
assert cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("")
    print("******************************************************")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req. 1: Consultar n videos con más views en un país, por categoría")
    print("3- Req. 2: Consultar video que más días ha sido trending en un país")
    print("4- Req. 3: Consultar video que más dias ha sido trending, por categoría")
    print("5- Req. 4: Consultar n videos con más likes en un país, por tag")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catálogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    return controller.loadData(catalog)


def printVideoInfo(video):
    """
    Imprime la información principal de un video
    """
    #TODO: Eliminar o ajustar
    print("------------------------------------------------------")
    print("Título: " + video["title"])
    print("Canal: " + video["channel_title"])
    print("Fecha en que fue trending: " + video["trending_date"])
    print("País: " + video["country"])
    print("Cantidad de vistas: " + video["views"])
    print("Cantidad de Likes: " + video["likes"])
    print("Cantidad de Dislikes: " + video["dislikes"])


def printVideoInfo1(video):
    """
    Imprime la información principal de un video
    """
    #TODO: Eliminar o ajustar
    print("------------------------------------------------------")
    print("Título: " + video["title"])
    print("Canal: " + video["channel_title"])
    print("Fecha en que fue trending: " + video["trending_date"])
    print("Fecha de publicación: " + video["publish_time"])
    print("Cantidad de reproducciones: " + video["views"])
    print("Cantidad de Likes: " + video["likes"])
    print("Cantidad de Dislikes: " + video["dislikes"])


def printVideoInfo2(info):
    """
    Imprime la información principal de un video
    """
    #TODO: Eliminar o ajustar
    print("------------------------------------------------------")
    print("Título: " + info["title"])
    print("Canal: " + info["channel"])
    print("País: " + str(info["country"]))
    print("Número de días como tendencia: " + str(info["count"]))

def printVideoInfo3(info):
    """
    Imprime la información principal de un video
    """
    #TODO: Eliminar o ajustar
    print("------------------------------------------------------")
    print("Título: " + info["title"])
    print("Canal: " + info["channel"])
    print("Identificador de categoría: " + str(info["cat"]))
    print("Número de días como tendencia: " + str(info["count"]))


def printVideoInfo4(video):
    """
    Imprime la información principal de un video
    """
    #TODO: Eliminar o ajustar
    print("------------------------------------------------------")
    print("Título: " + video["title"])
    print("Canal: " + video["channel_title"])
    print("Fecha de publicación: " + video["publish_time"])
    print("Cantidad de reproducciones: " + video["views"])
    print("Cantidad de Likes: " + video["likes"])
    print("Cantidad de Dislikes: " + video["dislikes"])
    print("Tags: " + video["tags"])


def askForDataSize(catalog):
    """
    Pregunta al usuario el tamaño de la muestra a comparar y valida la cantidad
    """
    #TODO: Eliminar o ajustar
    data_size = int(input("Número de videos que se quiere listar: "))
    if data_size > int(catalog["info"]["cantidad_videos"]):
        print("> Error: valor excede tamaño de los datos cargados.")
        print("> Tip: Intente con un valor más pequeño o ejecute la opción 1 nuevamente antes de intentarlo.")
        askForDataSize(catalog)
    else:
        return data_size


def firstReq(catalog, data_size, country, category):
    """
    Solicita al controller la información del requerimiento 1
    """
    return controller.firstReq(catalog, data_size, country, category)


def secondReq(catalog, country):
    """
    Solicita al controller la información del requerimiento 2
    """
    #TODO: Eliminar o ajustar
    return controller.secondReq(catalog,country)


def thirdReq(catalog, category):
    """
    Solicita al controller la información del requerimiento 3
    """
    #TODO: Eliminar o ajustar
    return controller.thirdReq(catalog, category)


def fourthReq(catalog, data_size, country, tag):
    """
    Solicita al controller la información del requerimiento 3
    """
    #TODO: Eliminar o ajustar
    return controller.fourthReq(catalog, data_size, country, tag)


catalog = None
"""
"""
# Menu principal

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        print("")
        print("******************************************************")
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        mediciones = loadData(catalog)
        print("Total de categorías cargadas: " + str(catalog["categories"]["size"]))
        print('Total de videos cargados: ' + str(catalog["info"]["cantidad_videos"]))       

    elif int(inputs[0]) == 2:
        print("")
        print("******************************************************")
        print("Req. #1: Consultar n videos con más views en un país, por categoría")
        data_size = askForDataSize(catalog)
        country = input("Indique el país: " )
        category = input("Indique la categoría: ")

        tracemalloc.start()
        delta_time = -1.0
        delta_memory = -1.0
        start_time = controller.getTime()
        start_memory = controller.getMemory()
        result = firstReq(catalog, data_size, country, category)
        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        mediciones = [delta_time, delta_memory]

        for video in lt.iterator(result):
            printVideoInfo1(video)
        
        print("------------------------------------------------------")
        print("> Tiempo y memoria consumidos:")
        print("> Tiempo [ms]: ", f"{mediciones[0]:.3f}", " || ", "Memoria [kB]: ", f"{mediciones[1]:.3f}") 

    elif int(inputs[0]) == 3:
        print("")
        print("******************************************************")
        print("Req. #2: Consultar video que más días ha sido trending en un país")
        country = input("Indique el país: ")

        tracemalloc.start()
        delta_time = -1.0
        delta_memory = -1.0
        start_time = controller.getTime()
        start_memory = controller.getMemory()
        result = secondReq(catalog, country)
        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        mediciones = [delta_time, delta_memory]

        printVideoInfo2(result)

        print("------------------------------------------------------")
        print("> Tiempo y memoria consumidos:")
        print("> Tiempo [ms]: ", f"{mediciones[0]:.3f}", " || ", "Memoria [kB]: ", f"{mediciones[1]:.3f}") 
    
    elif int(inputs[0]) == 4:
        print("")
        print("******************************************************")
        print("Req. #3: Consultar video que más dias ha sido trending, por categoría")
        category = input("Indique la categoría: ")

        tracemalloc.start()
        delta_time = -1.0
        delta_memory = -1.0
        start_time = controller.getTime()
        start_memory = controller.getMemory()        
        result = thirdReq(catalog, category)
        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        mediciones = [delta_time, delta_memory]

        printVideoInfo3(result)
    
        print("------------------------------------------------------")
        print("> Tiempo y memoria consumidos:")
        print("> Tiempo [ms]: ", f"{mediciones[0]:.3f}", " || ", "Memoria [kB]: ", f"{mediciones[1]:.3f}")  

    elif int(inputs[0]) == 5:
        print("")
        print("******************************************************")
        print("Req. #4: Consultar n videos con más likes en un país, por tag")
        data_size = askForDataSize(catalog)
        country = input("Indique el país: " )
        tag = str(input("Indique el tag: " ))

        tracemalloc.start()
        delta_time = -1.0
        delta_memory = -1.0
        start_time = controller.getTime()
        start_memory = controller.getMemory() 
        result = fourthReq(catalog, data_size, country, tag)
        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        mediciones = [delta_time, delta_memory]

        for video in lt.iterator(result):
            printVideoInfo4(video)
        
        print("------------------------------------------------------")
        print("> Tiempo y memoria consumidos:")
        print("> Tiempo [ms]: ", f"{mediciones[0]:.3f}", " || ", "Memoria [kB]: ", f"{mediciones[1]:.3f}")         

    else:
        print("")
        print("¡Hasta pronto!")
        print("")
        sys.exit(0)
sys.exit(0)