﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos


def initCatalog():

    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y estos a la estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):

    videosfile = (cf.data_dir + 'videos-small.csv').replace("\\","/")
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def findCategoryName(catalog, category):
    for cat in catalog["categories"]["elements"]:
        number = category['id\tname'][0].replace("\\", "")
        if (number) in cat['id\tname']:
            contents = cat['id\tname'].split("\t")
            category_name = contents[1]
            category_name = category_name.replace(" ", "")
            category_id = contents[0]
    return (category_name, category_id)

def loadCategories(catalog):

    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory1(catalog, category)
        cat_contents = findCategoryName(catalog, category)
        cat_name = cat_contents[0]
        cat_id = cat_contents[1]
        result = model.newCategory(cat_name, cat_id)
        model.addCategory2(catalog, cat_name, result)
    model.fixCategoriesMap(catalog)
    

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


def findCategoryId(catalog, category):
    for cat in catalog["categories"]["elements"]:
        print(category)
        if (category.title()) in cat['id\tname']:
            contents = cat['id\tname'].split("\t")
            category_id = contents[0]
    return category_id


def firstReq(catalog, data_size, country, category):
    """
    Solicita al model la información del requerimiento #1
    """
    idcat = findCategoryId(catalog, category)
    return model.firstReq(catalog, data_size, country, idcat)


def secondReq(catalog, country):
    """
    Solicita al model la información del requerimiento #2
    """
    return model.secondReq(catalog, country)


def thirdReq(catalog, category):
    """
    Solicita al model la información del requerimiento #3
    """
    idcat = findCategoryId(catalog, category)
    return model.thirdReq(catalog, idcat)


def fourthReq(catalog, data_size, country, tag):
    """
    Solicita al model la información del requerimiento #4
    """
    return model.fourthReq(catalog, data_size, country, tag)

