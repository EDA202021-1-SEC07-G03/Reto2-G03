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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import time
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import mergesort as mrg
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
  
    catalog = {'videos':None,
               'category':None}#,
               ''''video_id': None,
               'trending_date': None,
               'title': None,
               'channel_title': None,
               'category_id': None,
               'publish_time': None,
               'tags': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'comment_count': None,
               'thumbnail_link': None,
               'comments_disabled': None,
               'video_error_or_removed': None,
               'description': None,
               'country': None}'''
               

 
    catalog['videos'] = lt.newList('SINGLE_LINKED')
    catalog['category'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareMapBookIds)

    return catalog
def crear_nodo(categoria):
    d={categoria: lt.newList('ARRAY_LIST')}
    return d

def video_categoria(catalog,video):
    categoria=video['category_id']

    return
def agregar_categoria(catalog,category):
    catalog_category=catalog['category']
    if mp.cointains()
# Funciones para creacion de datos
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    lt.addLast(catalog['category'], category)
    


def addBook(catalog, book):
  
    lt.addLast(catalog['books'], book)
    mp.put(catalog['bookIds'], book['goodreads_book_id'], book)
    authors = book['authors'].split(",")  # Se obtienen los autores
    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
    addBookYear(catalog, book)


def addBookYear(catalog, book):

    try:
        years = catalog['years']
        if (book['original_publication_year'] != ''):
            pubyear = book['original_publication_year']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['books'], book)
    except Exception:
        return None


def newYear(pubyear):

    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry


def addBookAuthor(catalog, authorname, book):

    authors = catalog['authors']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newAuthor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['books'], book)
    author['average'] += float(book['average_rating'])
    totbooks = lt.size(author['books'])
    if (totbooks > 0):
        author['average_rating'] = author['average'] / totbooks



    

# Funciones de consulta
def nombre_id_categoria(catalog,nombre_categoria):
    i=0
    while i <= (lt.size(catalog['category'])-1):
        if nombre_categoria in ((lt.getElement(catalog['category'], i)['name']).lower()):
            id_categoria= lt.getElement(catalog['category'], i)['id']
            return id_categoria
        i+=1

# Funciones de comparacion
def cmpVideosbyViews(video1,video2):
    return(int(video1["views"])>int(video2["views"]))

def cmpVideosbyLikes(video1,video2):
    return(int(video1["likes"])>int(video2["likes"]))

def cmpVideosbyId(id1, id2):

    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1