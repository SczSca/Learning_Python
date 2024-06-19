from random import choice
from os import system
from os import name
class Ahorcado:
    
    #intentos para adivinar letras
    intentos = 6
    palabra_adivinar = ""
    espacio_adivinar = []
    letras_usadas = []

    '''
        Constructor que inicializa el ahorcado con una lista de palabras
        :param palabras: Lista de str. Palabras para adivinar

    '''

    def __init__(self, palabras):
        self.banco_palabras = palabras


    '''
        Selecciona una palabra aleatoria y muestra el ahorcado con espacios en blanco
    '''
    def elegir_palabra(self):
        self.palabra_adivinar = choice(self.banco_palabras)
        for i in range(len(self.palabra_adivinar)):
            self.espacio_adivinar.append('_')


    '''
        Comprueba si la letra se encuentra en la palabra y muestra el estado del ahorcado actual
        :param letra: str. Letra a intentar adivinar
    '''
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
        
        self.limpiar_terminal()
        print(mensaje)

        return 1


    '''
        Comprueba si se ha ganado el juego
        :return: bool
    '''
    def coincidir_palabra(self):
        return "".join(self.espacio_adivinar) == self.palabra_adivinar
    

    '''
        Limpia la terminal según el sistema operativo actual
    '''
    def limpiar_terminal(self):
        if name == 'nt':  # Windows
            system('cls')
        elif name == 'posix':  # Linux o macOS
            system('clear')
        else:
            print("Sistema operativo no compatible")

    '''
        Inicia el juego del ahorcado
    '''
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
            mensaje = f"Una lastima, se le acabaron los intentos. La palabra era {self.palabra_adivinar}."
        
        print(mensaje)

    
