from random import randint
from math import isnan
guest = ""
while guest == "":
    guest = input("Introduzca su nombre: ")

rdm_num = randint(1,100)

dic_text_prompts = {"start": "Adivina el numero entre el 1 y el 100.", "out_of_range": "Su numero está fuera de rango.", "lower": "El número a adivinar es menor al que introdujo.", "higher": "El número a adivinar es mayor al que introdujo.", "NaN": "Lo que introdujo no es un número.", "lost": f"Usted no logró adivinar el número ({rdm_num}) en los 8 intentos :(", "success": f"Efectivamente, el número es {rdm_num}."}
text_prompt = dic_text_prompts["start"]
for attempt in range(1,9):
    try:
        guest_num= int(input(f"{guest}, Este es su intento {attempt}. {text_prompt} Diga un número: "))
        if 1 > guest_num or guest_num > 100:
            text_prompt = dic_text_prompts["out_of_range"]
        elif rdm_num < guest_num:
            text_prompt = dic_text_prompts["lower"]
        elif rdm_num > guest_num:
            text_prompt = dic_text_prompts["higher"]
        elif  rdm_num == guest_num:
            text_prompt = dic_text_prompts["success"]
            print(f"{text_prompt} Lo logró en el intento {attempt}!")
            break
    except:
        text_prompt = dic_text_prompts["NaN"]

    

if text_prompt != dic_text_prompts["success"]:    
    print(dic_text_prompts["lost"] )