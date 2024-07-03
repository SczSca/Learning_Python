from time import perf_counter
def tiene_ceros_consecutivos(*args):
    '''
        Devuelve true si dentro de args hay dos 0 consecutivos
        O(n) donde:
        n: cantidad de 0 en los args
        :param args: list of int. Ej: [5,6,1,0,0,9,3,5]
        :return: bool. Ej: True
    '''
    start_time = perf_counter()
    result = True
    try:
        nums = list(args)
        zero_pos = nums.index(0)
        

        while zero_pos != -1:
            if zero_pos + 1 and nums[zero_pos] == nums[zero_pos + 1]:

                break

            zero_pos = nums.index(0, zero_pos + 2)

    except:
        result = False

    end_time = perf_counter()
    print(f'Execution time: {end_time - start_time} seconds')
    return result

def tiene_ceros_consecutivos2(*args):
    '''
        Devuelve true si dentro de args hay dos 0 consecutivos
        O(n) donde:
        n: cantidad de 0 en los args
        :param args: list of int. Ej: [5,6,1,0,0,9,3,5]
        :return: bool. Ej: True
    '''
    start_time = perf_counter()
    result = False
    # Iterar sobre la lista buscando ceros consecutivos
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            result = True
            break

    end_time = perf_counter()
    print(f'Execution time: {end_time - start_time} seconds')
    return result

def tiene_ceros_consecutivos3(*args):
    '''
        Devuelve true si dentro de args hay dos 0 consecutivos
        O(n) donde:
        n: cantidad de elementos en los args
        :param args: list of int. Ej: [5,6,1,0,0,9,3,5]
        :return: bool. Ej: True
    '''

    result = False
    # Iterar sobre la lista buscando ceros consecutivos
    i = 0
    while i < len(args) - 1:
        if args[i] == 0:
            if args[i + 1] == 0:
                result = True
                break
            else:
                #Si no hay un 0 consecutivo, hacer dos saltos
                i += 1
        i += 1

    return result


args = [5,6,1,0,0,9,3,5]
print(tiene_ceros_consecutivos(*args))
print(tiene_ceros_consecutivos2(*args))
print(tiene_ceros_consecutivos3(*args))