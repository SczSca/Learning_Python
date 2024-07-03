
def letras_unicas(palabra):
    '''
        obtiene los caracteres unicos de la palabra y los devuelve en orden alfabetico
        :param palabra: str. Ej: "palabra"
        :return: list of char. Ej: ['a','b','l','p','r']
    '''
    dic_char = {}
    characters = []

    for char in palabra:
        if char not in dic_char:
            dic_char[char] = None

    '''for key in dic_char.keys(): o esta tambien es una manera
        characters.append(key)'''
    characters = list(dic_char)
    characters.sort()

    return characters
print(letras_unicas("palabra"))