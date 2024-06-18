from Text_Analyzer import TextAnalyzer

texto = ""
letras = []
while True:
    texto = input("Introduzca un texto: ").lower()
    letras = input("Introduzca 3 letras separadas por ',': ").lower().split(',')
    if bool(texto) and len(letras) == 3:
        break
    print("Hubo un error con las entradas, intentemos de nuevo")



text_analyzer = TextAnalyzer()
result = {"repeated_letters_counter": text_analyzer.count_repeated_letters(texto,letras), "words_counter": text_analyzer.count_words(texto), "reverse_text": text_analyzer.reverse_text(texto), "has_python": text_analyzer.contains_python(texto)}
result.update(text_analyzer.first_last_letter(texto))
print(result)