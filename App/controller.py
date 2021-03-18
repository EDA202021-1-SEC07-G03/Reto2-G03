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
import time
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategory(catalog)
    
def loadVideos(catalog):
    vidsfile = cf.data_dir + 'videos-large.csv'
    input_file1 = csv.DictReader(open(vidsfile, encoding='utf-8'))
    for video in input_file1:
        model.addVideo(catalog, video)

def loadCategory(catalog):
    categoryfile = cf.data_dir + 'category-id.csv'
    input_file2 = csv.DictReader(open(categoryfile, encoding='utf-8'),delimiter=('\t'))
    for category in input_file2:
        model.addCategory(catalog, category)

# Funciones de consulta sobre el catálogo
def videos_pais_categoria(catalog,pais,nombre_categoria,n):
    subsub_list= model.videos_pais_categoria(catalog,pais,nombre_categoria,n)
    return subsub_list
def videos_tendencia_categoria (catalog, nombre_categoria):
    return model.videos_tendencia_categoria(catalog,nombre_categoria)
def videos_tendencia_pais(catalog,pais):
    return model.videos_tendencia_pais(catalog,pais)
def videos_pais_tag(catalog,pais,tag,cantidad):
    subsub_list= model.videos_pais_tag(catalog,pais,tag,cantidad)
    return subsub_list
