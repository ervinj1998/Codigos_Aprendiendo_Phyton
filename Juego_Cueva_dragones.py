#Juego "Cueva de dragones"
import random
import time

def Mostrar_Intro():
    print("Binvenido al juego CUEVA DE DRAGONES\n")
    print('Estás en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas. En una de ellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y está hambriento, y te devorará inmediatamente.')
    print()

def Elegir_Cueva():
    eleccion = ''
    while eleccion != '1' and eleccion != '2':
        print("En cual cueva te atreves a entrar ehhh ? (1  ó  2!!!!!")
        eleccion=input()
        return eleccion

def exploracion(elegir):
    print('vas entrando a la cueva lentamente..')
    time.sleep(2)
    print('es oscura y espeluznante......')
    time.sleep(2)
    print('Un dragon aparece subitamente y zas........')
    print()
    time.sleep(2)

    cueva_amigable = random.randint(1,2)

    if elegir == str(cueva_amigable):
        print('Se abre camino y te regale todo su tesoro..')

    else:
        print('Te engulle de un solo bocado y hasta ahi llegastes.')

jugar_de_nuevo = 's'
while jugar_de_nuevo == 'si' or jugar_de_nuevo== 's':
        Mostrar_Intro()
        num_cueva=Elegir_Cueva()
        exploracion(num_cueva)

        print('Quieres jugar de nuevo? si ó no')
        jugar_de_nuevo=input()
        

        

        

    
    
