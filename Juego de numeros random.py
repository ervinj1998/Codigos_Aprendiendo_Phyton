#Este es un juego que adivina un numero random
import random

intentos = 0

print ('Hola !!! , dime tu nombre: ')
nombre = input()

numero = random.randint(1, 10)
print ('Mucho gusto' + nombre + ', estoy pensando en un numero aleatorio del 1 al 10')
while intentos < 6:
    print('Intenta adivinar.')
    respuesta = input()
    respuesta = int(respuesta)

    intentos = intentos +1

    if respuesta < numero:
            print('Tu numero es muy bajo')

    if respuesta > numero:
            print('Tu numero es muy alto ')

    if respuesta == numero:
            break

if respuesta == numero:
        intentos = str(intentos)
        print('ADIVINASTES !!!' +nombre+ ' en ' +intentos+ 'veces')

if respuesta != numero:
    numero = str(numero)
    print('lo siento no adivinastes, el numero era:'+ numero)
