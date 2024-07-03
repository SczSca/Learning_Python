def devolver_distintos(n1,n2,n3):
    '''
        En base a las condicionales sobre la suma de los tres parametros, retornara algo
        :param n1: int | float. Un número
        :param n2: int | float. Un número
        :param n3: int | float. Un número
        :return: int | float. Uno de los tres parametros
    '''

    result = 0

    nums = [n1,n2,n3]
    nums.sort()
    suma = n1 + n2 + n3

    if suma > 15:
        result = nums[2]
    elif suma < 10:
        result = nums[0]
    else:
        result = nums[1]
    return result

def devolver_distintos2(n1,n2,n3):
    numeros = [n2,n3]

    menor = n1
    mayor
    medio

    for i in range(len(numeros)) :
        print(i)
        if menor > numeros[i]:
            if medio > mayor:
                mayor = medio
            medio = menor

            menor = numeros[i]
        else:
            if medio > numeros[i]:
                mayor = medio
                
            else:
                mayor = numeros[i]
            medio = numeros[i]

        #if menor < numeros[i] < mayor:
           # medio = numeros[i]
    print(menor, medio, mayor)

def devolver_distintos3(n1,n2,n3):
    numeros = [n2,n3]

    menor = n1
    mayor = n1
    medio = n1

    for i in range(len(numeros)) :
        print(i)
        if menor > numeros[i]:
            if medio > mayor:
                mayor = medio
            medio = menor

            menor = numeros[i]
        else:
            if medio > numeros[i]:
                mayor = medio

                medio = numeros[i]
                
            else:
                mayor = numeros[i]

        if menor < numeros[i] < mayor:
           medio = numeros[i]
    print(menor, medio, mayor)
print(devolver_distintos(3,1,2))

