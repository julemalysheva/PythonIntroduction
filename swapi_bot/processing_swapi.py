def print_people(dict):
    txt = ''
    for k,v in dict.items():
        if v != None:
            txt+= f'\n{k}:\t{v}'
    return txt    