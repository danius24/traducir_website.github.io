!pip install googletrans==4.0.0-rc1

from googletrans import Translator

nombre = input("Ingresa tu nombre: ")
print("Hola " + nombre + ", bienvenid@")

print("¿Qué deseas traducir?")
lenguaje = int(input("Elige (0) si es español-inglés o (1) si es inglés-español: "))

if lenguaje == 0:
    texto = input("Ingresa texto en español: ")
else:
    texto = input("Ingresa texto en inglés: ")

translator = Translator()

# Traducción del texto
if lenguaje == 0:
    traduccion = translator.translate(texto, dest='en', src='es')
    print(f'Tu texto fue traducido a inglés como : {traduccion.text}') #La expresión f' utiliza una f-string en Python. Una f-string (cadenas de formato) es una forma de formatear cadenas de texto de manera más concisa y legible. En este caso, la f-string está siendo utilizada para construir una cadena que incluye el texto de la traducción.
    print("Gracias por usar traductor.")

else:
    traduccion = translator.translate(texto, dest='es', src='en')
    print(f'Tu texto fue traducido a español como : {traduccion.text}')
    print("Gracias por usar traductor.")
    print('Te gustaría probar una función en español elige "si" o "no"')
    test= int(input("Te gustaría probar una función en español elige "si" o "no""))
    if test == "si":
      print("La actividad consiste en la busqueda del significado de las palabras en diferentes regiones de el habla hispana, con enfasis en el uso de jergas.")
      dic = {
    'amigo': 'parcero, pibe, pana, wey, tío, tronco, hermano, tronco, chaval, colega, compa, hermano, primo(pimo), picha, chocho, carnal, cuate, vato, causa, weon',
    'saludo': 'Que onda?, Que xopa?, Como esta la cosa?, Que más?, Que hue(Fue)?, Que hace wacho? Quibo?, Que pedo?, En que andas?, Que paso?'
}

    ans = input("Ingresa texto: ").lower()

        if ans == "amigo":
         print(ans + " también puede escribirse como: " + dic['amigo'])
        elif ans == "saludo":
         print(ans + " también puede escribirse como: " + dic['saludo'])
        else:
          print("Error")

   else text == "no":
    print("Se ha finalizado")