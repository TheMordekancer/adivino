#nombre:Franco Martin Veramendi 
#nr alumno:16738
import random
numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 5 intentos para adivinar un numero entre 0 y 100")
intento = 1
while intento < 6 and not gane:
    numeroIngresado = int(input('Ingresa tu número: '))
    if numeroIngresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
    intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
