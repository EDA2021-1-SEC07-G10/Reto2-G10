"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():

    typeofList = "ARRAY_LIST"
    catalog = {"videos": None, "categories": None}
    catalog["videos"] = lt.newList(typeofList, cmpfunction=cmpVideosByViews)
    catalog["categories"] = lt.newList(typeofList, cmpfunction=cmpVideosByViews)

    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(catalog['categories'], category)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son mayores que
    los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (int(video1["views"]) > int(video2["views"]))


# Funciones de ordenamiento


def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los 'likes' de video1 son mayores que
    los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1["likes"]) > int(video2["likes"]))


def firstReq(catalog, data_size, country, category):
    """
    Completa el requerimiento #1
    """
    filtered = catalog.copy()
    i = 1
    t = lt.size(filtered["videos"])
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        if (elem["country"].lower()) != (country.lower()) or elem["category_id"] != category:
            lt.deleteElement(filtered["videos"], i)
            t -= 1
            i -= 1
        i += 1
    sorted_list = quick.sort(filtered["videos"], cmpVideosByViews)
    try:
        data_sublist = lt.subList(sorted_list, 1, data_size)
        data_sublist = data_sublist.copy()
        return data_sublist
    except:
        return sorted_list


def secondReq(catalog, country):
    """
    Completa el requerimiento #2
    """
    dicc = {}
    filtered = catalog.copy()
    i = 1
    t = lt.size(filtered["videos"])
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        if (elem["country"].lower()) != (country.lower()):
            lt.deleteElement(filtered["videos"], i)
            t -= 1
            i -= 1
        i += 1
    i = 1
    t = lt.size(filtered["videos"])
    x = 0
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        titulo = (elem["title"] + "#,@,#" + elem["channel_title"])
        if titulo not in dicc:
            dicc[titulo] = 1
            x += 1
        else:
            dicc[titulo] += 1
        i += 1
    dicc_sort = sorted(dicc.items(), key=operator.itemgetter(1), reverse=True)
    mayor = dicc_sort[0]
    primerosdatos = mayor[0].split("#,@,#")
    resultado = [primerosdatos[0], primerosdatos[1], mayor[1]]
    return resultado


def thirdReq(catalog, category):
    """
    Completa el requerimiento #3
    """
    dicc = {}
    filtered = catalog.copy()
    i = 1
    t = lt.size(filtered["videos"])
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        if elem["category_id"] != category:
            lt.deleteElement(filtered["videos"], i)
            t -= 1
            i -= 1
        i += 1
    i = 1
    t = lt.size(filtered["videos"])
    x = 0
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        titulo = (elem["title"] + "#,@,#" + elem["channel_title"])
        if titulo not in dicc:
            dicc[titulo] = 1
            x += 1
        else:
            dicc[titulo] += 1
        i += 1
    dicc_sort = sorted(dicc.items(), key=operator.itemgetter(1), reverse=True)
    mayor = dicc_sort[0]
    primerosdatos = mayor[0].split("#,@,#")
    resultado = [primerosdatos[0], primerosdatos[1], mayor[1], category]
    return resultado


def fourthReq(catalog, data_size, country, tag):
    """
    Completa el requerimiento #4
    """
    filtered = catalog.copy()
    i = 1
    t = lt.size(filtered["videos"])
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        if (elem["country"].lower()) != (country.lower()) or tag not in elem["tags"]:
            lt.deleteElement(filtered["videos"], i)
            t -= 1
            i -= 1
        i += 1
    sorted_list = quick.sort(filtered["videos"], cmpVideosByLikes)
    try:
        data_sublist = lt.subList(sorted_list, 1, data_size)
        data_sublist = data_sublist.copy()
        return data_sublist
    except:
        return sorted_list
    