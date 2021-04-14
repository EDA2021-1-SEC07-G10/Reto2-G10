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
from DISClib.DataStructures import mapstructure as mp
#from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf
from DISClib.DataStructures import chaininghashtable as cht


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    catalog = {"videos": None, "categories": None, "info": None}
    catalog["videos"] = mp.newMap(1000000, 1000007, 'PROBING', 0.80, None)
    catalog["categories"] = mp.newMap(36, 37, 'PROBING', 0.80, None)
    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    """
    Esta funcion adiciona un video a la lista de videos teniendo como llave su video_id,
    adicionalmente lo guarda en un Map usando como llave su número de categoría.
    """
    cont = mp.contains(catalog["videos"], video["video_id"])
    if not cont:
        structure = newVideo()
        lt.addLast(structure["videos"], video)
        mp.put(catalog["videos"], video["video_id"], structure)
    else:
        pareja = mp.get(catalog["videos"], video["video_id"])
        llave = pareja["key"]
        valor = pareja["value"]
        lt.addLast(valor["videos"], video)
        mp.put(catalog["videos"], llave, valor)

    for cate in catalog["categories"]["table"]["elements"]:
        if cate["key"] == video["category_id"]:
            space = cate["value"]["videos"]
            lt.addLast(space, video)
    


def addCategory(catalog, category, mapvalue):
    # Se adiciona la categoria al map de categorias
    mp.put(catalog["categories"], category, mapvalue)


# Funciones para creacion de datos


def newVideo():
    video = {'videos': None,
           'count': 0.0}
    video["videos"] = lt.newList()
    return video


def newCategory(name, id):
    """
    Esta estructura crea una relación entre las categorías y videos existentes
    """
    category = {'name': '',
           'category_id': '',
           'videos': None,
           'count': 0.0}
    category['name'] = name
    category['category_id'] = id
    category['videos'] = lt.newList()
    return category

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


def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los 'likes' de video1 son mayores que
    los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1["likes"]) > int(video2["likes"]))


def cmpVideosByTrendingdays(video1, video2):
    return (int(video1["count"]) > int(video2["count"]))


# Funciones principales de requerimientos


def firstReq(catalog, data_size, country, category):
    """
    Completa el requerimiento #1
    """
    for cate in catalog["categories"]["table"]["elements"]:
        try:
            if int(cate["key"]) == int(category):
                info = cate["value"]["videos"]
                break
        except:
            pass

    new_list = lt.newList()
    for video in lt.iterator(info):
        if str(video["country"]).lower() == str(country).lower():
            lt.addLast(new_list, video)
    sorted_list = quick.sort(new_list, cmpVideosByViews)
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
    new_map = mp.newMap(500000, 500000, 'PROBING', 0.80, None)
    for videos in catalog["videos"]["table"]["elements"]:
        if videos["key"] != None:
            for video in lt.iterator(videos["value"]["videos"]):
                if str(video["country"]).lower() == str(country).lower():
                    value = {"title": video["title"], "channel": video["channel_title"], "count": 1}
                    key = video["title"]
                    exists = mp.contains(new_map, key)
                    if not exists:
                        mp.put(new_map, key, value)
                    else:
                        old_value = mp.get(new_map, key)
                        new_value = old_value["value"]["count"] = int(old_value["value"]["count"]) + 1
                        mp.put(new_map, key, new_value)
    
    new_list = lt.newList()
    for element in new_map["table"]["elements"]:
        if element["key"] != None:
            lt.addLast(new_list, element["value"])
    sorted_list = quick.sort(new_list, cmpVideosByTrendingdays)
    result = lt.firstElement(sorted_list)
    result["country"] = country

    return result


def thirdReq(catalog, category):
    """
    Completa el requerimiento #3
    """
    for cate in catalog["categories"]["table"]["elements"]:
        try:
            if int(cate["key"]) == int(category):
                info = cate["value"]["videos"]
                break
        except:
            pass
    new_map = mp.newMap(500000, 500000, 'PROBING', 0.80, None)
    i = 1
    t = lt.size(info)
    x = 0
    while i <= t:
        elem = lt.getElement(info, i)
        value = {"title": elem["title"], "channel": elem["channel_title"], "count": 1}
        key = elem["title"]
        exists = mp.contains(new_map, key)
        if not exists:
            mp.put(new_map, key, value)
        else:
            old_value = mp.get(new_map, key)
            key = elem["title"]
            new_value = old_value["value"]["count"] = int(old_value["value"]["count"]) + 1
            mp.put(new_map, key, new_value)
        i += 1

    new_list = lt.newList()
    for element in new_map["table"]["elements"]:
        if element["key"] != None:
            lt.addLast(new_list, element["value"])
    sorted_list = quick.sort(new_list, cmpVideosByTrendingdays)
    result = lt.firstElement(sorted_list)
    result["cat"] = category

    return result


def fourthReq(catalog, data_size, country, tag):
    """
    Completa el requerimiento #4
    """
    info = catalog["videos"]["table"]["elements"]
    new_list = lt.newList()
    for videos in info:
        if videos["key"] != None:
            for video in lt.iterator(videos["value"]["videos"]):
                if (str(video["country"]).lower() == str(country).lower()) and ((str(tag)).lower() in (str(video["tags"])).lower()):
                    lt.addLast(new_list, video)
    sorted_list = quick.sort(new_list, cmpVideosByLikes)
    try:
        data_sublist = lt.subList(sorted_list, 1, data_size)
        data_sublist = data_sublist.copy()
        return data_sublist
    except:
        return sorted_list