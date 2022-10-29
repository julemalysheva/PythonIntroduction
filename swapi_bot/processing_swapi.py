import requests
from json import *


def print_people(dict):
    txt = ''
    not_li = ['created', 'edited','url']
    for k,v in dict.items():
        # добавить обработку значения, если это ссылка или список ссылок - формировать новый get запрос для
        # получения названия
        if k not in not_li and v != None:
            if k == 'homeworld':
                r = requests.get(v).json()  
                txt+= f'\n{str(k).ljust(20)}-\t\t{r["name"]}' 
            elif k == 'films':
                films = []
                for el in v:
                    r = requests.get(el).json()
                    films.append(r['title']) 
                txt+= f'\n{str(k).ljust(20)}-\t\t{" ,".join(films)}' 
            elif k == 'species':
                species = []
                for el in v:
                    r = requests.get(el).json()
                    species.append(r['name']) 
                txt+= f'\n{str(k).ljust(20)}-\t\t{" ,".join(species)}' 
            elif k == 'vehicles':
                vehicles = []
                for el in v:
                    r = requests.get(el).json()
                    vehicles.append(r['name']) 
                txt+= f'\n{str(k).ljust(20)}-\t\t{" ,".join(vehicles)}' 
            elif k == 'starships':
                starships = []
                for el in v:
                    r = requests.get(el).json()
                    starships.append(r['name']) 
                txt+= f'\n{str(k).ljust(20)}-\t\t{" ,".join(starships)}' 
            else:
                txt+= f'\n{str(k).ljust(20)}-\t\t{v}'
    return txt    