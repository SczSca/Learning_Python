from random import choice
class Ahorcado:
    
    #intentos para adivinar letras
    intentos = 6
    palabra_adivinar = ""
    indice_palabra = -1
    espacio_adivinar = []
    letras_usadas = []

    def __init__(self, palabras):
        self.banco_palabras = palabras

    def elegir_palabra(self):
        self.palabra_adivinar = choice(self.banco_palabras)
        self.indice_palabra = self.banco_palabras.index(self.palabra_adivinar)
        for i in range(len(self.palabra_adivinar)):
            self.espacio_adivinar.append('_')

    def adivinar_letra(self, letra):
        mensaje = f"Le quedan {self.intentos} intentos. Así quedó la palabra: "

        if len(letra) > 1:
            self.intentos -= 1
            print("Tiene que ser una letra, no se pueden más. Se te restará el intento. Intentos: ", self.intentos)
            return -1
        
        self.letras_usadas.append(letra)
        letra_pos = self.palabra_adivinar.find(letra)
        indices = []
        tiene_letra = True if letra_pos != -1 else False

        counter = 0
        while letra_pos != -1:
            indices.append(letra_pos)
            self.espacio_adivinar[letra_pos] = self.palabra_adivinar[letra_pos]

            letra_pos = self.palabra_adivinar.find(letra, indices[counter] + 1)
            counter += 1
        
        if tiene_letra:
            mensaje = "Esa letra si se encuentra!. " + mensaje + "".join(self.espacio_adivinar)
        else:
            self.intentos -= 1
            mensaje = f"No se encontró la letra . Le quedan {self.intentos} intentos."
        
        print(mensaje)

        return 1

    def coincidir_palabra(self):
        return "".join(self.espacio_adivinar) == self.palabra_adivinar
    
    def iniciar_juego(self):
        self.intentos = 6
        self.elegir_palabra()
        mensaje = ""

        print("Bienvenido al juego del ahorcado. Usted tiene 6 intentos")

        while self.intentos > 0:
            letra = input(f"Introduzca una letra para adivinar la palabra: {''.join(self.espacio_adivinar)} . Las letras ya utilizadas son: {self.letras_usadas} ")
            self.adivinar_letra(letra)
            if self.coincidir_palabra():
                break

        if self.coincidir_palabra():
            mensaje = f"¡Felicidades! ¡Usted logró adivinar la palabra {''.join(self.espacio_adivinar)}! ¡Le quedaron {self.intentos} intentos!"
        else:
            mensaje = f"Una lastima, se le acabaron los intentos. La palabra era {self.banco_palabras[self.indice_palabra]}"
        
        print(mensaje)

    
