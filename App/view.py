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
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("------------------------------------------------------")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    #print("2- Req. 1: Consultar n videos con más views en un país, por categoría")
    #print("3- Req. 2: Consultar video que más días ha sido trending en un país")
    #print("4- Req. 3: Consultar video que más dias ha sido trending, por categoría")
    #print("5- Req. 4: Consultar n videos con más likes en un país, por tag")
    #print("0- Salir")


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
    print("------------------------------------------------------")
    print("Título: " + info[0])
    print("Canal: " + info[1])
    print("Número de días como tendencia: " + str(info[2]))


def printVideoInfo3(info):
    """
    Imprime la información principal de un video
    """
    print("------------------------------------------------------")
    print("Título: " + info[0])
    print("Canal: " + info[1])
    print("Identificador de categoría: " + str(info[3]))
    print("Número de días como tendencia: " + str(info[2]))


def printVideoInfo4(video):
    """
    Imprime la información principal de un video
    """
    print("------------------------------------------------------")
    print("Título: " + video["title"])
    print("Canal: " + video["channel_title"])
    print("Fecha de publicación: " + video["publish_time"])
    print("Cantidad de reproducciones: " + video["views"])
    print("Cantidad de Likes: " + video["likes"])
    print("Cantidad de Dislikes: " + video["dislikes"])
    print("Tags: " + video["tags"])


def printCategoriesList(catalog):
    "Imprime la lista de categorías"
    for category in lt.iterator(catalog['categories']):
        idpluscategory = category["id\tname"].split("\t ")
        print(idpluscategory[0], idpluscategory[1])


def askForDataSize(catalog):
    """
    Pregunta al usuario el tamaño de la muestra a comparar y valida la cantidad
    """
    data_size = int(input("Número de videos que se quiere listar: "))
    if data_size > int(lt.size(catalog['videos'])):
        print("Error: valor excede tamaño de los datos cargados.")
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
    return controller.secondReq(catalog,country)


def thirdReq(catalog, category):
    """
    Solicita al controller la información del requerimiento 3
    """
    return controller.thirdReq(catalog, category)


def fourthReq(catalog, data_size, country, tag):
    """
    Solicita al controller la información del requerimiento 3
    """
    return controller.fourthReq(catalog, data_size, country, tag)


catalog = None
"""
"""
# Menu principal

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        mediciones = loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print("Información sobre el primer video cargado:\n")
        video = lt.firstElement(catalog["videos"])
        printVideoInfo(video)
        print("Las categorías cargadas y sus id son:")
        printCategoriesList(catalog)
        print("")
        print("Resultados prueba ---------------------------------------------------------")
        print("Tiempo [ms]: ", f"{mediciones[0]:.3f}", " || ", "Memoria [kB]: ", f"{mediciones[1]:.3f}")
        print("")
        
        

    elif int(inputs[0]) == 2:
        print("------------------------------------------------------")
        print("Req. #1: Consultar n videos con más views en un país, por categoría")
        data_size = askForDataSize(catalog)
        country = input("Indique el país: " )
        category = input("Indique la categoría: ")
        result = firstReq(catalog, data_size, country, category)
        for video in result["elements"]:
            printVideoInfo1(video)

    elif int(inputs[0]) == 3:
        print("------------------------------------------------------")
        print("Req. #2: Consultar video que más días ha sido trending en un país")
        country = input("Indique el país: ")
        result = secondReq(catalog, country)
        printVideoInfo2(result)
    
    elif int(inputs[0]) == 4:
        print("------------------------------------------------------")
        print("Req. #3: Consultar video que más dias ha sido trending, por categoría")
        category = input("Indique la categoría: ")
        result = thirdReq(catalog, category)
        printVideoInfo3(result)
    

    elif int(inputs[0]) == 5:
        print("------------------------------------------------------")
        print("Req. #4: Consultar n videos con más likes en un país, por tag")
        data_size = askForDataSize(catalog)
        country = input("Indique el país: " )
        tag = str(input("Indique el tag: " ))
        result = fourthReq(catalog, data_size, country, tag)
        for video in result["elements"]:
            printVideoInfo4(video)

    else:
        sys.exit(0)
sys.exit(0)