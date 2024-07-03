from time import perf_counter
lista = [2,10,2,5,12,10,10,20,30,40,10,0,2,5,5,5,5,5,5,333,20]

t1_start = perf_counter()

lista2 = list(set(lista))

t1_end = perf_counter()


t2_start = perf_counter()

lista3 = list(dict.fromkeys(lista))

t2_end = perf_counter()

lista3.sort()
print(f"usando set: {t1_end}-{t1_start} = {t1_end-t1_start}. {lista2}")
print(f"usando dict: {t2_end}-{t2_start} = {t2_end-t2_start}. {lista3}")

lista_numeros = [1,2,15,7,2]
def reducir_lista(lista):
    '''
        elimina elementos repetidos de la lista
        :param lista: list of int | float ej: [1,2,15,7,2]
        :return: list of int | float ej: [1,2,7]
    '''
    #Crea un dict con claves de los elementos de la lista. Como no pueden haber mas de una clave con el mismo nombre
    new_list = list(dict.fromkeys(lista))
    #organiza de menor a mayor la lista
    new_list.sort()
    #elimina el mayor, siendo este el ultimo elemento de la lista
    new_list.pop()
    
    return new_list
print(reducir_lista(lista_numeros))