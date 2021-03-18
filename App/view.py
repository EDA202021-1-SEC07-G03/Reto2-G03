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
import time
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos tendencia por país y categoría")
    print("3- Video trending por país")
    print("4- Video trending por categoría")
    print("5- Videos con más likes por país y tag")
    print("6- Salir")

"""
Menu principal
"""

def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    controller.loadData(catalog)
catalog = None



while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        #Primer video cargado
        print('Title: '+ catalog['videos']['elements'][0]['title'])
        print('Channel title: '+ catalog['videos']['elements'][0]['channel_title'])
        print('Trending date: '+ catalog['videos']['elements'][0]['trending_date'])
        print('Country: '+ catalog['videos']['elements'][0]['country'])
        print('Views: '+ catalog['videos']['elements'][0]['views'])
        print('Likes: '+ catalog['videos']['elements'][0]['likes'])
        print('Dislikes: '+ catalog['videos']['elements'][0]['dislikes'])
        #Categorias
        print(catalog['category']['elements'])
        
    elif int(inputs)==2:
        pais=(str(input('Digite el pais de su interes: ')).lower())
        nombre_categoria=(str(input('Digite la categoria de su interes: ')).lower())
        n= int(input('Indique la cantidad de videos que desea recibir: '))
        subsub_list= controller.videos_pais_categoria(catalog,pais,nombre_categoria,n)
        i=0
        while i < (lt.size(subsub_list)):
            print('VIDEO ' +str(i+1)+ ' : '+('Trending date: '+ str(subsub_list['elements'][i]['trending_date']))+
            ' , Title: '+ str(subsub_list['elements'][i]['title'])+
            ' , Channel title: ' + str(subsub_list['elements'][i]['channel_title'])+ 
            ' , Publish time: ' + str(subsub_list['elements'][i]['publish_time'])+ 
            ' , Views: ' + str(subsub_list['elements'][i]['views'])+
            ' , Likes: '+ str(subsub_list['elements'][i]['likes'])+
            ' , Dislikes: '+ str(subsub_list['elements'][i]['dislikes']))
            i+=1
        
    elif int(inputs)==3:
        pais=(str(input('Digite el pais de su interes: ')).lower())
        trend=controller.videos_tendencia_pais(catalog,pais)
        n=''
        for info in trend:
           n+=info.title()+': '+str(trend[info])+', '
        print(n[:-2]) 
        pass
        
    elif int(inputs)==4:
        nombre_categoria=(str(input('Digite la categoria de su interes: ')).lower())
        trend=controller.videos_tendencia_categoria(catalog,nombre_categoria)
        n=''
        for info in trend:
           n+=info.title()+': '+str(trend[info])+', '
        print(n[:-2]) 
        pass

    elif int(inputs)==5:
        pais=(str(input('Digite el pais de su interes: ')).lower())
        tag=(str(input('Digite el tag de su interes: ')).lower())
        cantidad= int(input('Indique la cantidad de videos que desea recibir: '))
        subsub_list= controller.videos_pais_tag(catalog,pais,tag,cantidad)
        i=0
        while i < (lt.size(subsub_list)):
            print('VIDEO ' +str(i+1)+ ' : '+
            ('Title: '+ str(lt.getElement(subsub_list,i)['title'])+
            ' , Channel title: ' + str(lt.getElement(subsub_list,i)['channel_title'])+ 
            ' , Publish time: ' + str(lt.getElement(subsub_list,i)['publish_time'])+ 
            ' , Views: ' + str(lt.getElement(subsub_list,i)['views'])+
            ' , Likes: '+ str(lt.getElement(subsub_list,i)['likes'])+
            ' , Dislikes: '+ str(lt.getElement(subsub_list,i)['dislikes'])+
            ' , Tags: '+str(lt.getElement(subsub_list,i)['tags'])))
            i+=1

    else:
        sys.exit(0)
sys.exit(0)