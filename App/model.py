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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
   
    catalog = {'videos': lt.newList('ARRAY_LIST'), 'category': lt.newList('ARRAY_LIST')}
    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    lt.addLast(catalog['category'], category)
    
# Funciones para creacion de datos
def nombre_id_categoria(catalog,nombre_categoria):
    i=0
    while i <= (lt.size(catalog['category'])-1):
        if nombre_categoria in ((lt.getElement(catalog['category'], i)['name']).lower()):
            id_categoria= lt.getElement(catalog['category'], i)['id']
            return id_categoria
        i+=1
    
# Funciones de consulta
def videos_pais_categoria(catalog,pais,nombre_categoria,n):
    id_categoria = nombre_id_categoria(catalog,nombre_categoria)
    sub_list=lt.newList('ARRAY_LIST')
    j=1
    while j <  (lt.size(catalog['videos'])):
        if (pais in (lt.getElement(catalog['videos'], j)['country'].lower())) and (id_categoria == (lt.getElement(catalog['videos'], j)['category_id'])):
            lt.addLast(sub_list, lt.getElement(catalog['videos'], j))
        j+=1

    sub_list = sub_list.copy()
    mrg.sort(sub_list,cmpVideosbyViews)
    subsub_list = lt.subList(sub_list, 1, n)
    return subsub_list
def videos_tendencia_pais(catalog,pais):
    dates={}
    trend={}
    mayor=-1
    j=1
    while j <  (lt.size(catalog['videos'])):
        titulo=(lt.getElement(catalog['videos'], j)['title'])
        date=(lt.getElement(catalog['videos'], j)['trending_date'])
        channel=(lt.getElement(catalog['videos'], j)['channel_title'])
        country=(lt.getElement(catalog['videos'], j)['country'])
        if pais.lower() in country.lower():
            info=titulo+';;'+channel+';;'+country
            if dates.get(info)==None:
                dates[info]=lt.newList('ARRAY_LIST')
                lt.addLast(dates[info],date)
            else:
                lt.addLast(dates[info],date)
        j+=1
    for info in dates:
        if lt.size(dates[info])>mayor:
            mayor=lt.size(dates[info])
            i=info.split(';;')
            trend['title']=i[0]
            trend['channel']=i[1]
            trend['country']=i[2]
            trend['days']=mayor
    return trend
def videos_tendencia_categoria (catalog, nombre_categoria):
    id_categoria = nombre_id_categoria(catalog,nombre_categoria)
    j=1
    dates={}
    trend={}
    mayor=-1
    while j <  (lt.size(catalog['videos'])):
        if id_categoria == (lt.getElement(catalog['videos'], j)['category_id']):
            titulo=(lt.getElement(catalog['videos'], j)['title'])
            date=(lt.getElement(catalog['videos'], j)['trending_date'])
            channel=(lt.getElement(catalog['videos'], j)['channel_title'])
            info=titulo+';;'+channel+';;'+id_categoria
            if dates.get(info)==None:
                dates[info]=lt.newList('ARRAY_LIST')
                lt.addLast(dates[info],date)
            else:
                lt.addLast(dates[info],date)
        j+=1
    for info in dates:
        if lt.size(dates[info])>mayor:
            mayor=lt.size(dates[info])
            i=info.split(';;')
            trend['title']=i[0]
            trend['channel']=i[1]
            trend['category id']=i[2]
            trend['days']=mayor
    return trend
def videos_pais_tag(catalog,pais,tag,cantidad):
    i=0
    titles=lt.newList('ARRAY_LIST')
    sub_list= mrg.sort(catalog['videos'],cmpVideosbyLikes)
    sub_list = sub_list.copy()

    subsub_list=lt.newList('ARRAY_LIST')
    while i <  (lt.size(sub_list)):
        str_tags= lt.getElement(sub_list, i)['tags']
        str_tags_clean1= str_tags.replace('"','')
        str_tags_clean1= str_tags_clean1.replace('(','')
        str_tags_clean1= str_tags_clean1.replace(')','')
        str_tags_clean2= str_tags_clean1.replace('|',' ')

        list_tags1=str_tags_clean1.split('|')
        list_tags2=str_tags_clean2.split()
        list_tags3 = list_tags1 + list_tags2
        if  (pais in (lt.getElement(sub_list, i)['country']).lower()) and (tag in list_tags3) and lt.isPresent(titles,(lt.getElement(sub_list, i)['title']))==0:
            lt.addLast(subsub_list, lt.getElement(sub_list, i))
            lt.addLast(titles,lt.getElement(sub_list, i)['title'])
        i+=1

    subsub_list = lt.subList(subsub_list, 1, cantidad)
    return subsub_list

# Funciones de comparacion
def cmpVideosbyViews(video1,video2):
    return(int(video1["views"])>int(video2["views"]))

def cmpVideosbyLikes(video1,video2):
    return(int(video1["likes"])>int(video2["likes"]))